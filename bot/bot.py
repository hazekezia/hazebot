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

import discord
import asyncio
import os
from pytz import timezone
from datetime import datetime
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='!', description="hazeBot adalah sebuah Bot Discord yang digunakan untuk menghitung resin pada game Genshin Impact.")
DCTOKEN = os.getenv("DC_TOKEN")

@bot.event
async def on_ready():
    print("{} is online!".format(bot.user))
    
@bot.command(brief="Perintah untuk melakukan pengingat pada resin.")
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
            
        await pesan.send("Resin {} sekarang adalah {}. Resin kamu akan berjumlah {} pada jam **{}:{} WIB** - **{} hours {} minutes**".format(pesan.author.mention, resin1, resin2, timeHrs, timeMin, timeLeftHrs, timeLeftMin))
        
        #ResinTimer.py
        """
        while (True):
            loop = 0
            while (loop <= timer):
                await asyncio.sleep(1)
                loop += 1
            resin1 += 1
            if(resin1==resin2):
                await pesan.send("Halo {}, resin kamu menjadi {}.".format(pesan.author.mention, resin1))
                break
        """

#ResinTimerCancel.py
"""
@bot.command()
async def cancelresin(msg):
    eula.cancel()
    await msg.send("Timer resin telah dibatalkan!")
"""

bot.run(DCTOKEN)
