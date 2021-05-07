import asyncio
import discord

client = discord.Client()

token = "ODI2MTM4OTc1MTE0MTAwODU1.YGIH4A.dV5SrmwBOYBVwaKHRs27TPf2RXM"

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = "갱생서버에 강림"))
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("======================")

@client.event
async def on_message(message):
    if(message.author.bot):
        return None

    if(message.content.startswith("!안녕")):
       
        channel = message.channel
        await channel.send("반가워!")
        
    if(message.content.startswith("!명령어")):
       
        channel = message.channel
        await channel.send("!안녕: 반가워! \n!리영교: 으으.... \n !멈춰: 멈춰! \n !음: 쏘 테이스띠~")

    if(message.content.startswith("!리영교")):
       
        channel = message.channel
        await channel.send("으으...")

    if(message.content.startswith("!멈춰")):
       
        channel = message.channel
        await channel.send("멈춰!")
        
    if(message.content.startswith("!음")):
       
        channel = message.channel
        await channel.send("쏘 테이스띠~")
        
    if(message.content.startswith("!연패")):
       
        channel = message.channel
        await channel.send("제발 멈춰...")
    if(message.content.startswith("!롤")):
       
        channel = message.channel
        await channel.send("숙제게임 멈춰!")
    if(message.content.startswith("!무지성")):
       
        channel = message.channel
        await channel.send("다른 뜻은 없습니다. 뇌가 비었다는거죠.")
    if(message.content.startswith("!무야호")):
       
        channel = message.channel
        await channel.send("그만큼 신이 나시다는 거지~")
    if(message.content.startswith("!군머")):
       
        channel = message.channel
        await channel.send("정인, 지호, 철하, 효민")
        

        
client.run(token)
           
