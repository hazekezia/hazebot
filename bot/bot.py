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

from autism import Autism

bot = commands.Bot(command_prefix="hz.", description="hazeBot is a Discord Bot for Genshin Impact players.")
DCTOKEN = os.getenv("DC_TOKEN")

@bot.event
async def on_ready():
    print("{} is online!".format(bot.user))

#Add Autism Arguments
bot.add_cog(Autism(bot))

#ResinTimer.py    
@bot.command(brief="Commmand to set resin timer")
async def resin(pesan, resin1=None, resin2=None):
    if (resin1==None or resin2==None):
        await pesan.send("Masukkan resin sesuai dengan format! Type *hz.resin [current] [desired]*")
        return
    else:
        try:
            resin1 = int(resin1)
            resin2 = int(resin2)
        except ValueError:
            await pesan.send("Masukkan resin sesuai dengan format! Type *hz.resin [current] [desired]*")
            return

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
            await pesan.send("Yang bener aja bro? Resinnya ngurang gitu? Type *hz.resin [current] [desired]*")
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
                await pesan.reply("Hello {}, your resin now is **{}**. Make sure to spend it!".format(pesan.author.mention, resin1))
                break

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

    try:
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
        await pesan.reply(embed=Show)
        print("Send weapon description {} by {}".format(Name,pesan.author))
    except KeyError:
        await pesan.reply("Weapon not found. Please search again.")
        print("Send weapon description Not Found by {}".format(pesan.author))
        return

#ArtifactsDesc.py
@bot.command(brief="Command showing artifacts description")
async def artifact(pesan, artifacts):
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

    try:
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
        await pesan.reply(embed=Show)
        print("Send artefact description {} by {}".format(Name,pesan.author))
    except KeyError:
        await pesan.reply("Artifact not found. Please search again.")
        print("Send artefact description Not Found by {}".format(pesan.author))
        return

#NationDesc.py
@bot.command(brief="Command showing nations on Teyvat.")
async def nation(pesan, nation):
    nation = nation.lower()
    NationReq = requests.get("https://api.genshin.dev/nations/{}".format(nation))
    Nation = NationReq.json()

    if (nation=="mondstadt"):
        Description = "A city of freedom that lies in the northeast of Teyvat. From amongst mountains and wide-open plains, carefree breezes carry the scent of dandelions — a gift from the Anemo God, Barbatos — across Cider Lake to Mondstadt, which sits on an island in the middle of the lake."
        #Print
        Show = discord.Embed(title=Nation["name"], description=Description, color=0x1eff00)
        Show.set_thumbnail(url="https://api.genshin.dev/nations/{}/icon".format(nation))
        Show.add_field(name="Element", value=Nation["element"])
        Show.add_field(name="Archon", value=Nation["archon"])
        Show.add_field(name="Controlling Entity", value=Nation["controllingEntity"])
        Show.set_footer(text="Credits https://genshin.dev/")

        #Send
        await pesan.send(embed=Show)
        print("Send nation description {} by {}".format(Nation["name"],pesan.author))

    elif (nation=="liyue"):
        Description = "A bountiful harbor that lies in the east of Teyvat. Mountains stand tall and proud alongside the stone forest, that, together with the open plains and lively rivers, make up Liyue's bountiful landscape, which shows its unique beauty through each of the four seasons. Just how many gifts from the Geo God lie in wait amongst the rocks of Liyue's mountains?"
        #Print
        Show = discord.Embed(title=Nation["name"], description=Description, color=0xff8000)
        Show.set_thumbnail(url="https://api.genshin.dev/nations/{}/icon".format(nation))
        Show.add_field(name="Element", value=Nation["element"])
        Show.add_field(name="Archon", value=Nation["archon"])
        Show.add_field(name="Controlling Entity", value=Nation["controllingEntity"])
        Show.set_footer(text="Credits https://genshin.dev/")

        #Send
        await pesan.send(embed=Show)
        print("Send nation description {} by {}".format(Nation["name"],pesan.author))

    elif (nation=="inazuma"):
        Description = "An Isolated Archipelago Far East of Teyvat. Overcome endless thunderstorms and set foot on the islands of red maple and cherry blossoms. On winding shores and towering cliffs, and in forests and mountains full of secrets, witness the Eternity pursued by Her Excellency, the Almighty Narukami Ogosho."
        #Print
        Show = discord.Embed(title=Nation["name"], description=Description, color=0xa335ee)
        Show.set_thumbnail(url="https://api.genshin.dev/nations/{}/icon".format(nation))
        Show.add_field(name="Element", value=Nation["element"])
        Show.add_field(name="New Archon", value=Nation["archon"])
        Show.add_field(name="Controlling Entity", value=Nation["controllingEntity"])
        Show.set_footer(text="Credits https://genshin.dev/")

        #Send
        await pesan.send(embed=Show)
        print("Send nation description {} by {}".format(Nation["name"],pesan.author))
    
    else:
        await pesan.reply("Nation not found. Please search again.")
        print("Send nation description Not Found by {}".format(pesan.author))

bot.run(DCTOKEN)