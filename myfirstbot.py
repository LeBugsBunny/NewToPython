import discord
from discord.ext import commands

token = 'Njg5MzMwNDIxMDAzMDU5MjQw.XnJYSg.YUC4YmeQO76Kyvn_oxYinEF1vW8'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready...")

client.run(token)