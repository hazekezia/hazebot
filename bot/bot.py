"""
MIT License

Copyright (c) 2021 Jonathan Sitohang

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
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix='!', description="hazeBot adalah sebuah Bot Discord yang digunakan untuk menghitung resin pada game Genshin Impact.")
dctoken = os.getenv("DC_TOKEN")

@bot.event
async def on_ready():
    print("{} is online!".format(bot.user))
    
@bot.command(brief="Perintah untuk melakukan pengingat pada resin.")
async def resin(pesan, resin1:int, resin2:int):
    #Inisialisasi Waktu
    timer=480                           #480 detik = 8 menit
    minutes=(timer/60)                  #8 menit
    
    resingap=resin2-resin1              #Hitung resin2 dikurangi resin1
    totalminutesresin=minutes*resingap  #Total menit yang dibutuhkan agar resin penuh
    
    timelefthrs=totalminutesresin/60    #Hitung jam resin
    timeleftmin=totalminutesresin%60    #Hitung menit resin

    #Discord
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
        
    await pesan.send("Resin {} sebanyak {}. Akan diingatkan saat resin mencapai {}. (**Time: {} hours {} minutes**).".format(pesan.author.mention, resin1,resin2, int (timelefthrs), int (timeleftmin)))
    
    while (True):
        loop=0
        while (loop<=timer):
            await asyncio.sleep(1)
            loop+=1
        resin1+=1
        if(resin1==resin2):
            await pesan.send("Halo {}, resin kamu menjadi {}.".format(pesan.author.mention, resin1))
            break

bot.run(dctoken)
