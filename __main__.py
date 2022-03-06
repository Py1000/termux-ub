import os
os.system("pip install telethon")
import asyncio
from telethon import TelegramClient,events
from termuxPlug import *
from collections import deque
from telethon import __version__ as telever
from telethon.sessions import StringSession
from datetime import datetime
import time

e = "Lul Error"
mainCmdList = ["hi","update"]

def editVars():
  varFile = open("/storage/emulated/0/VARS/var.txt","a")
  API_ID = input("Enter API_ID: ")
  varFile.write(f"{API_ID} ")
  API_HASH = input("Enter API_HASH: ")
  varFile.write(f"{API_HASH} ")
  SESSION = input("Enter SESSION: ")
  varFile.write(f"{SESSION}")
  varFile = open("/storage/emulated/0/VARS/var.txt","r")
  varFile = varFile.read()

def editConfig():
  conFile = open("/storage/emulated/0/CONFIG/config.txt", "w")
  conFileALIVE_TXT = open("/storage/emulated/0/CONFIG/ALIVE_TXT.txt","w")
  ALIVE_NAME = input("Enter ALIVE NAME [If you want to set this as default press enter]: ")
  ALIVE_TXT = input("Enter ALIVE TEXT [If you want to set this as default press enter]: ")
  ALIVE_PIC = input("Enter ALIVE PIC(link) [If you want to set this as default press enter]: ")
  conFile.writelines(f"{ALIVE_NAME} ")
  conFileALIVE_TXT.writelines(ALIVE_TXT)
  conFile.writelines(ALIVE_PIC)
  conFile = open("/storage/emulated/0/CONFIG/config.txt", "r")
  conFile = conFile.read()
  conFileALIVE_TXT = open("/storage/emulated/0/CONFIG/ALIVE_TXT.txt")
  conFileALIVE_TXT = conFileALIVE_TXT.read()

#var
try:
  varFile = open("/storage/emulated/0/VARS/var.txt","r")
  varFile = varFile.read()
  ask = input("Edit vars [y/press enter]: ")
  ask = ask.lower()
  if ask == "y":
    editVars()
  else:
    pass

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

#config
try:
  conFile = open("/storage/emulated/0/CONFIG/config.txt","r")
  conFile = conFile.read()
  conFileALIVE_TXT = open("/storage/emulated/0/CONFIG/ALIVE_TXT.txt")
  conFileALIVE_TXT = conFileALIVE_TXT.read()
  ask = input("Edit config [y/press enter]: ")
  ask = ask.lower()
  if ask == "y":
    editConfig()
  else:
    pass
except:
  os.mkdir("/storage/emulated/0/CONFIG")
  conFile = open("/storage/emulated/0/CONFIG/config.txt", "w")
  conFileALIVE_TXT = open("/storage/emulated/0/CONFIG/ALIVE_TXT.txt","w")
  ALIVE_NAME = input("Enter ALIVE NAME [If you want to set this as default press enter]: ")
  ALIVE_TXT = input("Enter ALIVE TEXT [If you want to set this as default press enter]: ")
  ALIVE_PIC = input("Enter ALIVE PIC(link) [If you want to set this as default press enter]: ")
  conFile.writelines(f"{ALIVE_NAME} ")
  conFileALIVE_TXT.writelines(ALIVE_TXT)
  conFile.writelines(ALIVE_PIC)
  conFile = open("/storage/emulated/0/CONFIG/config.txt", "r")
  conFile = conFile.read()
  conFileALIVE_TXT = open("/storage/emulated/0/CONFIG/ALIVE_TXT.txt")
  conFileALIVE_TXT = conFileALIVE_TXT.read()


varFileS = varFile.split(" ")
API_ID = varFileS[0]
API_HASH = varFileS[1]
SESSION = varFileS[2]
session = str(SESSION)

conFileS = conFile.split(" ")
ALIVE_NAME = conFileS[0]
ALIVE_TXT = conFileALIVE_TXT
ALIVE_PIC = conFileS[1]
print(ALIVE_PIC)

user = TelegramClient(StringSession(session), API_ID, API_HASH)
user.start()
os.system("clear")
print("BOT STARTUP COMPLETE \nDo .hi in any chat \n《---BOT LOG---》")


async def startBot():
  await user.send_message("me","Hello!")

@user.on(events.NewMessage(pattern=".hi",outgoing=True))
async def _hi(event):
  await hi(event)
#  id = event.chat_id
#  await event.edit("Hello there!")
#  print(f"{datetime.now()} {id} used : hi")

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
  **{ALIVE_TXT}**
 **Owner : [{ALIVE_NAME}](https://google.com)**
 **Telethon : {telever}**
 **Python : 3.9**
 **BOT: 1.0**
  '''
  await user.send_file(id,ALIVE_PIC,caption=aliveCaption)
  await event.delete()
  print(f"User Link : {userLink}")
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
    print(f"{datetime.now()} id used : lol")
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)

@user.on(events.NewMessage(pattern="\.os",outgoing=True))
async def telOs(event):
  try:
    txt = event.raw_text.spli(" ") 
    cmd = txt[1]
    os.system(f"{cmd}")
    await event.edit("**DONE** \n**CHECK YOUR TERMINAL**")
  except:
     await event.edit("**ERROR OCCURRED**")

user.run_until_disconnected()
