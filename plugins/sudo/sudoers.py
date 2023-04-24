from pyrogram import filters
from pyrogram.types import Message

from Bikash.config import BANNED_USERS, MONGO_DB_URI, OWNER_ID, MUSIC_BOT_NAME
from Bikash.Bgt import get_command
from Bikash import app
from Bikash.misc import SUDOERS
from Bikash.utils.database import add_sudo, remove_sudo
from Bikash.utils.decorators.language import language

# Command
ADDSUDO_COMMAND = get_command("ADDSUDO_COMMAND")
DELSUDO_COMMAND = get_command("DELSUDO_COMMAND")
SUDOUSERS_COMMAND = get_command("SUDOUSERS_COMMAND")


@app.on_message(
    filters.command(ADDSUDO_COMMAND) & filters.user(OWNER_ID)
)
@language
async def useradd(client, message: Message, _):
    if MONGO_DB_URI is None:
        return await message.reply_text(
            f"**𝐃𝐮𝐞 𝐓𝐨 {MUSIC_BOT_NAME}'𝐒 𝐏𝐫𝐢𝐯𝐚𝐜𝐲 𝐈𝐬𝐬𝐮𝐞𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐌𝐚𝐧𝐚𝐠𝐞 𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫𝐬 𝐎𝐧 {MUSIC_BOT_NAME} 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞.\n\n 𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐝𝐝 𝐘𝐨𝐮𝐫 𝐌𝐨𝐧𝐠𝐨 𝐃𝐚𝐭𝐚𝐁𝐚𝐬𝐞 𝐈𝐧 𝐕𝐚𝐫𝐬 𝐓𝐨 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐅𝐞𝐚𝐭𝐮𝐫𝐞.**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["auth_1"])
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id in SUDOERS:
            return await message.reply_text(
                _["sudo_1"].format(user.mention)
            )
        added = await add_sudo(user.id)
        if added:
            SUDOERS.add(user.id)
            await message.reply_text(_["sudo_2"].format(user.mention))
        else:
            await message.reply_text("ғᴀɪʟᴇᴅ.")
        return
    if message.reply_to_message.from_user.id in SUDOERS:
        return await message.reply_text(
            _["sudo_1"].format(
                message.reply_to_message.from_user.mention
            )
        )
    added = await add_sudo(message.reply_to_message.from_user.id)
    if added:
        SUDOERS.add(message.reply_to_message.from_user.id)
        await message.reply_text(
            _["sudo_2"].format(
                message.reply_to_message.from_user.mention
            )
        )
    else:
        await message.reply_text("𝐅𝐚𝐢𝐥𝐞𝐝.")
    return


@app.on_message(
    filters.command(DELSUDO_COMMAND) & filters.user(OWNER_ID)
)
@language
async def userdel(client, message: Message, _):
    if MONGO_DB_URI is None:
        return await message.reply_text(
            f"**𝐃𝐮𝐞 𝐓𝐨 {MUSIC_BOT_NAME}'𝐒 𝐏𝐫𝐢𝐯𝐚𝐜𝐲 𝐈𝐬𝐬𝐮𝐞𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐌𝐚𝐧𝐚𝐠𝐞 𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫𝐬 𝐎𝐧 {MUSIC_BOT_NAME} 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞.\n\n 𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐝𝐝 𝐘𝐨𝐮𝐫 𝐌𝐨𝐧𝐠𝐨 𝐃𝐚𝐭𝐚𝐁𝐚𝐬𝐞 𝐈𝐧 𝐕𝐚𝐫𝐬 𝐓𝐨 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐅𝐞𝐚𝐭𝐮𝐫𝐞.**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["auth_1"])
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id not in SUDOERS:
            return await message.reply_text(_["sudo_3"])
        removed = await remove_sudo(user.id)
        if removed:
            SUDOERS.remove(user.id)
            await message.reply_text(_["sudo_4"])
            return
        await message.reply_text(f"Something wrong happened.")
        return
    user_id = message.reply_to_message.from_user.id
    if user_id not in SUDOERS:
        return await message.reply_text(_["sudo_3"])
    removed = await remove_sudo(user_id)
    if removed:
        SUDOERS.remove(user_id)
        await message.reply_text(_["sudo_4"])
        return
    await message.reply_text(f"𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐰𝐞𝐧𝐭 𝐖𝐫𝐨𝐧𝐠.")


@app.on_message(filters.command(SUDOUSERS_COMMAND) & ~BANNED_USERS)
@language
async def sudoers_list(client, message: Message, _):
    text = _["sudo_5"]
    count = 0
    for x in OWNER_ID:
        try:
            user = await app.get_users(x)
            user = (
                user.first_name if not user.mention else user.mention
            )
            count += 1
        except Exception:
            continue
        text += f"{count}➤ {user}\n"
    smex = 0
    for user_id in SUDOERS:
        if user_id not in OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = (
                    user.first_name
                    if not user.mention
                    else user.mention
                )
                if smex == 0:
                    smex += 1
                    text += _["sudo_6"]
                count += 1
                text += f"{count}➤ {user}\n"
            except Exception:
                continue
    if not text:
        await message.reply_text(_["sudo_7"])
    else:
        await message.reply_text(text)
