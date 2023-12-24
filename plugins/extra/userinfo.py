## Bikash Halder & Aditya Halder

import os
from Bikash.config import BANNED_USERS
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from Bikash import app


n = "\n"
w = " "

bold = lambda x: f"**{x}:** "
bold_ul = lambda x: f"**--{x}:**-- "
mono = lambda x: f"`{x}`{n}"


def section(title: str, body: dict, indent: int = 2, underline: bool = False) -> str:
    text = (bold_ul(title) + n) if underline else bold(title) + n
    for key, value in body.items():
        text += (indent * w + bold(key) + ((value[0] + n) if isinstance(value, list) else mono(value)))
    return text


async def get_user_info(user, already=False):
    if not already:
        user = await app.get_users(user)
    if not user.first_name:
        return ["ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("ʟɪɴᴋ")
    mlink = user.mention()
    uname = ("@" + username) if username else mlink
    dc_id = user.dc_id
    photo_id = user.photo.big_file_id if user.photo else None
    is_scam = user.is_scam
    is_restricted = user.is_restricted
    caption = f"""<b><u>Usᴇʀ Fᴜʟʟ Dᴇᴛᴀɪʟs</u> ✨</b>

<b>ɴᴀᴍᴇ:</b> {first_name}
<b>ᴜsᴇʀɴᴀᴍᴇ:</b> {uname}
<b>ᴍᴇɴᴛɪᴏɴ:</b> {mention}
<b>ᴜsᴇʀ ɪᴅ:</b> <code>{user_id}</code>
<b>ᴜsᴇʀ ᴅᴄ ɪᴅ:</b> <code>{dc_id}</code>
<b>sᴄᴀᴍ:</b> {is_scam}
<b>ʀᴇsᴛʀɪᴄᴛᴇᴅ:</b> {is_restricted}"""
    return [caption, photo_id]


async def get_chat_info(chat, already=False):
    if not already:
        chat = await app.get_chat(chat)
    chat_id = chat.id
    username = chat.username
    title = chat.title
    is_scam = chat.is_scam
    description = chat.description
    members = chat.members_count
    is_restricted = chat.is_restricted
    if username:
        link = f"@{username}"
    else:
        try:
            clink = await app.export_chat_invite_link(chat_id)
            link = f"<a href={clink}>private</a>"
        except:
            link = "ᴘʀɪᴠᴀᴛᴇ"
            pass
    photo_id = chat.photo.big_file_id if chat.photo else None
    caption = f"""<b><u>Cʜᴀᴛ Fᴜʟʟ Dᴇᴛᴀɪʟs</u> ✨</b>

<b>ɴᴀᴍᴇ:</b> {title}
<b>ᴜsᴇʀɴᴀᴍᴇ:</b> {link}
<b>ᴄʜᴀᴛ ɪᴅ:</b> <code>{chat_id}
<b>ᴍᴇᴍʙᴇʀs:</b> <code>{members}</code>
<b>sᴄᴀᴍ:</b> {is_scam}
<b>ʀᴇsᴛʀɪᴄᴛᴇᴅ:</b> {is_restricted}
<b><u>ᴅᴇsᴄʀɪᴘᴛɪᴏɴ</u>:</b>
<code>{description}</code>"""
    return [caption, photo_id]


@app.on_message(filters.command(["info", "id", "userinfo"]) & ~BANNED_USERS)
async def info_func(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    m = await message.reply_text("**𝐏ɤ๏ƈɛssɩŋʛ ✨...**")
    try:
        info_caption, photo_id = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))

    if not photo_id:
        return await m.edit(info_caption, disable_web_page_preview=True)
    photo = await app.download_media(photo_id)

    await message.reply_photo(photo=photo, caption=info_caption, quote=True, parse_mode=ParseMode.HTML)
    await m.delete()
    os.remove(photo)


@app.on_message(filters.command("chatinfo") & ~BANNED_USERS)
async def chat_info_func(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) > 2:
            return await message.reply_text("**ᴜsᴀɢᴇ:** /chat_info [username|id]")
        if len(message.command) == 1:
            chat = message.chat.id
        elif len(message.command) == 2:
            chat = message.text.split(None, 1)[1]
            
        m = await message.reply_text("**𝐏ɤ๏ƈɛssɩŋʛ ✨...**")
        info_caption, photo_id = await get_chat_info(chat)
        if not photo_id:
            return await m.edit(info_caption, disable_web_page_preview=True)

        photo = await app.download_media(photo_id)
        await message.reply_photo(photo=photo, caption=info_caption, quote=True, parse_mode=ParseMode.HTML)
        await m.delete()
        os.remove(photo)
    except Exception as e:
        await m.edit(e)
     
