import discord
import re
import random
from time import localtime, strftime, sleep

client = discord.Client()
token = "NzYxODU0Njk4NzcyNzU4NTQ5.X3gqeg.Pey4W-gxZHTLSPOxZedEkH9Nq-A"

def equal_message(dm, booldm):
    return dm == booldm or dm.startswith(booldm + " ")

@client.event
async def on_ready():
    print("Discord Bot was beginning to be Running now! ")
    print("\n  Bot Info :: ")
    print("  ID : " + str(client.user.id))

@client.event
async def on_message(message):
    if message.author.bot:
        if message.author.id == client.user.id:
            return None
    elif equal_message(message.content, "!주사위"):
        dice = random.randint(1, 6)
        await message.channel.send(embed = discord.Embed(title = ":game_die: 주사위를 굴렸습니다. ", description = "결과는 **" + str(dice) + "**입니다. "))
    elif equal_message(message.content, "!날짜"):
        await message.channel.send(embed = discord.Embed(title = ":calendar: 현재 날짜는...", description = strftime("%Y년 %m월 %d일입니다. ", localtime())))
    elif equal_message(message.content, "!시간") or equal_message(message.content, "!시각"):
        if eval(strftime("%H", localtime())) > 12:
            nowhour = "오후 " + str(eval(strftime("%H", localtime())) - 12)
        elif eval(strftime("%H", localtime())) != 0:
            nowhour = "오전 12시"
        else:
            nowhour = "오전 " + strftime("%H", localtime())
        await message.channel.send(embed = discord.Embed(title = ":clock4: 현재 시간은...", description = nowhour + strftime("시 %M분입니다. ", localtime())))
    elif equal_message(message.content, "!채광") or equal_message(message.content, "!채굴") or equal_message(message.content, "!광질") or equal_message(message.content, "!광석"):
        miningloot = random.randint(1, 100)
        if miningloot <= 50:
            displayminingloot = "돌"
        if miningloot > 50 and miningloot <= 70:
            displayminingloot = "석탄"
        if miningloot > 70 and miningloot <= 80:
            displayminingloot = "철광석"
        if miningloot > 80 and miningloot <= 90:
            displayminingloot = "구리"
        if miningloot > 90 and miningloot <= 93:
            displayminingloot = "루비"
        if miningloot > 93 and miningloot <= 96:
            displayminingloot = "사파이어"
        if miningloot > 96 and miningloot <= 99:
            displayminingloot = "에메랄드"
        if miningloot == 100:
            displayminingloot = "다이아몬드"
        await message.channel.send(embed = discord.Embed(title = ":pick: 광석을 채굴했습니다! ", description = displayminingloot + "을(를) 채굴했습니다. "))
    elif equal_message(message.content, "!정보"):
        userinfo = open(str(message.author.id) + ".txt", "w")
        userinfo.close()
        userinfo = open(str(message.author.id) + ".txt", "r")
        if userinfo.read() == "":
            userinfo.close()
            userinfo = open(str(message.author.id) + ".txt", "w")
            userinfo.write("# money\n1000\n# level\n1\n# equipped_weapon\n\"시작의 검\"\n# equipped_tool\n\"시작의 곡괭이\"\n# equipped_armor\n\"NOT EQUIPPED\"")
        userinfo.close()
        userinfo = open(str(message.author.id) + ".txt", "r")
        displayuserinfo = userinfo.read().split("\n")
        money = eval(displayuserinfo[1])
        level = eval(displayuserinfo[3])
        equipped_weaopn = eval(displayuserinfo[5])
        equipped_tool = eval(displayuserinfo[7])
        equipped_armor = eval(displayuserinfo[9])
        await message.channel.send(embed = discord.Embed(title = ":pushpin: 내 정보와 현재 상태를 표시합니다. ", description = message.author.display_name + "\n\n:moneybag: 소지금 : **" + str(money) + "**\n:star: 레벨 : **Lv." + str(level) +"**\n\n**ㆍ장비 슬롯**\n:dagger: 무기 슬롯 : **" + str(equipped_weaopn) + "**\n:pick: 도구 슬롯 : **" + str(equipped_tool) + "**\n:shield: 방어구 슬롯 : **" + str(equipped_armor) + "**"))
        userinfo.close()
    elif equal_message(message.content, "!moneyadd") and len(message.content) > 9:
        if message.author.id == 705638878698012743:
            userinfo = open(str(message.author.id) + ".txt", "w")
            userinfo.close()
            userinfo = open(str(message.author.id) + ".txt", "r")
            if userinfo.read() == "":
                userinfo.close()
                userinfo = open(str(message.author.id) + ".txt", "w")
                userinfo.write("# money\n1000\n# level\n1\n# equipped_weapon\n\"시작의 검\"\n# equipped_tool\n\"시작의 곡괭이\"\n# equipped_armor\n\"NOT EQUIPPED\"")
            userinfo.close()
            userinfo = open(str(message.author.id) + ".txt", "w")
            displayuserinfo = open(str(message.author.id) + ".txt", "w").read().split("\n")[0]
            displayuserinfo.append(str(eval(open(str(message.author.id) + ".txt", "w").read().split("\n")[1]) + 1))
            displayuserinfo.append(open(str(message.author.id) + ".txt", "w").read().split("\n")[2:])
            userinfo.writelines()
            await message.channel.send(embed = discord.Embed(title = ""))
        else:
            await message.channel.send(embed = discord.Embed(title = ":x: Permission Error", description = "You're just Human, you can't to be God or Godness"))
    elif message.content.startswith("!"):
        await message.channel.send(embed = discord.Embed(title = ":x: Command Error", description = "Invalid bot Command"))
    else:
        print(strftime("[%H:%M:%S]", localtime()) + message.author.name + " sent message in #" + str(message.channel.id) + ". ")

client.run(token)
