﻿
# 아람쓰#5050 또는 아람#5920 : 전체디엠봇 소스
# 영상보고 모르는점 있을시 유튜브 댓글또는 디엠주세요


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇실행이 시작되었습니다(24시간 온라인).")
    game = discord.Game('디엠봇테스트')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 546485207516184589!!:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="DM봇공지")
                        embed.add_field(name="테스트중", value=msg, inline=True)
                        embed.set_footer(text=f"https://discord.gg/uecWPY72a9")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzgzOTgxMDgwNTk5NzI0MDQy.X8ipRw.gA7eEz3Klaz6C4byXr_TeH8qjvs')
