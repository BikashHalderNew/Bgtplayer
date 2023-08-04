## Bikash Halder & Aditya Halder



from pyrogram import Client, filters
from pyrogram.types import Message
from Bikash.config import LOG_GROUP_ID
from Bikash import app


async def new_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "Bgt User"
        title = message.chat.title
        chat_id = message.chat.id
        bgt = f"🥀 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐍𝐨𝐰 𝐀𝐝𝐝𝐞𝐝 𝐀 𝐍𝐞𝐰 𝐆𝐫𝐨𝐮𝐩 🥀\n\n🥀 𝐆𝐫𝐨𝐮𝐩 𝐈𝐝 : {chat_id} 🌴\n🥀 𝐆𝐫𝐨𝐮𝐩 𝐍𝐚𝐦𝐞 : {title} 🌺\n🥀 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 : {added_by} 🌱 \n\n Powered By @BikashGadgetsTech"
        await new_message(LOG_GROUP_ID, bgt)
