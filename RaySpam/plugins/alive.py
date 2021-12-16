from .. import Ray, SUDO_USERS, rayversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RAY_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/spambot-12-16"
  

          
ray = "✧ 𝑅AY 𝑋 𝑆𝑃𝐴𝑀 𝐼𝑍𝑍 𝐴𝐿𝐼𝑉𝐸𝐸 ✧\n\n"

ray += f"┏━━━━━━━━━━━━━━━━━━━\n"

ray += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

ray += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

ray += f"┣➣ **ʀɪᴢᴏᴇʟXsᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `{rayversion}`\n"

ray += f"┗━━━━━━━━━━━━━━━━━━━\n\n"
         
                                    
@Ray.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Ray.send_file(event.chat_id,
                                  RAY_PIC,
                                  caption=ray,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Feel_love_bgms"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/funtwenty4")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/RayOfficial/RaySpamBot")
        ]
        ]
        )
    
