import random

from pyrogram.types import InlineKeyboardButton

selections = [
    "▁▄▂▇▄▅▄▅▃",
    "▁▃▇▂▅▇▄▅▃",
    "▃▁▇▂▅▃▄▃▅",
    "▃▄▂▄▇▅▃▅▁",
    "▁▃▄▂▇▃▄▅▃",
    "▃▁▄▂▅▃▇▃▅",
    "▁▇▄▂▅▄▅▃▄",
    "▁▃▅▇▂▅▄▃▇",
    "▃▅▂▅▇▁▄▃▁",
    "▇▅▂▅▃▄▃▁▃",
    "▃▇▂▅▁▅▄▃▁",
    "▅▄▇▂▅▂▄▇▁",
    "▃▅▂▅▃▇▄▅▃",
]


def stream_markup_timer(_, videoid, chat_id, played, dur):
    bar = random.choice(selections)
    buttons = [
        [
            InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/Dm0Ds_kAkaShI"),
            InlineKeyboardButton(text="❰𝙂𝙧o𝙪𝙥❱", url=f"https://t.me/international_chatting_zones"),
        ], 
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    bar = random.choice(selections)
    buttons = [
        [
            InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/Dm0Ds_kAkaShI"),
            InlineKeyboardButton(text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/international_chatting_zones"),
        ], 
    ]
    return buttons


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/Dm0Ds_kAkaShI"),
            InlineKeyboardButton(text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/international_chatting_zones"),
        ], 
    ]
    return buttons

def stream_markup(_, videoid):
    buttons = [
        [
            InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/Dm0Ds_kAkaShI"),
            InlineKeyboardButton(text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/international_chatting_zones"),
        ], 
    ]
    return buttons


def telegram_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/Dm0Ds_kAkaShI"),
            InlineKeyboardButton(text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/international_chatting_zones"),
        ], 
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/Dm0Ds_kAkaShI"),
            InlineKeyboardButton(text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/international_chatting_zones"),
        ], 
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/Dm0Ds_kAkaShI"),
            InlineKeyboardButton(text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/international_chatting_zones"),
        ], 
    ]
    return buttons


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/Dm0Ds_kAkaShI"),
            InlineKeyboardButton(text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"https://t.me/international_chatting_zones"),
        ], 
    ]
    return buttons
