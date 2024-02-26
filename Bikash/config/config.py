import os
import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
  load_dotenv("Internal")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_ID = int(getenv("BOT_ID", "7198638721"))
BOT_TOKEN = getenv("BOT_TOKEN")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "༺ 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 ༻")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1439222689").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/BikashHalderNew/Bgtplayer")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "bikash")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/BikashGadgetsTech")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Bgt_Chat")
SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "150"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
SET_CMDS = getenv("SET_CMDS", False)
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

############################
COMMAND_PREFIXES.append('')
OWNER_ID.append(1439222689)
############################
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
############################

START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/c8135608b7f9f77541a82.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://te.legra.ph/file/3127b3484676bd2254e97.jpg")

PLAYLIST_IMG_URL = "https://te.legra.ph/file/c8135608b7f9f77541a82.jpg"
GLOBAL_IMG_URL = "https://te.legra.ph/file/2e2741f5dfe9f62eed91d.png"
STATS_IMG_URL = "https://te.legra.ph/file/2be94fc76030833b51a78.png"
TELEGRAM_AUDIO_URL = "https://graph.org/file/d68f9ff85714d4dbc6069.png"
TELEGRAM_VIDEO_URL = "https://graph.org/file/d68f9ff85714d4dbc6069.png"
STREAM_IMG_URL = "https://graph.org/file/93882ae5ea01a7bf687b1.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/0d021735560cbf0bb749a.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/4a8cc770a5bea2136bada.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/8427fca139bcbf3c54bcb.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/8427fca139bcbf3c54bcb.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/8427fca139bcbf3c54bcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "resources/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/3127b3484676bd2254e97.jpg"

if START_IMG_URL:
    if START_IMG_URL != "resources/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/c8135608b7f9f77541a82.jpg"
