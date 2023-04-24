from pyrogram import filters
from pyrogram.types import Message

from Bikash.Bgt import get_command
from Bikash import app
from Bikash.misc import SUDOERS
from Bikash.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(filters.command(ACTIVEVC_COMMAND) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text(
        "𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐀𝐜𝐭𝐢𝐯𝐞 𝐕𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭𝐬 𝐋𝐢𝐬𝐭 👉..."
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐂𝐡𝐚𝐭"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("𝐍𝐨 𝐀𝐜𝐭𝐢𝐯𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭𝐬...")
    else:
        await mystic.edit_text(
            f"**𝐀𝐜𝐭𝐢𝐯𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭𝐬:-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text(
        "𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐀𝐜𝐭𝐢𝐯𝐞 𝐕𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭𝐬 𝐋𝐢𝐬𝐭 👉..."
    )
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐂𝐡𝐚𝐭"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("𝐍𝐨 𝐀𝐜𝐭𝐢𝐯𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭𝐬...")
    else:
        await mystic.edit_text(
            f"**𝐀𝐜𝐭𝐢𝐯𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭𝐬 :-**\n\n{text}",
            disable_web_page_preview=True,
        )
