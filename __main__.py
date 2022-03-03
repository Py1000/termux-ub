import os

def setup():
  os.system("pip install telethon")
  from telethon import *

setup()

API_ID = input("Enter API_ID: ")
API_HASH = input("Enter API_HASH: ")
SESSION = input("Enter SESSION: ")

try:
  user = TelegramClient(API_ID, API_HASH, SESSION)
except as e:
  print(f"Error: {e}")
