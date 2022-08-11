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

import discord, os
from discord.ext import commands, tasks

from Cringe import Autism
from GenshinWiki import GenshinWiki
from myGenshinStats import myStats

bot = commands.Bot(command_prefix="hz.", description="hazeBot is a Discord Bot for Genshin Impact players.")
DCTOKEN = os.getenv("DC_TOKEN")

@bot.event
async def on_ready():
    print("{} is online!".format(bot.user))

#Add Autism Arguments
bot.add_cog(Autism(bot))

#Add Genshinstats Arguments
bot.add_cog(myStats(bot))

#Add Genshinstats Arguments
bot.add_cog(GenshinWiki(bot))

bot.run(DCTOKEN)