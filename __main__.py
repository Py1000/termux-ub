import os
os.system("pip install telethon")
from telethon import TelegramClient,events
from telethon.sessions import StringSession
from datetime import datetime

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
	aliveCaption = '''
        **BOT ALIVE
      Owner : [User]("tg:settings")**
       '''
	await user.send_file(id,"https://te.legra.ph/file/03c9b0143d1c222dede47.jpg",caption=aliveCaption) 

@user.on(events.NewMessage(pattern="\."))
async def addons(event):
  rawTxt = event.raw_text.split()

user.run_until_disconnected()
