import discord
from discord.ext import commands
import random
import asyncio




client = discord.Client()
bot = commands.Bot(command_prefix='>') #command_prefix='>'

@client.event
async def on_ready():
    print("-------------------")
    print("Bot online")
    print(client.user.name)
    print(client.user.id)
    print("-------------------")


@bot.command()
async def manzano(ctx):
    await ctx.send('MANZANO É OMU SEXUAL')
@bot.command()
async def gabriel(ctx):
    await ctx.send('Gabriel is very sexy')
@bot.command()
async def raider(ctx):
    await ctx.send('FreeFire')

token = open("token.txt", "r")
tokengrap = token.read()
token.close()
bot.run(tokengrap)