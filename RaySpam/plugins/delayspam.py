async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Ray, Ray2, Ray3, Ray4, Ray5 , Ray6, Ray7, Ray8, Ray9, Ray10, SUDO_USERS



@Ray.on(events.NewMessage(pattern=".delayspam"))
@Ray2.on(events.NewMessage(pattern=".delayspam"))
@Ray3.on(events.NewMessage(pattern=".delayspam"))
@Ray4.on(events.NewMessage(pattern=".delayspam"))
@Ray5.on(events.NewMessage(pattern=".delayspam"))
@Ray6.on(events.NewMessage(pattern=".delayspam"))
@Ray7.on(events.NewMessage(pattern=".delayspam"))
@Ray8.on(events.NewMessage(pattern=".delayspam"))
@Ray9.on(events.NewMessage(pattern=".delayspam"))
@Ray10.on(events.NewMessage(pattern=".delayspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Ray = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Raysexy = Ray[1:]
        if len(raysexy) == 2:
            message = str(Raysexy[1])
            counter = int(Raysexy[0])
            sleeptime = float(Ray[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Raysexy[0])
            sleeptime = float(Ray[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Raysexy[0])
            sleeptime = float(Ray[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
