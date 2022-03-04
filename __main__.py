import os
from telethon import TelegramClient,events
from telethon.sessions import StringSession

e = "Lul Error"

try:
  varFile = open("/storage/emulated/0/VARS/var.txt","r")
except:
  os.mkdir("/storage/emulated/0/VARS")
  varFile = open("/storage/emulated/0/var.txt","a")
  API_ID = input("Enter API_ID: ")
  varFile.write(API_ID)
  API_HASH = input("Enter API_HASH: ")
  varFile.write(API_HASH)
  SESSION = input("Enter SESSION: ")
  varFile.write(SESSION)
  



def setup():
  os.system("pip install telethon")
  os.system("termux-setup-storage")
  from telethon import TelegramClient 

setup()

session = str(SESSION)

user = TelegramClient(StringSession(session), API_ID, API_HASH)
user.start()
print("BOT STARTUP COMPLETE")

async def startBot():
  await user.send_message("me","Hello!")

@user.on(events.NewMessage(pattern=".hi"))
async def hi(event):
  await event.edit("Hello there!")
user.run_until_disconnected()
