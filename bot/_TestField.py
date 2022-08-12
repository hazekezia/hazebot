from discord.ext import commands

class TestField(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="TestField")
    async def testo(self, ctx):
        await ctx.message.delete()
        await ctx.send("deleted")
        return
    
    @commands.command(brief="TestField")
    async def blough(self, ctx):
        await ctx.send("lu gobloug")
        return