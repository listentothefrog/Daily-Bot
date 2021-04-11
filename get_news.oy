import os
import json
import requests

def get_latest_news():

  url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=17dbb3c9a5c54f8a887fe0f9aa7f23cb'
  response = requests.get(url)
  json_data = json.loads(response.text)
  news = f"{json_data['articles'][0]['title']}  Read the full article 👉  {json_data['articles'][0]['url']}"
  return news
