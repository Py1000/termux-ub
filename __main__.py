import os
from telethon import TelegramClient,events
from telethon.sessions import StringSession

e = "Lul Error"

def setup():
  os.system("pip install telethon")
  from telethon import TelegramClient 

setup()

API_ID = input("Enter API_ID: ")
API_HASH = input("Enter API_HASH: ")
SESSION = input("Enter SESSION: ")

session = str(SESSION)

user = TelegramClient(StringSession(session), API_ID, API_HASH)
user.start()

async def startBot():
  await user.send_message("me","Hello!")

@user.on(events.NewMessage(pattern=".hi"))
async def hi(event):
  await evemt.edit("Hello there!")
user.run_until_disconnected()
