from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Bikash import app

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            # text=_["BACK_BUTTON"],
            text="Updates",
            url=f"https://t.me/BikashGadgetsTech",
        ),
        InlineKeyboardButton(
            text="Creator",
            url=f"t.me/BikashHalder",
        ),
        InlineKeyboardButton(
            text="Close", callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Admin",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="Auth",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="Blacklist",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Broadcast",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="Extra",
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text="Gban",
                    callback_data="help_callback hb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Ping",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="Play",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="Playlist",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Sudo",
                    callback_data="help_callback hb9",
                ),
                InlineKeyboardButton(
                    text="Start",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="VideoChats",
                    callback_data="help_callback hb10",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    # text=_["BACK_BUTTON"],
                    text="Back",
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
