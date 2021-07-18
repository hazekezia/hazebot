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
    Show.set_footer(text="Credits https://genshin.dev/)

    #Send
    await pesan.send(embed=Show)
"""