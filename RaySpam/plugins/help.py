from .. import Ray, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
    
HELP_PIC = "https://telegra.ph/spambot-12-16"

Ray_Help = "ð¥ RAY SPAM ð¥\n\n"
 
Ray_Help += f"__á´á´á´s á´á´ á´ÉªÊá´ÊÊá´ ÉªÉ´ ÊÉªá´¢á´á´Ê x sá´á´á´__\n\n"

Ray_Help += f" â§ ððð´ðð±ð¾ð ð²ð¼ð³ð â§\n\n"

Ray_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots\n\n"
 
Ray_Help += f" â§ ð»ð´ð°ðð´ ð²ð¼ð³ â§\n\n"

Ray_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
Ray_Help += f" â§ ðð¿ð°ð¼ ð²ð¼ð³ð â§\n\n"

Ray_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n\n"
 
Ray_Help += f"á´ÊÉªá´á´ Êá´Êá´á´¡ Êá´á´á´á´É´ Òá´Ê á´á´Êá´ ÉªÉ´Òá´.\n\n"

Ray_Help += f"Â© @Innocent_Gaurav | @Funtwenty4\n"


@Ray.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Ray.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Ray_Help,
                                  buttons=[
        [
        Button.url("á´ÊÊ á´á´á´s", "https://telegra.ph/commandsetup-12-16")
        ],
        [
        Button.url("á´Êá´É´É´á´Ê", "https://t.me/FunTwenty4")
        ] 
        ]
        )                                                         
