import asyncio
import os
import re
from typing import Union

import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from py_yt import VideosSearch, Playlist
import aiohttp
from Bikash.config import *


def time_to_seconds(time):
    if not time: return 0
    stringt = str(time)
    if stringt == "None": return 0
    try:
        return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))
    except Exception:
        return 0

async def download_song(link: str) -> str:
    video_id = link.split("v=")[-1].split("&")[0] if "v=" in link else link
    if not video_id or len(video_id) < 3: return None
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mp3")
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0: return file_path
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{API_URL}/download", params={"url": video_id, "type": "audio", "api_key": API_KEY}, timeout=aiohttp.ClientTimeout(total=300)) as resp:
                if resp.status != 200: return None
                with open(file_path, "wb") as f:
                    async for chunk in resp.content.iter_chunked(131072): f.write(chunk)
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0: return file_path
        return None
    except Exception:
        if os.path.exists(file_path):
            try: os.remove(file_path)
            except: pass
        return None

async def download_video(link: str) -> str:
    video_id = link.split("v=")[-1].split("&")[0] if "v=" in link else link
    if not video_id or len(video_id) < 3: return None
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mp4")
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0: return file_path
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{API_URL}/download", params={"url": video_id, "type": "video", "api_key": API_KEY}, timeout=aiohttp.ClientTimeout(total=600)) as resp:
                if resp.status != 200: return None
                with open(file_path, "wb") as f:
                    async for chunk in resp.content.iter_chunked(131072): f.write(chunk)
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0: return file_path
        return None
    except Exception:
        if os.path.exists(file_path):
            try: os.remove(file_path)
            except: pass
        return None

class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.status = "https://www.youtube.com/oembed?url="
        self.listbase = "https://youtube.com/playlist?list="
        self.reg = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        return bool(re.search(self.regex, link))

    async def url(self, message_1: Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message: messages.append(message_1.reply_to_message)
        for message in messages:
            if message.entities:
                for entity in message.entities:
                    if entity.type == MessageEntityType.URL:
                        text = message.text or message.caption
                        return text[entity.offset: entity.offset + entity.length]
            elif message.caption_entities:
                for entity in message.caption_entities:
                    if entity.type == MessageEntityType.TEXT_LINK: return entity.url
        return None

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        if "&" in link: link = link.split("&")[0]
        try:
            results = VideosSearch(link, limit=1)
            res = await results.next()
            if not res.get("result"): return None, None, 0, None, None
            result = res["result"][0]
            title = result["title"]
            duration_min = result["duration"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            vidid = result["id"]
            duration_sec = time_to_seconds(duration_min)
            return title, duration_min, duration_sec, thumbnail, vidid
        except Exception:
            return None, None, 0, None, None

    async def title(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        if "&" in link: link = link.split("&")[0]
        try:
            results = VideosSearch(link, limit=1)
            res = await results.next()
            if not res.get("result"): return None
            return res["result"][0]["title"]
        except Exception: return None

    async def duration(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        if "&" in link: link = link.split("&")[0]
        try:
            results = VideosSearch(link, limit=1)
            res = await results.next()
            if not res.get("result"): return None
            return res["result"][0]["duration"]
        except Exception: return None

    async def thumbnail(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        if "&" in link: link = link.split("&")[0]
        try:
            results = VideosSearch(link, limit=1)
            res = await results.next()
            if not res.get("result"): return None
            return res["result"][0]["thumbnails"][0]["url"].split("?")[0]
        except Exception: return None

    async def video(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        if "&" in link: link = link.split("&")[0]
        try:
            downloaded_file = await download_video(link)
            if downloaded_file: return 1, downloaded_file
            return 0, "Video download failed"
        except Exception as e:
            return 0, f"Video download error: {e}"

    async def playlist(self, link, limit, user_id, videoid: Union[bool, str] = None):
        if videoid: link = self.listbase + link
        if "&" in link: link = link.split("&")[0]
        try: plist = await Playlist.get(link)
        except Exception: return []
        videos = plist.get("videos") or []
        ids = []
        for data in videos[:limit]:
            if not data: continue
            vid = data.get("id")
            if not vid: continue
            ids.append(vid)
        return ids

    async def track(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        if "&" in link: link = link.split("&")[0]
        try:
            results = VideosSearch(link, limit=1)
            res = await results.next()
            if not res.get("result"): return None, None
            result = res["result"][0]
            track_details = {
                "title": result["title"], "link": result["link"], "vidid": result["id"],
                "duration_min": result["duration"], "thumb": result["thumbnails"][0]["url"].split("?")[0],
            }
            return track_details, result["id"]
        except Exception:
            return None, None

    async def formats(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        if "&" in link: link = link.split("&")[0]
        ytdl_opts = {"quiet": True}
        ydl = yt_dlp.YoutubeDL(ytdl_opts)
        try:
            with ydl:
                formats_available = []
                r = ydl.extract_info(link, download=False)
                for format in r["formats"]:
                    try:
                        if "dash" not in str(format["format"]).lower():
                            formats_available.append({
                                "format": format["format"], "filesize": format.get("filesize"),
                                "format_id": format["format_id"], "ext": format["ext"],
                                "format_note": format["format_note"], "yturl": link,
                            })
                    except Exception: continue
            return formats_available, link
        except Exception:
            return [], link

    async def slider(self, link: str, query_type: int, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        if "&" in link: link = link.split("&")[0]
        try:
            a = VideosSearch(link, limit=10)
            res = await a.next()
            result = res.get("result")
            if not result or query_type >= len(result): return None, None, None, None
            title = result[query_type]["title"]
            duration_min = result[query_type]["duration"]
            vidid = result[query_type]["id"]
            thumbnail = result[query_type]["thumbnails"][0]["url"].split("?")[0]
            return title, duration_min, thumbnail, vidid
        except Exception:
            return None, None, None, None

    async def download(self, link: str, mystic, video: Union[bool, str] = None, videoid: Union[bool, str] = None, songaudio: Union[bool, str] = None, songvideo: Union[bool, str] = None, format_id: Union[bool, str] = None, title: Union[bool, str] = None) -> str:
        if videoid: link = self.base + link
        try:
            if video: downloaded_file = await download_video(link)
            else: downloaded_file = await download_song(link)
            if downloaded_file: return downloaded_file, True
            return None, False
        except Exception: return None, False

    async def get_related_streams(self, video_id: str):
        PIPED_INSTANCES = [
            "https://pipedapi.kavin.rocks",
            "https://pipedapi.adminforge.de",
            "https://api.piped.projectsegfau.lt",
            "https://pipedapi.in.projectsegfau.lt"
        ]
        for instance in PIPED_INSTANCES:
            try:
                url = f"{instance}/streams/{video_id}"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as resp:
                        if resp.status == 200:
                            data = await resp.json()
                            related = data.get("relatedStreams", [])
                            results = []
                            for item in related[:20]:
                                vid_url = item.get("url", "")
                                if "v=" in vid_url:
                                    vid_id = vid_url.split("v=")[-1].split("&")[0]
                                else:
                                    vid_id = vid_url.replace("/watch?v=", "").strip("/")
                                if vid_id:
                                    results.append({
                                        "id": vid_id,
                                        "title": item.get("title"),
                                        "duration": item.get("duration", 0),
                                        "thumb": item.get("thumbnail")
                                    })
                            if results: return results
            except Exception: continue
        
        try:
            details = await self.details(video_id, videoid=True)
            if details and details[0]:
                title = details[0]
                results = VideosSearch(f"{title} song", limit=10)
                res = await results.next()
                if res.get("result"):
                    return [{
                        "id": item["id"], "title": item["title"],
                        "duration": time_to_seconds(item.get("duration", "0:00")),
                        "thumb": item["thumbnails"][0]["url"].split("?")[0]
                    } for item in res["result"]]
        except Exception: pass
        return []

YouTube = YouTubeAPI()
