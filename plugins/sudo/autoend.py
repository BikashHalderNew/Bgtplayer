from pyrogram import filters

from Bikash import config
from Bikash.Bgt import get_command
from Bikash import app
from Bikash.misc import SUDOERS
from Bikash.utils.database import autoend_off, autoend_on
from Bikash.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**𝐔𝐬𝐚𝐠𝐞 👇:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "🥀 𝐀𝐮𝐭𝐨 𝐄𝐧𝐝 𝐒𝐭𝐫𝐞𝐚𝐦 𝐄𝐧𝐚𝐛𝐥𝐞𝐝.\n\n𝐁𝐠𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐖𝐢𝐥𝐥 𝐋𝐞𝐚𝐯𝐞 𝐕𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭 𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜𝐥𝐥𝐲  𝐀𝐟𝐭𝐞𝐫 3 𝐌𝐢𝐧𝐬 𝐈𝐬 𝐋𝐢𝐬𝐭𝐞𝐧𝐢𝐧𝐠 𝐖𝐢𝐭𝐡 𝐀 𝐖𝐚𝐫𝐧𝐢𝐧𝐠 𝐌𝐞𝐬𝐬𝐚𝐠𝐞"
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("🥀 𝐀𝐮𝐭𝐨 𝐒𝐭𝐫𝐞𝐚𝐦 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 ✅")
    else:
        await message.reply_text(usage)
