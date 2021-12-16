import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Ray, Ray2, Ray3, Ray4, Ray5, Ray6, Ray7, Ray8, Ray9, Ray10, ALIVE_PIC

RAY_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/spambot-12-16"


Ray_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Feel_love_bgms"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/FunTwenty4")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/RayOfficial/RaySpamBot")
        ]
        ]


@Ray.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RayBot = await Ray.get_me()
       bot_id = RayBot.first_name
       bot_username = RayBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRay = event.chat_id
       firstname = replied_user.user.first_name
       Raymsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**Powered By RAY OFFICIAL (https://t.me/Funtwenty4)**"
       await Ray.send_file(TheRay,
                RAY_IMG,
                caption=Raymsg, 
                buttons=Ray_Button)
                
@Ray2.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RayBot = await Ray2.get_me()
       bot_id = RayBot.first_name
       bot_username = RayBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRay = event.chat_id
       firstname = replied_user.user.first_name
       Raymsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**Powered By RAY OFFICIAL(https://t.me/FunTwenty4)**"
       await Ray2.send_file(TheRay,
                RAY_IMG,
                caption=Raymsg, 
                buttons=Ray_Button)      
 
@Ray3.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RayBot = await Ray3.get_me()
       bot_id = RayBot.first_name
       bot_username = RayBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRay = event.chat_id
       firstname = replied_user.user.first_name
       Raymsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**Powered By RAY OFFICIAL(https://t.me/Funtwenty4)**"
       await Ray3.send_file(TheRay,
                RAY_IMG,
                caption=Raymsg, 
                buttons=Ray_Button)
                
@Ray4.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RayBot = await Ray4.get_me()
       bot_id = RayBot.first_name
       bot_username = RayBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRay = event.chat_id
       firstname = replied_user.user.first_name
       Raymsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**Powered By RAY OFFICIAL(https://t.me/funtwenty4)**"
       await Ray4.send_file(TheRay,
                RAY_IMG,
                caption=Raymsg, 
                buttons=Ray_Button)  

@Ray5.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RayBot = await Ray5.get_me()
       bot_id = RayBot.first_name
       bot_username = RayBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRay = event.chat_id
       firstname = replied_user.user.first_name
       Raymsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**Powered By RAY OFFICIAL(https://t.me/funtwenty4)**"
       await Ray5.send_file(TheRay,
                RAY_IMG,
                caption=Raymsg, 
                buttons=Ray_Button)

@Ray6.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RayBot = await Ray6.get_me()
       bot_id = RayBot.first_name
       bot_username = RayBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRay = event.chat_id
       firstname = replied_user.user.first_name
       Raymsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**Powered By RAY OFFICIAL(https://t.me/funtwenty4)**"
       await Ray6.send_file(TheRay,
                RAY_IMG,
                caption=Raymsg, 
                buttons=Ray_Button)       

@Ray7.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RayBot = await Ray7.get_me()
       bot_id = RayBot.first_name
       bot_username = RayBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRay = event.chat_id 
       firstname = replied_user.user.first_name
       Raymsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**Powered By RAY OFFICIAL(https://t.me/funtwenty4)**"
       await Ray7.send_file(TheRay,
                RAY_IMG,
                caption=Raymsg, 
                buttons=Ray_Button)

@Ray8.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RayBot = await Ray8.get_me()
       bot_id = RayBot.first_name
       bot_username = RayBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRay = event.chat_id
       firstname = replied_user.user.first_name
       Raymsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**Powered By RAY OFFICIAL(https://t.me/Funtwenty4)**"
       await Ray8.send_file(TheRay,
                RAY_IMG,
                caption=Raymsg, 
                buttons=Ray_Button)
                
@Ray9.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RayBot = await Ray9.get_me()
       bot_id = RiayBot.first_name
       bot_username = RayBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRay = event.chat_id
       firstname = replied_user.user.first_name
       Raymsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**Powered By RAY OFFICIAL(https://t.me/funtwenty4)**"
       await Ray9.send_file(TheRay,
                RAY_IMG,
                caption=Raymsg, 
                buttons=Ray_Button)
                
@Ray10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RayBot = await Ray10.get_me()
       bot_id = RayBot.first_name
       bot_username = RayBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRay = event.chat_id
       firstname = replied_user.user.first_name
       Raymsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**Powered By RAY OFFICIAL(https://t.me/funtwenty4)**"
       await Ray10.send_file(TheRay,
                RAY_IMG,
                caption=Raymsg, 
                buttons=Ray_Button)                
