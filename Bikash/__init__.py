from Bikash.core.bot import BikashBot
from Bikash.core.dir import dirr
from Bikash.core.git import git
from Bikash.core.userbot import Userbot
from Bikash.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

dbb()

heroku()

sudo()

# Clients
app = BikashBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
