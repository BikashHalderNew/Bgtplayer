from Bikash import app
from pyrogram import Client, filters
from Bikash.config import config
from pyrogram.types import ChatMemberUpdated


# Define the group ID where you want to monitor members leaving

@app.on_chat_member_updated(filters.chat(config.LOG_GROUP_ID) & filters.left_chat_member)
def handle_left_member(client, update: ChatMemberUpdated):
    left_user = update.left_chat_member
    if left_user.is_self:
        return  # Ignore if the bot itself left the chat

    # Send a message to the group after a member leaves
    message = f"Goodbye {left_user.first_name}! We'll miss you."
    client.send_message(config.LOG_GROUP_ID, message)
