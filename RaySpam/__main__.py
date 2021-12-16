#RaySpam By @Innocent_Gaurav

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from RaySpam.utils import load_plugins
import logging
from telethon import events
from . import Ray, Ray2, Ray3, Ray4, Ray5, Ray6, Ray7, Ray8, Ray9, Ray10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "RaySpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Ray Bot Spam Successfully deployed -!")
print("Enjoy! Do visit @Funtwenty4")

if __name__ == "__main__":
    Ray.run_until_disconnected()
    
if __name__ == "__main__":
    Ray2.run_until_disconnected()

if __name__ == "__main__":
    Ray3.run_until_disconnected()
    
if __name__ == "__main__":
    Ray4.run_until_disconnected()

if __name__ == "__main__":
    Ray5.run_until_disconnected()
    
if __name__ == "__main__":
    Ray6.run_until_disconnected()
    
if __name__ == "__main__":
    Ray7.run_until_disconnected()

if __name__ == "__main__":
    Ray8.run_until_disconnected()
    
if __name__ == "__main__":
    Ray9.run_until_disconnected()

if __name__ == "__main__":
    Ray10.run_until_disconnected()    
