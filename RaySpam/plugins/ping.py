

from .. import Ray, Ray2, Ray3, Ray4, Ray5 , Ray6, Ray7, Ray8, Ray9, Ray10, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Ray.on(events.NewMessage(pattern=".ping"))
@Ray2.on(events.NewMessage(pattern=".ping"))
@Ray3.on(events.NewMessage(pattern=".ping"))
@Ray4.on(events.NewMessage(pattern=".ping"))
@Ray5.on(events.NewMessage(pattern=".ping"))
@Ray6.on(events.NewMessage(pattern=".ping"))
@Ray7.on(events.NewMessage(pattern=".ping"))
@Ray8.on(events.NewMessage(pattern=".ping"))
@Ray9.on(events.NewMessage(pattern=".ping"))
@Ray10.on(events.NewMessage(pattern=".ping"))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"\nϟ RAY SPAM ϟ︎ `{ms}` ᴍs")                       


# ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀
# ▒█▀▀▄ ▒█░░▒█ ░▒█░░
# ▒█▄▄█ ▒█▄▄▄█ ░▒█░░
