import os
os.system("pip install telethon")
from telethon import TelegramClient,events
from telethon.sessions import StringSession

e = "Lul Error"

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

@user.on(events.NewMessage(pattern=".hi"))
async def hi(event):
  await event.edit("Hello there!")

@user.on(events.NewMessage(pattern=".update"))
async def update(event):
  await event.edit("Updating...")
  os.system("rm -rf termux-ub")
  os.system("git clone https://github.com/AOSOFJ/termux-ub")
  os.system("python termux-ub")
  await event.edit("Updated!")

user.run_until_disconnected()
