"""
MIT License

Copyright (c) 2021 hazekezia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord, asyncio, os
import json, requests
from pytz import timezone
from datetime import datetime
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='!', description="hazeBot is a Discord Bot for Genshin Impact players.")
DCTOKEN = os.getenv("DC_TOKEN")

@bot.event
async def on_ready():
    print("{} is online!".format(bot.user))

#ResinTimer.py    
@bot.command(brief="Commmand to set resin timer")
async def resin(pesan, resin1=None, resin2=None):
    if (resin1==None or resin2==None):
        await pesan.send("Masukkan resin sesuai dengan format!")
        return
    else:
        resin1 = int(resin1)
        resin2 = int(resin2)

        # Atur Jam (Hours) dan Menit (Minutes)
        TimeDate = datetime.now()
        Asia = TimeDate.astimezone(timezone("Asia/Jakarta"))

        Hours = int(Asia.strftime("%H"))
        Minutes = int(Asia.strftime("%M"))

        #Inisialisasi Waktu
        timer = 480                              #480 detik = 8 menit

        resinGap = resin2-resin1                 #Hitung resin2 dikurangi resin1
        totalMinutesResin = (timer/60)*resinGap  #Total menit yang dibutuhkan agar resin penuh
        
        timeLeftHrs = int(totalMinutesResin/60)    #Hitung jam resin
        timeLeftMin = int(totalMinutesResin%60)    #Hitung menit resin
        
        #Set Hours
        timeHrs = timeLeftHrs + Hours
        if (timeHrs >= 24):
            timeHrs = timeHrs%24
            if (timeHrs < 10):
                timeHrs = str(timeHrs)
                timeHrs = "0" + timeHrs

        #Set Minutes
        timeMin = timeLeftMin + Minutes
        if (timeMin >= 60):
            timeMin = timeMin%60
            timeHrs = int(timeHrs)+1
            if (timeMin < 10):
                timeMin = str(timeMin)
                timeMin = "0" + timeMin

        #Resin Check
        if (resin1<0 and resin2>160):
            await pesan.send("Sumpah ya. Lu mau ngetes bot gw atau gimana gan?")
            return
        elif (resin1<0 and resin2<0):
            await pesan.send("Wtf? Resin ente minus gan?")
            return
        elif (resin1<0):
            await pesan.send("Bro, tidak ada resin minus. Saya maklumin mungkin salah ketik.")
            return
        elif(resin2>160):
            await pesan.send("Buset akun sultan, resin lebih dari 160. Ampun sultan!")
            return
        elif(resin1>resin2):
            await pesan.send("Yang bener aja bro? Resinnya ngurang gitu? Format: !resin <current resin> <desired resin>")
            return
        elif(resin1==resin2):
            await pesan.send("Bro, masa resin nya sama sih?")
            return
            
        await pesan.send("{}'s resin now is **{}**. You will be reminded when the resin reaches **{}** on **{}:{} WIB** - **{} hours {} minutes**".format(pesan.author.mention, resin1, resin2, timeHrs, timeMin, timeLeftHrs, timeLeftMin))
        
        #ResinTimer.py
        while (True):
            loop = 0
            while (loop <= timer):
                await asyncio.sleep(1)
                loop += 1
            resin1 += 1
            if(resin1==resin2):
                await pesan.send("Hello {}, your resin now is **{}**. Make sure to spend it!".format(pesan.author.mention, resin1))
                break

#ResinTimerCancel.py
"""
@bot.command()
async def cancelresin(msg):
    eula.cancel()
    await msg.send("Timer resin telah dibatalkan!")
"""

#WeaponDesc.py
@bot.command(brief="Command showing weapon description")
async def weapon(pesan, weapon):
    #Colors for rarity
    Colors = {5: 0xff8000, 4: 0xa335ee, 3: 0x0070dd, 2: 0x1eff00, 1: 0xffffff}

    #Lower Case
    Weapon = weapon.lower()
    WeaponList = requests.get("https://api.genshin.dev/weapons")
    WeaponList = WeaponList.json()

    #Check Weapon Array
    for CheckList in WeaponList:
        if Weapon in CheckList:
            Weapon = CheckList
            break
    
    #Weapon Check
    WeaponListRaw = requests.get("https://api.genshin.dev/weapons/{}".format(Weapon))
    JSONWeapon = WeaponListRaw.json()

    #Initialization
    Name = JSONWeapon["name"]
    Descriptons = "".join([":star:" for i in range(0, JSONWeapon["rarity"])])
    RarityColors = Colors[JSONWeapon["rarity"]]
    
    #Print
    Show = discord.Embed(title=Name, description=Descriptons, color=RarityColors)
    Show.set_thumbnail(url="https://api.genshin.dev/weapons/{}/icon".format(Weapon))
    Show.add_field(name="Type", value=JSONWeapon["type"])
    Show.add_field(name="Base Attack", value=JSONWeapon["baseAttack"])
    Show.add_field(name="Substat", value=JSONWeapon["subStat"])
    Show.add_field(name=JSONWeapon["passiveName"], value=JSONWeapon["passiveDesc"], inline=False)
    Show.add_field(name="How to Get This Weapon", value=JSONWeapon["location"], inline=False)

    #Send
    await pesan.send(embed=Show)

#ArtifactsDesc.py
@bot.command(brief="Command showing artifacts description")
async def artifacts(pesan, artifacts):
    #Colors for rarity
    Colors = {5: 0xff8000, 4: 0xa335ee, 3: 0x0070dd, 2: 0x1eff00, 1: 0xffffff}

    #Lower Case
    Artifacts = artifacts.lower()
    ArtifactsList = requests.get("https://api.genshin.dev/artifacts")
    ArtifactsList = ArtifactsList.json()

    #Check Artifacts Array
    for CheckList in ArtifactsList:
        if Artifacts in CheckList:
            Artifacts = CheckList
            break
    
    #Artifacts Check
    ArtifactsListRaw = requests.get("https://api.genshin.dev/artifacts/{}".format(Artifacts))
    JSONArtifacts = ArtifactsListRaw.json()

    #Initialization
    Name = JSONArtifacts["name"]
    Descriptons = "Rarity Max : " + "".join([":star:" for i in range(0, JSONArtifacts["max_rarity"])])
    RarityColors = Colors[JSONArtifacts["max_rarity"]]
    
    #Print
    Show = discord.Embed(title=Name, description=Descriptons, color=RarityColors)
    Show.set_thumbnail(url="https://api.genshin.dev/artifacts/{}/flower-of-life".format(Artifacts))
    Show.add_field(name="2-Piece Bonus", value=JSONArtifacts["2-piece_bonus"], inline=False)
    Show.add_field(name="4-Piece Bonus", value=JSONArtifacts["4-piece_bonus"], inline=False)
    Show.set_footer(text="Credits https://genshin.dev/")

    #Send
    await pesan.send(embed=Show)

bot.run(DCTOKEN)