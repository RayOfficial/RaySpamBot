
import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Ray, Ray2, Ray3, Ray4, Ray5 , Ray6, Ray7, Ray8, Ray9, Ray10, SUDO_USERS
from resources.data import RAID, REPLYRAID, Ray

que = {}

@Ray.on(events.NewMessage(pattern=r"\.raid"))
@Ray2.on(events.NewMessage(pattern=r"\.raid"))
@Ray3.on(events.NewMessage(pattern=r"\.raid"))
@Ray4.on(events.NewMessage(pattern=r"\.raid"))
@Ray5.on(events.NewMessage(pattern=r"\.raid"))
@Ray6.on(events.NewMessage(pattern=r"\.raid"))
@Ray7.on(events.NewMessage(pattern=r"\.raid"))
@Ray8.on(events.NewMessage(pattern=r"\.raid"))
@Ray9.on(events.NewMessage(pattern=r"\.raid"))
@Ray10.on(events.NewMessage(pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Ray = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Ray) == 2:
            user = str(Ray[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in Ray:
                text = f"I can't raid on @Funtwenty4's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Ray[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in Ray:
                text = f"I can't raid on @Funtwenty4's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(Ray[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@Ray.on(events.NewMessage(incoming=True))
@Ray2.on(events.NewMessage(incoming=True))
@Ray3.on(events.NewMessage(incoming=True))
@Ray4.on(events.NewMessage(incoming=True))
@Ray5.on(events.NewMessage(incoming=True))
@Ray6.on(events.NewMessage(incoming=True))
@Ray7.on(events.NewMessage(incoming=True))
@Ray8.on(events.NewMessage(incoming=True))
@Ray9.on(events.NewMessage(incoming=True))
@Ray10.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@Ray.on(events.NewMessage(pattern=r"\.replyraid"))
@Ray2.on(events.NewMessage(pattern=r"\.replyraid"))
@Ray3.on(events.NewMessage(pattern=r"\.replyraid"))
@Ray4.on(events.NewMessage(pattern=r"\.replyraid"))
@Ray5.on(events.NewMessage(pattern=r"\.replyraid"))
@Ray6.on(events.NewMessage(pattern=r"\.replyraid"))
@Ray7.on(events.NewMessage(pattern=r"\.replyraid"))
@Ray8.on(events.NewMessage(pattern=r"\.replyraid"))
@Ray9.on(events.NewMessage(pattern=r"\.replyraid"))
@Ray10.on(events.NewMessage(pattern=r"\.replyraid"))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        Ray = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        Rayx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Ray[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in Ray:
                text = f" can't raid on @funtwenty4's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated replyraid"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in Ray:
                text = f" can't raid on @funtwenty4's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated Replyraid"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@Ray.on(events.NewMessage(pattern=r"\.dreplyraid"))
@Ray2.on(events.NewMessage(pattern=r"\.dreplyraid"))
@Ray3.on(events.NewMessage(pattern=r"\.dreplyraid"))
@Ray4.on(events.NewMessage(pattern=r"\.dreplyraid"))
@Ray5.on(events.NewMessage(pattern=r"\.dreplyraid"))
@Ray6.on(events.NewMessage(pattern=r"\.dreplyraid"))
@Ray7.on(events.NewMessage(pattern=r"\.dreplyraid"))
@Ray8.on(events.NewMessage(pattern=r"\.dreplyraid"))
@Ray9.on(events.NewMessage(pattern=r"\.dreplyraid"))
@Ray10.on(events.NewMessage(pattern=r"\.dreplyraid"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Ray = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Ray[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
