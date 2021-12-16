from .. import Ray, Ray2, Ray3, Ray4, Ray5, Ray6, Ray7, Ray8, Ray9, Ray10, SUDO_USERS
from telethon import events
import os
import random
import sys


@Ray.on(events.NewMessage(pattern=".restart"))
@Ray2.on(events.NewMessage(pattern=".restart"))
@Ray3.on(events.NewMessage(pattern=".restart"))
@Ray4.on(events.NewMessage(pattern=".restart"))
@Ray5.on(events.NewMessage(pattern=".restart"))
@Ray6.on(events.NewMessage(pattern=".restart"))
@Ray7.on(events.NewMessage(pattern=".restart"))
@Ray8.on(events.NewMessage(pattern=".restart"))
@Ray9.on(events.NewMessage(pattern=".restart"))
@Ray10.on(events.NewMessage(pattern=".restart"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**Restarting Your RAY SPAM BOT**.. Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Ray.disconnect()
        except Exception:
            pass
        try:
            await Ray2.disconnect()
        except Exception:
            pass
        try:
            await Ray3.disconnect()
        except Exception:
            pass
        try:
            await Ray4.disconnect()
        except Exception:
            pass
        try:
            await Ray5.disconnect()
        except Exception:
            pass
        try:
            await Ray6.disconnect()
        except Exception:
            pass
        try:
            await Ray7.disconnect()
        except Exception:
            pass
        try:
            await Ray8.disconnect()
        except Exception:
            pass
        try:
            await Ray9.disconnect()
        except Exception:
            pass
        try:
            await Ray10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
