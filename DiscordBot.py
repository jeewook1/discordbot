import discord
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print('ready')
    game =  discord.Game("파밍봇")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    if message.content.startswith('/aa'):
        html = requests.get('https://www.naver.com/').text
        soup = BeautifulSoup(html, 'html.parser')

        title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

        for idx, title in enumerate(title_list, 1):
           print(idx, title.text)




client.run("NjMyNDQ1NTA2Nzg1NjQwNDQ4.XaSGNQ.bcXgqigVVFUthAmmWzTmah2xx5Q")