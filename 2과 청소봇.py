#기본 import 
import discord
import time
import requests


client = discord.Client()


@client.event


async def on_ready():
    #봇이 준비가 되면 콘솔 창에 "ready" 가 출력 됨.
    print('ready')

@client.event
async def on_message(message):
    #시작 스위치 : !청소 라는 메시지가 보이면
    if message.content.startswith('!청소') :
        #메시지 50개를 지우고
        await message.channel.purge(limit=5000)
        #1초를 기다린다.
        time.sleep(1)
        #embed 의 색을 7a92e2 로 지정 하고
        embed = discord.Embed(colour=discord.Colour(0x7a92e2))
        #embed 글 지정 
        embed.set_footer(text="After 5 seconds this message will be cleared automatically.")
        #embed 글 지정 
        embed.add_field(name="Rampaka Python", value="50 messages have been deleted successfully.")
        #embed 를 보낸다.
        await message.channel.send(embed=embed)
        #5초를 기다리고
        time.sleep(5)
        #메시지 1개를 삭제 한다.
        await message.channel.purge(limit=1)


#구동 할 봇 토큰
client.run("NzQ2NzE0NjMzMzAxMzkzNDQ4.X0EWMQ.ffgNAooSLs-56mxTLqx8SCHmCQk")