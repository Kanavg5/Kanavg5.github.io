import discord
from discord.ext import commands
import asyncio


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', intents = intents, help_command = None)

@client.event
async def on_ready():
    print('The bot is ready')

@client.command()
async def ping(ctx):
    channel = ctx.channel
    await channel.send('pong')

@client.command()
async def poll(ctx):
    channel = ctx.channel
    user = ctx.author.id



client.run('OTQyODc1MDYwMDY1MTQ0ODY0.Ygq21A.SUriCckP6O_yzHkR6-YiZlXJWsc')