from MikuXMusic.core.bot import Anony
from MikuXMusic.core.dir import dirr
from MikuXMusic.core.git import git
from MikuXMusic.core.userbot import Userbot
from MikuXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
