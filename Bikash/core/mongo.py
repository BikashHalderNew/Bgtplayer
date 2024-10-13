from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

from Bikash import config

from ..logging import LOGGER

TEMP_MONGODB = "mongodb+srv://tomavey417:5NZlsU9uAD8V9frr@cluster0.z4f5a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DB_NAME = "BgtOwner"

if config.MONGO_DB_URI is None:
    LOGGER(__name__).warning(
        "No MONGO DB URL found.. Your Bot will work on Yukki's Database"
    )
    temp_client = Client(
        "Yukki",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_[DB_NAME]
    pymongodb = _mongo_sync_[DB_NAME]
