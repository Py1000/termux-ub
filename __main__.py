import os
os.system("pip install telethon")
os.system("pip install collections")
import asyncio
from telethon import TelegramClient,events
from collections import deque
from telethon import __version__ as telever
from telethon.sessions import StringSession
from datetime import datetime
import time

e = "Lul Error"
mainCmdList = ["hi","update"]

try:
  varFile = open("/storage/emulated/0/VARS/var.txt","r")
  varFile = varFile.read()
except:
  os.mkdir("/storage/emulated/0/VARS")
  varFile = open("/storage/emulated/0/VARS/var.txt","a")
  API_ID = input("Enter API_ID: ")
  varFile.write(f"{API_ID} ")
  API_HASH = input("Enter API_HASH: ")
  varFile.write(f"{API_HASH} ")
  SESSION = input("Enter SESSION: ")
  varFile.write(f"{SESSION}")
  varFile = open("/storage/emulated/0/VARS/var.txt","r")
  varFile = varFile.read()

varFileS = varFile.split(" ")
API_ID = varFileS[0]
API_HASH = varFileS[1]
SESSION = varFileS[2]

session = str(SESSION)
 
user = TelegramClient(StringSession(session), API_ID, API_HASH)
user.start()
os.system("clear")
print("BOT STARTUP COMPLETE \nDo .hi in any chat \n《---BOT LOG---》")


async def startBot():
  await user.send_message("me","Hello!")

@user.on(events.NewMessage(pattern=".hi",outgoing=True))
async def hi(event):
  id = event.chat_id
  await event.edit("Hello there!")
  print(f"{datetime.now()} {id} used : hi")

@user.on(events.NewMessage(pattern=".update",outgoing=True))
async def update(event):
  id = event.chat_id
  await event.edit("Updating...")
  os.system("rm -rf termux-ub")
  os.system("git clone https://github.com/AOSOFJ/termux-ub")
  await event.edit("Updated!")
  print(f"{datetime.now()} {id} used : update")
  os.system("python termux-ub")

@user.on(events.NewMessage(pattern=".alive",outgoing= True))
async def alive(event):
  id = event.chat_id
  aliveCaption = f'''
  **BOT ALIVE**
 **Owner : [User]("https://google.com")**
 **Telethon : {telever}**
 **Python : 3.9**
 **BOT: 1.0**
  '''
  await user.send_file(id,"https://te.legra.ph/file/03c9b0143d1c222dede47.jpg",caption=aliveCaption)
  await event.delete()
  print(f"{datetime.now()} {id} used : alive")

@user.on(events.NewMessage(pattern=".del",outgoing="True"))
async def delit(event):
  id = event.chat_id
  try:
    toDel = await event.get_reply_message()
    await toDel.delete()
    await event.delete()
    print(f"{datetime.now()} {id} : del")
  except:
    await event.edit("**ERROR OCCURRED**")

@user.on(events.NewMessage(pattern=".lol",outgoing=True))
async def lol(event):
    await event.edit("**LOL**")
    deq = deque(list("😂🤣😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)

@user.on(events.NewMessage(pattern="\.os",outgoing=True)
async def os(event):
  try:
    txt = event.raw_text.spli(" ") 
    cmd = txt[1]
    os.system(f"{cmd}")
    await event.edit("**DONE** \n**CHECK YOUR TERMINAL**")
  except:
     await event.edit("**ERROR OCCURRED**")

user.run_until_disconnected()
