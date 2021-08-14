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

#NationDesc.py
@bot.command(brief="Command showing nations description on Teyvat.")
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
"""