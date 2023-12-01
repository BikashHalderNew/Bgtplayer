import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

from Bikash import config
from Bikash import LOGGER, app, userbot
from Bikash.core.call import Bikashh
from Bikash.misc import sudo
from plugins import ALL_MODULES
from Bikash.utils.database import get_banned_users, get_gbanned
from Bikash.config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
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
    LOGGER("plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Bikashh.start()
    await Bikashh.decorators()
    LOGGER("Bikash").info(
        "bot started"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Bikash").info("Stopping Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
