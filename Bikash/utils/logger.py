from Bikash.config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from Bikash import app
from Bikash.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐂𝐡𝐚𝐭"
        logger_text = f""" ━━━━━━━━━━━━━━━━━━━━━━━     
**{MUSIC_BOT_NAME} 𝐏𝐥𝐚𝐲 𝐋𝐨𝐠𝐠𝐞𝐫**
┏━━━━━━━━━━━━━━━━━┓
       ༺𝐂𝐡𝐚𝐭 𝐈𝐧𝐟𝐨༻
┗━━━━━━━━━━━━━━━━━┛      
┣★**𝐂𝐡𝐚𝐭:** {message.chat.title} [`{message.chat.id}`]
┣★**𝐂𝐡𝐚𝐭 𝐋𝐢𝐧𝐤:** {chatusername}
┏━━━━━━━━━━━━━━━━━┓
       ༺𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨༻
┗━━━━━━━━━━━━━━━━━┛ 
┣★**𝐔𝐬𝐞𝐫:** {message.from_user.mention}

┣★**𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞:** @{message.from_user.username}
┣★**𝐈𝐝:** `{message.from_user.id}`
┏━━━━━━━━━━━━━━━━━┓
       ༺𝐏𝐥𝐚𝐲 𝐈𝐧𝐟𝐨༻
┗━━━━━━━━━━━━━━━━━┛ 
┣★**𝐒𝐞𝐚𝐫𝐜𝐡 𝐒𝐨𝐧𝐠:** {message.text}

┣★**𝐒𝐫𝐞𝐚𝐦 𝐓𝐲𝐩𝐞:** {streamtype}
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
