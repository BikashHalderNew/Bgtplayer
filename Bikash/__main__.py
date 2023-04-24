import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

from Bikash import config
from Bikash.config import BANNED_USERS
from Bikash import LOGGER, app, userbot
from Bikash.core.call import Bikashh
from plugins import ALL_MODULES
from Bikash.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Bikash").error(
            "No Assistant Clients Vars Defined!.. Exiting Process.."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Bikash").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("plugins" + all_module)
    LOGGER("plugins").info(
        "Successfully Imported Modules."
    )
    await userbot.start()
    await Bikashh.start()
    try:
        await Bikashh.stream_decall("https://te.legra.ph/file/f73af9a4ffe130a83d8d2.jpg")
    except:
        pass
    try:
        await Bikashh.stream_call(
            "https://te.legra.ph/file/f73af9a4ffe130a83d8d2.jpg"
        )
    except NoActiveGroupCall:
        LOGGER("Bikash").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Bikashh.decorators()
    LOGGER("Bikash").info("Bikash Player Started")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Bikash").info("Stopping Music Bot...")
