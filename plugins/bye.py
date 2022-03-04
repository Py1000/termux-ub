from datetime import datetime
from telethon import events
@bot.on(events.NewMessage(patter="bye",outgoing=True))
async def bye(event):
  id = event.id
  await event.edit("Bye!⚡ going offline ......")
  print(f"{datetime.now()} {id} used : bye")
