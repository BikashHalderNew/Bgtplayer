from Bikash.core.bot import BikashBot
from Bikash.core.dir import dirr
from Bikash.core.git import git
from Bikash.core.userbot import Userbot
from Bikash.misc import dbb, heroku

from .logging import LOGGER

git()


dirr()

dbb()

heroku()

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
