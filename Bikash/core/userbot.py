import sys

from pyrogram import Client

from Bikash import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="bgtxmusic1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="bgtxmusic2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="bgtxmusic3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="bgtxmusic4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="bgtxmusic5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Gettings Assistants Info...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("BikashGadgetsTech")
                await self.one.join_chat("BikashGadgetsTech")
            except:
                pass
            assistants.append(1)
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            self.one.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 {self.one.name}"
            )
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, f"Assistant Started"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("BikashGadgetsTech")
                await self.two.join_chat("BikashGadgetsTech")
            except:
                pass
            assistants.append(2)
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            self.two.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐓𝐰𝐨 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 :**\n\n✨ 𝐈𝐝 : `{self.two.id}`\n❄ 𝐍𝐚𝐦𝐞 : {self.two.name}\n💫 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 : @{self.two.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐓𝐰𝐨 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 {self.two.name}"
            )
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("BikashGadgetsTech")
                await self.three.join_chat("BikashGadgetsTech")
            except:
                pass
            assistants.append(3)
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            self.three.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐓𝐡𝐫𝐞𝐞 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 :**\n\n✨ 𝐈𝐝 : `{self.three.id}`\n❄ 𝐍𝐚𝐦𝐞 : {self.three.name}\n💫 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 : @{self.three.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐓𝐡𝐫𝐞𝐞 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 {self.three.name}"
            )
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("BikashGadgetsTech")
                await self.four.join_chat("BikashGadgetsTech")
            except:
                pass
            assistants.append(4)
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            self.four.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐅𝐨𝐮𝐫 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 :**\n\n✨ 𝐈𝐝 : `{self.four.id}`\n❄ 𝐍𝐚𝐦𝐞 : {self.four.name}\n💫 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 : @{self.four.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐅𝐨𝐮𝐫 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 {self.four.name}"
            )
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("BikashGadgetsTech")
                await self.five.join_chat("BikashGadgetsTech")
            except:
                pass
            assistants.append(5)
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            self.five.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐅𝐢𝐯𝐞 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 :**\n\n✨ 𝐈𝐝 : `{self.five.id}`\n❄ 𝐍𝐚𝐦𝐞 : {self.five.name}\n💫 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 : @{self.five.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐅𝐢𝐯𝐞 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 {self.five.name}"
            )
