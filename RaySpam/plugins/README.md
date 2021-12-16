# EXTRA PLUGINS

```python
from .. import Ray, Ray2, Ray3, Ray4, Ray5, Ray6, Ray7, Ray8, Ray9, Ray10, SUDO_USERS
from telethon import events

@Ray.on(events.NewMessage(pattern=".hi"))
@Ray2.on(events.NewMessage(pattern=".hi"))
@Ray3.on(events.NewMessage(pattern=".hi"))
@Ray4.on(events.NewMessage(pattern=".hi"))
@Ray5.on(events.NewMessage(pattern=".hi"))
@Ray6.on(events.NewMessage(pattern=".hi"))
@Ray7.on(events.NewMessage(pattern=".hi"))
@Ray8.on(events.NewMessage(pattern=".hi"))
@Ray9.on(events.NewMessage(pattern=".hi"))
@Ray10.on(events.NewMessage(pattern=".hi"))
async def hi(e):
    if e.sender_id in SUDO_USERS:
        text = "**HELLO**"
        await e.reply(text, parse_mode=None, link_preview=None )
```
