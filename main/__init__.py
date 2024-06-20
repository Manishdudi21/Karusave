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
SESSION = "BABZZiVHVbyvV3G3_62wrSp6iBD2jDByYJQEG8MoShGXVoV-NQhdApSmh29KmSLDbXqX8l1R5cbWO6u1kOX_iXH3ENRJP-DqUOzu1Kb6lZkM_58DsHA35BCK0nFXhhBXkJjpYHGmyqDSiM_LR4FeDah4ml2rO22UyZC9U8HtEjiOdc1_bN8R4AaqAuBxWFFDbobvi_QzdjADbQ_3_hNoT9RllpwhtfF1B9HzqFNvevMKIzaS6XAVdj-Zk8k7FckT2LUpov4aGLYHFUBCQ_qqNPew8o16EzU7cK0CpNLZ538EyMAvTbG6BYKQ0GxgdLGOqPv6NvUC9RSKis66Tua6mcPWAAAAAYiMhfwA"
FORCESUB = "botsecom"
AUTH = "6585878012"
MONGODB_CONNECTION_STRING = config("MONGO", default=ggn)
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
