from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🤫 𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥 🤫",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="🌎 𝐆𝐥𝐨𝐛𝐚𝐥 🌏", callback_data="get_top_playlists"
            ),
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐓𝐨𝐩 10 𝐏𝐥𝐚𝐲𝐋𝐢𝐬𝐭𝐬", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="🤫 𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥 🤫", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌍 ɢʟᴏʙᴀʟ 🌏", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="𝐆𝐫𝐨𝐮𝐩's", callback_data="SERVERTOP chat"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁ 𝐁𝐚𝐜𝐤 ◁", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀𝐮𝐝𝐢𝐨 🔊", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="𝐕𝐢𝐝𝐞𝐨 📽️", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁ 𝐁𝐚𝐜𝐤 ◁", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐓𝐨𝐩 10 𝐏𝐥𝐚𝐲 𝐋𝐢𝐬𝐭", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="🤫 𝐏𝐞𝐫𝐬𝐨𝐧𝐚 🤫", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌏 𝐆𝐥𝐨𝐛𝐚𝐥 🌎", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="☘ 𝐆𝐫𝐨𝐮𝐩'𝐬 ☘", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="◁ 𝐁𝐚𝐜𝐤 ◁", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="◁ 𝐁𝐚𝐜𝐤 ◁",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🚫 𝐃𝐞𝐥𝐞𝐭𝐞 🚫",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="◁ 𝐁𝐚𝐜𝐤 ◁",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
