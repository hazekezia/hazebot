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

"""
import discord, json, requests
from discord.ext import commands, tasks

Colors = {5: 0xff8000, 4: 0xa335ee, 3: 0x0070dd, 2: 0x1eff00, 1: 0xffffff}

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
    Show.set_footer(text="Credits https://genshin.dev/)

    #Send
    await pesan.send(embed=Show)
"""