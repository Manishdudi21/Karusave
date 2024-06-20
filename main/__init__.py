#Join @dev_gagan

from telethon.errors import FloodWaitError
from datetime import datetime as dt, timedelta
import asyncio
import sys
from pyrogram import Client
import asyncio
import uvloop
from pyrogram.errors import FloodWait
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config
import logging, time
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

uvloop.install()
API_ID = "23449041"
API_HASH = "22263bf0807d45f0fc9bac99471fec1b"
BOT_TOKEN = "7186291829:AAGHlSx7Y-iyYP2qHVSBe9iSt003gWsuqkw"
SESSION = "BAFlzdEAaWgYUVh2wi0dyX7X_9auWw9QOtxhcdv_DwBdnhQR92pZk5pyahFv_FluiVtKz9NjzpQ65ucRZPSw44nXH1sRU8D9FiUozNGhZNgjC4ZKroLUGU7uutF10zAZjkfeixAe_Z5ikQIPA-vaSdL2IvlVX46pKG4cKnE1IXdzeWrQdwTbRumkY6il5_qK8vZ_YPhVfj4GHsZUTu6zKiRQB2d7MC_hVsIoo0ZcgdMgxMlurEFU7s7Uv02wp_UXlmI8uFjf3NF-NQCm25ueBOhZgGxTLsx1NCEmzVXIRhTxQSwrgniM_VMdEBhNz3_EOaTYK1jGd3G6w8fmJXtCt_jfjAtAAAAAGIjIX8AA"
FORCESUB = "botsecom"
AUTH = "6585878012"
OWNER_ID = "6585878012"
LOG_GROUP = "-1002002312606"
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "ggnbot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    sys.exit(1)
