from BgtxD import config
from config import LOG, LOG_GROUP_ID
from BgtxD import app
from BgtxD.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""
<b>BgtxD PLAY LOG<b>

<b>Chat:<b> {message.chat.title} [{message.chat.id}]
<b>User:<b> {message.from_user.mention}
<b>Username:<b> @{message.from_user.username}
<b>User ID:<b> {message.from_user.id}
<b>Chat Link:<b> {chatusername}

<b>Query:<b> {message.text}

<b>StreamType:<b> {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
