import genshinstats as gs
import asyncio
from datetime import datetime
from pytz import timezone
from discord.ext import commands

from database import connecting_db

class GenshinStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Database add user
    @commands.command(brief="Add your HoyoLab account to database")
    async def addme(self, ctx, ltoken=None, ltuid=None, uid=None):
        if (ltoken == None or ltuid == None or uid == None):
            await ctx.send("Format: hz.addme <ltoken> <ltuid> <uid>")
            await ctx.send("How to get that : <https://github.com/hazekezia/hazebot_DiscordBot>")
            return
        else:
            db = connecting_db()
            cursor = db.cursor(buffered=True)

            profid = ctx.author.id
        
            cursor.execute("SELECT profile_id FROM user where profile_id = %s", (profid,))
            if (cursor.rowcount <= 0):
                SQLCommand = "INSERT INTO user (profile_id, server_id, ltoken, ltuid, uid) VALUES (%s, %s, %s, %s, %s)"
                Data = (ctx.author.id, ctx.guild.id, ltoken, ltuid, uid)

                print(ctx.guild.id)

                cursor.execute(SQLCommand, Data)
                db.commit()
                cursor.close()

                await ctx.message.delete()
                await ctx.send("User added! You can always delete your account using hz.deleteme command.")
                return
            elif (cursor.rowcount >= 1):
                cursor.close()
                await ctx.send("Your account is already in database!")
                return

    #Database check user
    @commands.command(brief="Check your HoyoLab account already on database")
    async def checkme(self, ctx):
        db = connecting_db()
        cursor = db.cursor(buffered=True)

        profid = ctx.author.id
        
        cursor.execute("SELECT profile_id FROM user where profile_id = %s", (profid,))
        
        if (cursor.rowcount <= 0):
            cursor.close()
            await ctx.send("User not found! Please add yourself with hz.addme command.")
            return
        elif (cursor.rowcount >= 1):
            cursor.close()
            await ctx.send("Already on database!")
            return

    #Database delete user
    @commands.command(brief="Delete your HoyoLab account on database")
    async def deleteme(self, ctx):
        db = connecting_db()
        cursor = db.cursor(buffered=True)

        profid = ctx.author.id
        
        cursor.execute("DELETE FROM user WHERE profile_id = %s", (profid,))
        db.commit()

        await ctx.send("User deleted!")
        return

    #ResinCheck
    @commands.command(brief="Show your current resin")
    async def myresin(self, ctx):
        db = connecting_db()
        cursor = db.cursor(buffered=True)
        profid = ctx.author.id

        cursor.execute("SELECT * FROM user where profile_id = %s", (profid,))
        result = cursor.fetchone()

        if (cursor.rowcount >= 1):
            LTOKEN = result[3]
            LTUID = result[4]
            LUID = result[5]

            gs.set_cookie(ltuid=LTUID, ltoken=LTOKEN)
            uid = LUID
            data_ = gs.get_notes(uid)

            record_card = gs.get_record_card(LTUID)
            nickname = record_card["nickname"]
            level = record_card["level"]

            #Calculate Resin

            ResinTimer = 8 #Minutes
            ResinNow = data_['resin']
            ResinMax = data_['max_resin']

            resinGap = ResinMax - ResinNow
            totalMinutesResin = ResinTimer*resinGap

            TimeDate = datetime.now()
            Asia = TimeDate.astimezone(timezone("Asia/Jakarta"))

            Hours = int(Asia.strftime("%H"))
            Minutes = int(Asia.strftime("%M"))

            timeLeftHrs = int(totalMinutesResin/60) 
            timeLeftMin = int(totalMinutesResin%60)

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

            # Status condition
            if (ResinNow == ResinMax):
                nextStr = "Already full, spend it already!"
            else:
                nextStr = "Full refill in **{} hours {} minutes ** at {}:{} UTC+7".format(timeLeftHrs, timeLeftMin, timeHrs, timeMin)

            await ctx.send("{} [*{}* - AR{}], your current resin: {}/{}. {}".format(ctx.author.mention, nickname, level, ResinNow, ResinMax, nextStr))
            return
        elif (cursor.rowcount <= 0):
            await ctx.send("You are not in database! Please add yourself with **hz.addme** command.")
            return
        
    #RealmCurrencyCheck
    @commands.command(brief="Show your current realm currency")
    async def myrealm(self, ctx):
        db = connecting_db()
        cursor = db.cursor(buffered=True)
        profid = ctx.author.id

        cursor.execute("SELECT * FROM user where profile_id = %s", (profid,))
        result = cursor.fetchone()

        if (cursor.rowcount >= 1):
            LTOKEN = result[3]
            LTUID = result[4]
            LUID = result[5]

            gs.set_cookie(ltuid=LTUID, ltoken=LTOKEN)
            uid = LUID
            data_ = gs.get_notes(uid)

            record_card = gs.get_record_card(LTUID)
            nickname = record_card["nickname"]
            level = record_card["level"]

            await ctx.send("Hello {}, your current realm currency: {}/{} (*{}* - AR{})".format(ctx.author.mention, data_['realm_currency'], data_['max_realm_currency'], nickname, level))
            return
        elif (cursor.rowcount <= 0):
            await ctx.send("You are not in database! Please add yourself with **hz.addme** command.")
            return
        
    #DailyClaim
    @commands.command(brief="Claim daily reward from HoyoLab")
    async def claimdaily(self, ctx):
        db = connecting_db()
        cursor = db.cursor(buffered=True)
        profid = ctx.author.id

        cursor.execute("SELECT * FROM user where profile_id = %s", (profid,))
        result = cursor.fetchone()

        if (cursor.rowcount >= 1):
            LTOKEN = result[3]
            LTUID = result[4]

            gs.set_cookie(ltuid=LTUID, ltoken=LTOKEN)
            reward = gs.claim_daily_reward()
            if reward is not None:
                await ctx.send("Claimed daily reward from HoyoLab - {}x {}".format(reward['cnt'], reward['name']))
                return
            else:
                await ctx.send("Already claimed today.")
                return
        elif (cursor.rowcount <= 0):
            await ctx.send("You are not in database! Please add yourself with **hz.addme** command.")
            return

    #ResinTimer.py    
    @commands.command(brief="Set resin timer")
    async def resintimer(self, ctx, resin1=None, resin2=None):
        if (resin1==None or resin2==None):
            await ctx.send("Masukkan resin sesuai dengan format! Type *hz.resin [current] [desired]*")
            return
        else:
            try:
                resin1 = int(resin1)
                resin2 = int(resin2)
            except ValueError:
                await ctx.send("Masukkan resin sesuai dengan format! Type *hz.resin [current] [desired]*")
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
                await ctx.send("Sumpah ya. Lu mau ngetes bot gw atau gimana gan?")
                return
            elif (resin1<0 and resin2<0):
                await ctx.send("Wtf? Resin ente minus gan?")
                return
            elif (resin1<0):
                await ctx.send("Bro, tidak ada resin minus. Saya maklumin mungkin salah ketik.")
                return
            elif(resin2>160):
                await ctx.send("Buset akun sultan, resin lebih dari 160. Ampun sultan!")
                return
            elif(resin1>resin2):
                await ctx.send("Yang bener aja bro? Resinnya ngurang gitu? Type *hz.resin [current] [desired]*")
                return
            elif(resin1==resin2):
                await ctx.send("Bro, masa resin nya sama sih?")
                return
                
            await ctx.send("{}'s resin now is **{}**. You will be reminded when the resin reaches **{}** on **{}:{} WIB** - **{} hours {} minutes**".format(ctx.author.mention, resin1, resin2, timeHrs, timeMin, timeLeftHrs, timeLeftMin))
            
            #ResinTimer.py
            while (True):
                loop = 0
                while (loop <= timer):
                    await asyncio.sleep(1)
                    loop += 1
                resin1 += 1
                if(resin1==resin2):
                    await ctx.reply("Hello {}, your resin now is **{}**. Make sure to spend it!".format(ctx.author.mention, resin1))
                    break