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
                 text="★𝐔𝐏𝐃𝐀𝐓𝐄★", url=f"https://t.me/kittu_support"
            ),
            InlineKeyboardButton(
                text="★𝐆𝐑𝐎𝐔𝐏★", url=config.SUPPORT_GROUP
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="❰ 𝐀𝐃𝐃 𝐌𝐄 𝚰𝐍 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 ❱",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="☯︎𝐇𝐞𝐥𝐩☯︎", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                 text="★𝐔𝐏𝐃𝐀𝐓𝐄★", url=f"https://t.me/kittu_support"
            ),
            InlineKeyboardButton(
                text="★𝐆𝐑𝐎𝐔𝐏★", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="★𝐎𝐖𝐍𝐄𝐑★", user_id=OWNER
            )
        ]
     ]
    return buttons
