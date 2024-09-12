from pyrogram import Client, filters
from pyrogram.enums import ChatType,  ChatAction
from enum import Enum
from Bikash import app


# Define an enumeration for chat actions
class ChatAction(Enum):
    JOIN = "joined"
    LEAVE = "left"


@app.on_message(filters.chat_type.group)
async def handle_group_message(client, message):
    # Check if the chat type is a supergroup or group
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        # Detect user joining or leaving
        if message.new_chat_members:
            for user in message.new_chat_members:
                action = ChatAction.JOIN
                welcome_message = f"Welcome to the group, {user.mention}!"
                await message.reply(welcome_message)
        
        if message.left_chat_member:
            user = message.left_chat_member
            action = ChatAction.LEAVE
            goodbye_message = f"Goodbye, {user.mention}. We will miss you!"
            await message.reply(goodbye_message)
