from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bikash import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="❰𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒❱",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠⚙", callback_data="settings_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❰𝙂𝙧𝙤𝙪𝙥❱", url=config.SUPPORT_GROUP
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="❰✚ 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 ✚❱",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=""❰𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎❱", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❰𝙂𝙧𝙤𝙪𝙥❱", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="❰𝙊𝙬𝙣𝙚𝙧❱", user_id=OWNER
            )
        ]
     ]
    return buttons
