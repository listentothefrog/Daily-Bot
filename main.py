import discord
import os
import requests
import json
import random
from get_news import *

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$daily-news'):
    news = get_latest_news()
    await message.channel.send(news)
  
client.run(os.getenv('DISCORD_API_KEY'))
