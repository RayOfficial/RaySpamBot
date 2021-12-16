import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Ray, Ray2, Ray3, Ray4, Ray5 , Ray6, Ray7, Ray8, Ray9, Ray10, SUDO_USERS


@Ray.on(events.NewMessage(pattern=".uspam"))
@Ray2.on(events.NewMessage(pattern=".uspam"))
@Ray3.on(events.NewMessage(pattern=".uspam"))
@Ray4.on(events.NewMessage(pattern=".uspam"))
@Ray5.on(events.NewMessage(pattern=".uspam"))
@Ray6.on(events.NewMessage(pattern=".uspam"))
@Ray7.on(events.NewMessage(pattern=".uspam"))
@Ray8.on(events.NewMessage(pattern=".uspam"))
@Ray9.on(events.NewMessage(pattern=".uspam"))
@Ray10.on(events.NewMessage(pattern=".uspam"))
async def unlimitedspam(event):
  if event.sender_id in SUDO_USERS:
    try:
      op = event.text[7:]
      x = None
      while x == None:
        await event.client.send_message(event.chat, op)
        await asyncio.sleep(0.3)
    except Exception as e:
      await event.reply("Oops!! Something went wrong, Report In @FunTwenty4\n\n" + str(e))
