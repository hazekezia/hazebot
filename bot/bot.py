import discord
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix='!', description="Bot Resin")
dctoken = os.getenv("DC_TOKEN")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def resin(pesan, resin1:int, resin2:int):
    #Inisialisasi Waktu
    timer=60                          #480 detik = 8 menit
    minutes=(timer/60)                  #8 menit
    
    resingap=resin2-resin1              #Hitung resin2 dikurangi resin1
    totalminutesresin=minutes*resingap  #Total menit yang dibutuhkan agar resin penuh
    
    timelefthrs=totalminutesresin/60    #Hitung jam resin
    timeleftmin=totalminutesresin%60    #Hitung menit resin
        
    await pesan.send("Resin {} sebanyak {}. Akan diingatkan saat resin mencapai {}. (**Time: {} hours {} minutes**).".format(pesan.author.mention, resin1,resin2, int (timelefthrs), int(timeleftmin)))
    
    while (True):
        await asyncio.sleep(timer)
        resin1=resin1+timer
        if(resin1==resin2):
            await pesan.send("Halo {}, resin kamu menjadi {}.".format(pesan.author.mention, resin1))
            break

bot.run(dctoken)