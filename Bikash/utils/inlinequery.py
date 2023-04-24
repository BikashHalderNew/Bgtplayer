from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="⏸️ 𝐏𝐚𝐮𝐬𝐞 ⏸️",
            description=f"𝐏𝐚𝐮𝐬𝐞 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐮𝐬𝐢𝐜.",
            thumb_url="https://te.legra.ph/file/9dcb4e3f8392e4aea0292.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="⏹️ 𝐑𝐞𝐬𝐮𝐦𝐞 ⏹️",
            description=f"𝐑𝐞𝐬𝐮𝐦𝐞 𝐓𝐡𝐞 𝐏𝐚𝐮𝐬𝐞𝐝 𝐌𝐮𝐬𝐢𝐜.",
            thumb_url="https://te.legra.ph/file/78445accf6d74242d56fb.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="⏩ 𝐒𝐤𝐢𝐩 ⏩",
            description=f"𝐒𝐤𝐢𝐩 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐮𝐬𝐢𝐜 & 𝐏𝐥𝐚𝐲 𝐍𝐞𝐱𝐭 𝐌𝐮𝐬𝐢𝐜",
            thumb_url="https://te.legra.ph/file/dd8423621d77860885d70.jpg",
            input_message_content=InputTextMessageContent("/skip", "/next"),
        ),
        InlineQueryResultArticle(
            title="📴 𝐄𝐧𝐝 📴",
            description="𝐄𝐧𝐝 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜.",
            thumb_url="https://te.legra.ph/file/6f3513fabd84be1ecf423.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🔉 𝐒𝐡𝐮𝐟𝐟𝐥𝐞 🔉",
            description="𝐒𝐡𝐮𝐟𝐟𝐥𝐞 𝐓𝐡𝐞 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐌𝐮𝐢𝐜.",
            thumb_url="https://te.legra.ph/file/3810eb9a72fd36c0aed50.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🔈 𝐋𝐨𝐨𝐩 🔈",
            description="𝐋𝐨𝐨𝐩 𝐓𝐡𝐞 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜 .",
            thumb_url="https://te.legra.ph/file/d35e187e613d1b6cbfb07.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
