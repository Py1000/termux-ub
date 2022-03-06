#Hi
async def hi(event):
  id = event.chat_id
  await event.edit("Hello there!")
  print(f"{datetime.now()} {id} used : hi")
