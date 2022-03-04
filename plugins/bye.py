from . import *
async def bye(event):
  id = event.id
  await event.edit("Bye!⚡ going offline ......")
  print(f"{datetime.now()} {id} used : bye")
