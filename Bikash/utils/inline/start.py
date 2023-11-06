from Bikash import app

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bikash import config


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀 ❰ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 ❱ 💥",
                url=f"https://t.me/TT093Bot?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ 𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 ⚙", callback_data="settings_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💖", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💖 𝐆𝐫𝐨𝐮𝐩 💖", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            )
        ],
     ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ❰ 𝐀𝐝𝐝 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕",
                url=f"https://t.me/TT093Bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐇𝐞𝐥𝐩 💖", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 💥", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="🥀 𝐆𝐫𝐨𝐮𝐩 💥", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            )
        ],
        [
            InlineKeyboardButton(
                text="♕ 𝐎𝐰𝐧𝐞𝐫 ♕", user_id=OWNER
            )
        ]
     ]
    return buttons
