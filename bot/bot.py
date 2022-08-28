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

import asyncio
import discord, os
from discord.ext import commands, tasks

from _Cringe import Autism
from _GenshinWiki import GenshinWiki
from _myGenshinStats import GenshinStats
from _TestField import TestField

from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="hz.", status=discord.Status.idle, activity = discord.Game(name="Ente kadang-kadang ente, ini beda lagi nih"), intents=intents, description="hazeBot is a Discord Bot for Genshin Impact players.")
DCTOKEN = os.getenv("DC_TOKEN")

@bot.event
async def on_ready():
    print("{} is online!".format(bot.user))
    print("=================================================")
    print('List of servers the bot is in: ')
    for guilds in bot.guilds:
        print(guilds.name)

async def main():
    async with bot:
        #Add GenshinStats Arguments
        await bot.add_cog(GenshinStats(bot))

        #Add GenshinWiki Arguments
        await bot.add_cog(GenshinWiki(bot))

        #Add Autism Arguments
        await bot.add_cog(Autism(bot))

        #Add TestField Arguments
        await bot.add_cog(TestField(bot))

        #Start bot
        await bot.start(DCTOKEN)

asyncio.run(main())