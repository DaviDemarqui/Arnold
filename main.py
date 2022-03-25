import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is on ready for use!")
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$oi'):
    await message.channel.send("VINI BO TOMA UM CAFè?")

  if msg.startswith('$robozona'):
    await message.channel.send("SOLTA AS ROBOZONAAAA!")

  if msg.startswith('$branch'):
    await message.channel.send("VINI CRIA UMA NOVA BRANCH AI")  
  
 
client.run(os.environ['TOKEN'])