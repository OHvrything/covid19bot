import discord
import time
import requests
import json
import re #계산을 위한 특수문자 제거
from discord.ext import commands
import os

client = discord.Client()

korea = "http://api.corona-19.kr/korea?serviceKey="
key = "c5aacbfc2e7a2d8fc42d098d36549164c" #API 키(https://api.corona-19.kr/ 에서 무료 발급 가능)

response = requests.get(korea + key)
text = response.text
data = json.loads(text)

@client.event
async def on_ready():
    client_id = str(client.user.id)
    print('Client ID: ' + client_id)
    print("디스코드 봇이 준비되었습니다!")
    game = discord.Game("!현황 명령어로 코로나19 현황 보기")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("")


@client.event
async def on_message(message):
    if message.content.startswith("!현황"):
        response = requests.get(korea + key)
        text = response.text
        data = json.loads(text)
        await message.channel.send(
          "=== [ " + data["updateTime"] + "상황 ] ===\n\n" + 
          "국내 확진자: " + data["TotalCase"] + "\n" + 
          "국내 완치자: " + data["TotalRecovered"] + "\n" + 
          "국내 사망자: " + data["TotalDeath"] + "\n" + 
          "국내 치료중: " + data["NowCase"] + "\n\n" +
          "==========================================="
        )
        

client.run(os.environ['token'])
