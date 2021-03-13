import discord, random, aiohttp, asyncio
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S
import os

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="Persona 3 FES"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("Aigis:",client.user.name,"819929289759653928:",client.user.id)

@client.command()
async def aigis(ctx):
  await ctx.message.delete()
  author = ctx.author
  cmds = discord.Embed(
    title = "Aigis - Commands", 
    description = """
**__COMMANDS__**
```
{prefix}aigis
Shows this message. 
 
{prefix}orgia
Nukes the server. 
 
{prefix}sall <message>
Spams all the channels.
 
{prefix}ccr <channel count> <channel name>
Creates channels with the given name.
 
{prefix}rank
Deletes all channels.
 
{prefix}overheat
Logs out the client.
```
**__CREDITS__**
```
asdf
```
""")
  await author.send(embed = cmds)
  

@client.command()
async def overheat(ctx):
  await ctx.message.delete()
  exit()  
  
  
  
  
  
  
  
  
  
  
  
  
client.run(os.environ['token'])
