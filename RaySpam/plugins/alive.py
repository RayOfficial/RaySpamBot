from .. import Ray, SUDO_USERS, rayversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RAY_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/spambot-12-16"
  

          
ray = "β§ πAY π πππ΄π πΌππ π΄πΏπΌππΈπΈ β§\n\n"

ray += f"ββββββββββββββββββββ\n"

ray += f"β£β£ **α΄Κα΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄** : `3.9.6`\n"

ray += f"β£β£ **α΄α΄Κα΄α΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄** : `{version.__version__}`\n"

ray += f"β£β£ **ΚΙͺα΄’α΄α΄ΚXsα΄α΄α΄ α΄ α΄ΚsΙͺα΄Ι΄**  : `{rayversion}`\n"

ray += f"ββββββββββββββββββββ\n\n"
         
                                    
@Ray.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Ray.send_file(event.chat_id,
                                  RAY_PIC,
                                  caption=ray,
                                  buttons=[
        [
        Button.url("α΄Κα΄Ι΄Ι΄α΄Κ", "https://t.me/Feel_love_bgms"),
        Button.url("sα΄α΄α΄α΄Κα΄", "https://t.me/funtwenty4")
        ],
        [
        Button.url("β’ Κα΄α΄α΄ β’", "https://github.com/RayOfficial/RaySpamBot")
        ]
        ]
        )
    
