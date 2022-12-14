## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCuJ7kUnxKFFn_uR1cFbppvzkVDOyWi4ZMhdmnFh5CLxXLy-njAP4dSt2klHq18wr60wu09usEeqzPv1IGkd-_B-b4HeYXA2YgYXgKzxmw_NRKXtjMqeV_-iQ862Wc6bOWXrTPmWHFk9kNXTgSwwNGVU61e2B88VOxuIg8KL1s-4iyYDpTyuIrlOQuPJ2HkLsfatstQrdfQ9hqW28byC86rKNexk4sSaRxCi5Du06aTxhV7gIH2CjMYF5q38d-dkW-eXJ4cd2LXDhLuo6kRUW9RJpNLW5nO-Ll0ikl3zvwRrFbd5HcpMyZU2JKRSxyRn99g7a1LM5lO65NNWtf-_SQyAAAAAWAduRsA")
BOT_TOKEN = getenv("BOT_TOKEN", "5923540555:AAEgfFz7Ge0ntG2_Ihp_yMwQsDhS0z1sj68")
BOT_NAME = getenv("BOT_NAME", "Boys_club_music")
API_ID = int(getenv("API_ID", "20347323"))
API_HASH = getenv("API_HASH", "aed062680c87d6037027387fc9646723")
OWNER_NAME = getenv("OWNER_NAME", "balaji914")
OWNER_USERNAME = getenv("OWNER_USERNAME", "balaasmart")
ALIVE_NAME = getenv("ALIVE_NAME", "Zaid")
BOT_USERNAME = getenv("BOT_USERNAME", "boysclubmusic_bot")
OWNER_ID = getenv("OWNER_ID", "1669178360")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Boysclub_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5303146278").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
