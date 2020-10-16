print("준비중입니다...")
import discord
from discord.ext import commands
import os
import asyncio
client = discord.Client()

@client.event
async def on_ready():
    print("준비 완료!")
    game = discord.Game("'띵아 도움말' 명령어로 도움말 확인")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("띵아 도움말"):
        await message.channel.send("https://cdn.discordapp.com/attachments/751333105171955772/755672858918780928/fbaab007aba79536.png")
        await message.channel.send("띵이의 도움말이에요!")
        await message.channel.send("띵이와 노는 방법입니다!")
        await message.channel.send("1. 띵아 안녕")
        await message.channel.send("띵이에게 인사하세요!")
        await message.channel.send("2. 띵아 뭐해")
        await message.channel.send("띵이가 뭐하는지 물어보세요!")
        await message.channel.send("3. 띵아 넌 누구")
        await message.channel.send("띵이에 대해 소개해줘요!")
        await message.channel.send("4. 띵아 기분 어때")
        await message.channel.send("띵이의 기분을 물어보세요!")
        await message.channel.send("=======================")
        await message.channel.send("그리고 이 외에 다른 커맨드도 있어요!(예: 띵아 바보니)")

    if message.content.startswith("띵아 안녕"):
        await message.channel.send("안녕하세요! 반가워요!")

    if message.content.startswith("띵아 뭐해"):
        await message.channel.send("~~봇 속에 같여있어요!~~")

    if message.content.startswith("띵아 넌 누구"):
        await message.channel.send("태어난 날: 2020년 9월 16일")
        await message.channel.send("태어난 시간: 3시 00분")
        await message.channel.send("~~집어넣은 사람: 애브리띵~~")
        await message.channel.send("~~파이썬으로 이루어져 있다~~")

    if message.content.startswith("띵아 말해 해"):
        channel = message.content[7:26]
        msg = message.content[27:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("띵아 바보니"):
        await message.channel.send("봇은 슬퍼하지 않아!")
        await message.channel.send("라고 했지만...")
        await message.channel.send("너무 슬퍼 ㅠㅠ")

    if message.content.startswith("띵아 샌드박스"):
        await message.channel.send("띵이도 그곳에 들어가면 유명해질까요...?")

    if message.content.startswith("띵아 기분 어때"):
        msg = await message.channel.send("**봇 속에 갇혀있어서 더럽다.**")
        await asyncio.sleep(0.5)
        await msg.edit(content='앗! 기분이 너무 좋아요!;;')

    if message.content.startswith("띵아 ㅋㅋ"):
        await message.channel.send("ㅋㅋㅋ 너무 재미있어요!")
        await asyncio.sleep(1.0)
        await message.channel.send("~~그런데 뭐가 재미있는거지...?~~")


client.run(os.environ['token'])
