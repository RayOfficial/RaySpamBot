import asyncio
from .. import Ray, Ray2, Ray3, Ray4, Ray5, Ray6, Ray7, Ray8, Ray9, Ray10, SUDO_USERS
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events
import os
import random
import sys
    
@Ray.on(events.NewMessage(pattern=".leave"))
@Ray2.on(events.NewMessage(pattern=".leave"))
@Ray3.on(events.NewMessage(pattern=".leave"))
@Ray4.on(events.NewMessage(pattern=".leave"))
@Ray5.on(events.NewMessage(pattern=".leave"))
@Ray6.on(events.NewMessage(pattern=".leave"))
@Ray7.on(events.NewMessage(pattern=".leave"))
@Ray8.on(events.NewMessage(pattern=".leave"))
@Ray9.on(events.NewMessage(pattern=".leave"))
@Ray10.on(events.NewMessage(pattern=".leave"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SUDO_USERS:
        ray = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = ray[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )   
