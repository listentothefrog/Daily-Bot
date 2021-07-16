import discord
import os
import requests
import json
from get_news import get_latest_news
from keep_alive import keep_alive
from motivate import get_quote

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$daily-news'):
    news = get_latest_news()
    await message.channel.send(news)

keep_alive()
client.run(os.getenv('DISCORD_API_KEY'))
