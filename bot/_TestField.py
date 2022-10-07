from discord.ext import commands
import discord, requests, os
from pytz import timezone
from datetime import datetime

class TestField(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="TestField", hidden=True)
    async def testo(self, ctx):
        await ctx.message.delete()
        await ctx.send("deleted")
        return
    
    @commands.command(brief="TestField", hidden=True)
    async def blough(self, ctx):
        await ctx.send("lu gobloug")
        return
    
    @commands.command(brief="TestField", hidden=True)
    async def timenow(self, ctx):
        TimeDate = datetime.now()
        Asia = TimeDate.astimezone(timezone("Asia/Jakarta"))

        Hours = int(Asia.strftime("%H"))
        Minutes = int(Asia.strftime("%M"))

        await ctx.send("Server Time: {}:{} UTC+7".format(Hours, Minutes))
        return