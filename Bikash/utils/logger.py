from Bikash.config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from Bikash import app
from Bikash.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Chat"
        logger_text = f""" ━━━━━━━━━━━━━━━━━━━━━━━     
**{MUSIC_BOT_NAME} Play Logger**
┏━━━━━━━━━━━━━━━━━┓
       ༺Chat Info༻
┗━━━━━━━━━━━━━━━━━┛      
┣★**Chat:** {message.chat.title} [`{message.chat.id}`]
┣★**Chat Link:** {chatusername}
┏━━━━━━━━━━━━━━━━━┓
       ༺User Info༻
┗━━━━━━━━━━━━━━━━━┛ 
┣★**User:** {message.from_user.mention}

┣★**UserName:** @{message.from_user.username}
┣★**Id:** `{message.from_user.id}`
┏━━━━━━━━━━━━━━━━━┓
       ༺Play Info༻
┗━━━━━━━━━━━━━━━━━┛ 
┣★**Search Song:** {message.text}

┣★**Stream Type:** {streamtype}
━━━━━━━━━━━━━━━━━━━━━━━"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
