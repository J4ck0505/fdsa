#머리

import discord, random, aiohttp, asyncio
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '?')

@client.command()
async def delchannel(ctx, channel: discord.TextChannel):
    await channel.delete()


client.run(os.environ['token'])
