# Powered By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Updates
# Join @AdityaCheats For Hacks
# Join Our Chats @Bgt_Chat & @Adityadiscus 

import asyncio
import time

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from py_yt import VideosSearch
from pyrogram.enums import ChatType, ParseMode
from Bikash import config
from Bikash.config import BANNED_USERS
from Bikash.config import OWNER_ID
from Bikash.Bgt import get_command, get_string
from Bikash import Telegram, YouTube, app
from Bikash.misc import SUDOERS, _boot_
from plugins.play.playlist import del_plist_msg
from plugins.sudo.sudoers import sudoers_list
from Bikash.utils.database import (add_served_chat,
                                       add_served_user,
                                       get_served_chats,
                                       get_served_users,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from Bikash.utils.decorators.language import LanguageStart
from Bikash.utils.formatters import get_readable_time
from Bikash.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

loop = asyncio.get_running_loop()


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.private
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                       photo=config.START_IMG_URL,
                       caption=_["help_1"], reply_markup=keyboard
            )
        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        if name[0:3] == "sta":
            m = await message.reply_text(
                f"🥱 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥 𝐒𝐭𝐚𝐭𝐬 𝐅𝐫𝐨𝐦 {config.MUSIC_BOT_NAME} 𝐒𝐞𝐫𝐯𝐞𝐫."
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐞𝐝𝐢𝐚]({config.SUPPORT_GROUP}) ** 𝐏𝐥𝐚𝐲𝐞𝐝 {count} 𝐓𝐢𝐦𝐞𝐬**\n\n"
                    else:
                        msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(
                    None, get_stats
                )
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.mention
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} 𝐉𝐮𝐬𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐓𝐡𝐞 𝐁𝐨𝐭 𝐓𝐨 𝐂𝐡𝐞𝐜𝐤 <code>𝐒𝐮𝐝𝐨𝐥𝐢𝐬𝐭</code>\n\n**𝐔𝐬𝐞𝐫 𝐈𝐝:** {sender_id}\n**𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text(
                    "𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐆𝐞𝐭 𝐋𝐲𝐫𝐢𝐜𝐬."
                )
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name == "verify":
            await message.reply_text(f"𝐇𝐞𝐲 {message.from_user.mention},\n𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐕𝐞𝐫𝐢𝐟𝐲𝐢𝐧𝐠 𝐘𝐨𝐮𝐫𝐬𝐞𝐥𝐟 𝐈𝐧 {config.MUSIC_BOT_NAME}, 𝐍𝐨𝐰 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐆𝐨 𝐁𝐚𝐜𝐤 & 𝐒𝐭𝐚𝐫𝐭 𝐔𝐬𝐢𝐧𝐠 𝐌𝐞.")
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.mention
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} 𝐉𝐮𝐬𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐓𝐡𝐞 𝐁𝐨𝐭 𝐓𝐨 <code> 𝐕𝐞𝐫𝐢𝐟𝐲 𝐇𝐢𝐦𝐬𝐞𝐥𝐟</code>\n\n**𝐔𝐬𝐞𝐫 𝐈𝐝:** {sender_id}\n**𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:** {sender_name}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🌺**𝐓𝐫𝐚𝐜𝐤 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 **🌺

🥀 **𝐓𝐢𝐭𝐥𝐞:** {title}

⏳ **𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧:** {duration} ᴍɪɴᴜᴛᴇs
👀 **𝐕𝐢𝐞𝐰𝐬:** `{views}`
⏰ **𝐏𝐮𝐛𝐥𝐢𝐬𝐡𝐞𝐝 𝐎𝐧:** {published}
🎥 **𝐂𝐡𝐚𝐧𝐧𝐞𝐥:** {channel}
📎 **𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐋𝐢𝐧𝐤:** [𝐕𝐢𝐬𝐢𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥]({channellink})
🔗 **𝐋𝐢𝐧𝐤:** [𝐖𝐚𝐭𝐜𝐡 𝐎𝐧 𝐘𝐨𝐮𝐭𝐮𝐛𝐞]({link})

💖 𝐒𝐞𝐚𝐫𝐜𝐡 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 {config.MUSIC_BOT_NAME}"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="• 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 •", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="🌿 𝐆𝐫𝐨𝐮𝐩 🌿", url=config.SUPPORT_GROUP
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.mention
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} 𝐉𝐮𝐬𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐨𝐭 𝐓𝐨 𝐂𝐡𝐞𝐜𝐤 <code> 𝐓𝐫𝐚𝐜𝐤 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧</code>\n\n**𝐔𝐬𝐞𝐫 𝐈𝐝:** {sender_id}\n**𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_2"].format(
                        config.MUSIC_BOT_NAME
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            except:
                await message.reply_text(
                    _["start_2"].format(config.MUSIC_BOT_NAME),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await message.reply_text(
                _["start_2"].format(config.MUSIC_BOT_NAME),
                reply_markup=InlineKeyboardMarkup(out),
            )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.mention
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} 𝐉𝐮𝐬𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭.\n\n**𝐔𝐬𝐞𝐫 𝐈𝐝:** {sender_id}\n**𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:** {sender_name}",
            )


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.group
    & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    OWNER = OWNER_ID[0]
    out = start_pannel(_, app.username, OWNER)
    return await message.reply_photo(
               photo=config.START_IMG_URL,
               caption=_["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**Private Music Bot**\n\nOnly for authorized chats from the owner. Ask my owner to allow your chat first."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                out = start_pannel(_)
                await message.reply_text(
                    _["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return



# Powered By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Updates
# Join @AdityaCheats For Hacks
# Join Our Chats @Bgt_Chat & @Adityadiscus 
