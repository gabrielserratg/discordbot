import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print("-------------------")
    print("Bot online")
    print(client.user.name)
    print(client.user.id)
    print("-------------------")

@client.event
async def on_message(message):
    if message.content.lower().startswith('?test'):
        await client.send_message(message.channel, "Olá Mundo, estou vivo!")


token = open("token.txt", "r")
tokengrap = token.read()
token.close()
client.run(tokengrap)