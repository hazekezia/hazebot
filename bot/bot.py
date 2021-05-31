import discord
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix='!', description="Bot Resin")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
@bot.command()
async def resin(pesan, resin1:int, resin2:int):
    #Inisialisasi Waktu
    timer=30                           #480 detik = 8 menit
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
            await pesan.send("")
            loop+=1
        resin1=resin1+1
        if(resin1==resin2):
            await pesan.send("Halo {}, resin kamu menjadi {}.".format(pesan.author.mention, resin1))
            break

bot.run("ODQ3NjY1OTg2NjQzNDI3Mzg4.YLBYeA.ESV-Ks5a0g-m-ZYr3QKwardiMo8")