"""
SAYA BERSUMPAH,
SAYA DISURUH TEMEN SAYA BIKIN INI

I swear, I was told by my friends to do this...
"""

import io
import aiohttp
import discord, asyncio, os, requests
from discord.ext import commands
import random

class Autism(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Wangy Copypasta (NSFW)", hidden=True)
    async def wangy(self, ctx, char):
        autism_text = [f"{char} {char} {char} ❤️ ❤️ ❤️ WANGI WANGI WANGI WANGI HU HA HU HA HU HA, aaaah baunya rambut {char} wangi aku mau nyiumin aroma wanginya {char} AAAAAAAAH ~ Rambutnya.... aaah rambutnya juga pengen aku elus-elus ~~ AAAAAH {char} keluar pertama kali di anime juga manis ❤️ ❤️ ❤️ banget AAAAAAAAH {char} AAAAA LUCCUUUUUUUUUUUUUUU............{char} AAAAAAAAAAAAAAAAAAAAGH ❤️ ❤️ ❤️apa ? {char} itu gak nyata ? Cuma HALU katamu ? nggak, ngak ngak ngak ngak NGAAAAAAAAK GUA GAK PERCAYA ITU DIA NYATA NGAAAAAAAAAAAAAAAAAK PEDULI BANGSAAAAAT !! GUA GAK PEDULI SAMA KENYATAAN POKOKNYA GAK PEDULI. ❤️ ❤️ ❤️ {char} gw ...{char} di laptop ngeliatin gw, {char} .. kamu percaya sama aku ? aaaaaaaaaaah syukur {char} aku gak mau merelakan {char} aaaaaah ❤️ ❤️ ❤️ YEAAAAAAAAAAAH GUA MASIH PUNYA {char} SENDIRI PUN NGGAK SAMA AAAAAAAAAAAAAAH", f"Buruan, panggil gue SIMP, ato BAPERAN. ini MURNI PERASAAN GUE. Gue pengen genjot bareng {char}. Ini seriusan, suaranya yang imut, mukanya yang cantik, apalagi badannya yang aduhai ningkatin gairah gue buat genjot {char}. Setiap lapisan kulitnya pengen gue jilat. Saat gue mau crot, gue bakal moncrot sepenuh hati, bisa di perut, muka, badan, teteknya, sampai lubang burit pun bakal gue crot sampai puncak klimaks. Gue bakal meluk dia abis gue moncrot, lalu nanya gimana kabarnya, ngrasain enggas bareng saat telanjang. Dia bakal bilang kalau genjotan gue mantep dan nyatain perasaannya ke gue, bilang kalo dia cinta ama gue. Gue bakal bilang balik seberapa gue cinta ama dia, dan dia bakal kecup gue di pipi. Terus kita ganti pakaian dan ngabisin waktu nonton film, sambil pelukan ama makan hidangan favorit. Gue mau {char} jadi pacar, pasangan, istri, dan idup gue. Gue cinta dia dan ingin dia jadi bagian tubuh gue. Lo kira ini copypasta? Kagak cok. Gue ngetik tiap kata nyatain prasaan gue. Setiap kali elo nanya dia siapa, denger ini baik-baik : DIA ISTRI GUE. Gue sayang {char}, dan INI MURNI PIKIRAN DAN PERASAAN GUE.", f"{char} AHHH {char} WANGY WANGY WANGY.... SEPONG SEPONG SEPONG 🤤 ❤️ 💔 {char} {char} AHHH AKU CROOOTT CROOTT MONCROOTT!!! 🤤 🤤 🤤 AHHH {char} KU SAYANG KU IMUT BANGET ❤️ ❤️ MANIS BANGET ❤️ ❤️ RAMBUT NYA JUGA AHHH PENGEN AKU GOSOK GOSOK NYAMPE BISA MENGALIRKAN ARUS LISTRIK BUAT NYALAIN SATU KABUPATEN 🤤 🤤 ❤️ TATAPAN {char} BEGITU MENGGODAAAAAAA....... AHHH AKU GAK KUATTTT LAGIIIII ~ AKU RELA DIENJEK INJEK SAMA {char}, AKU RELA JILATIN KETEK NYA NYAMPE AIR LIUR KU BERCUCURAN DI SEKUJUR TUBUHNYA 🤤 🤤 🤤 AKU RELA JADI BUDAK NYA SEUMUR HIDUP DEMI {char} KU SAYANG KU ❤️ ❤️ ❤️ APA KAMU BILANG? AKU FURRY? GAK GAK GAKKKK. SINI GW TONJOK DADA LU NYAMPE KEJANG KEJANG 😡 😡 😡 YEAAHHHH {char} PUNYA KU SENDIRI, ISTRI KU, BOJO KU, AHHHHH ❤️ ❤️ ❤️ AAAAAAAHHHHHHHHHHHHHHHHHHH",f"GW BENAR-BENAR PENGEN JILATI KAKI {char}. GW PENGEN BANGET MENJILAT SETIAP BAGIAN KAKINYA SAMPAI AIR LIUR GW BERCUCURAN KAYAK AIR KERINGAT LALU NGENOD DENGANNYA SETIAP HARI SAMPAI TUBUH KITA MATI RASA YA TÜHAN. GW INGIN MEMBUAT ANAK-ANAK DENGAN {char} SEBANYAK SATU TÌM SEPAK BOLA DAN MEMBUAT SATU TIM SEPAK BOLA LAINNYA UNTUK MELAWAN ANAK-ANAK TIM SEPAK BOLA PERTAMA GW YANG GW BUAT SAMA {char}. GW PENGEN MASUK KE SETIAP LUBANG TUBUHNYA, MAU ITU LUBANG HIDUNG, LUBANG TELINGA, RONGGA MATA MAUPUN PUSAR, KECUALI PORI-PORI KULIT. KEMUDIAN GW AKAN MENJADIKANNYA MANUSIA YANG TIDAK BISA HIDUP KALO TIDAK GW KENTOG SETIAP HARI. DAN KALAU GUA DISEPONG GUA RELA KONTL GUA PUTUS.", f"watashi mencintai {char} dengan tulus dan penuh kasih sayang, watashi tidak tahan dengan hinaan kalian yg kalian berikan terhadap {char}. {char} selalu menangis dikamarnya setiap malam karena hinaan kalian. shine, shine, shine hanya kata itulah yang ada dipikiran watashi tpi watashi hanya manusia lemah yang tak berdaya jika dikroyok banyak orang. Suatu saat kemudian ada orang biadab memfitnah {char} dengan membuat video skandal lalu menyebarkannya di website pornografi. Amarah dan aura merah menyelimuti watashi tanpa disadari darah menetes dari mata watashi secepat kilat watashi menengok cermin lalu watashi melihat rambut watashi belahan menjadi putih lalu ada kagune di punggung watashi lalu sosok kaneki muncul dari dalam cermin tanpa berkata apapun dia memberikan maskernya dan langsung pergi melompati jendela. Watashi langung mencuci masker itu karena bau tengik mulut kaneki membekas di masker itu. Perut Watashi tiba tiba merasa lapar, watashi mencoba indomie buatan {char} lalu watashi muntah muntah 😖, lalu terlintas dipikiran watashi jadi berita itu benar ! ghoul memang harus memakan manusia karena watashi masih mempunya jiwa manusia akhirnya watashi memakan tangan sendiri. Meskipun tidak menghilangkan rasa lapar setidaknya ini cukup untuk berdiri lalu memangsa siapapun yang menghina istri watashi. no mercy no cry u must die, watashi tak segan segan membunuh kalian jika kalian menghina {char}."]
        acak = random.choice(autism_text)
        
        await ctx.send(acak)
        return

    @commands.command(brief="Show Random Waifu Pictures", hidden=True)
    async def waifu(self, ctx):
        pic = requests.get("https://api.waifu.pics/sfw/waifu")
        picx = pic.json()
        url_links = picx["url"]
        async with aiohttp.ClientSession() as session:
            async with session.get(url_links) as resp:
                if resp.status != 200:
                    return await ctx.send('Download failed!')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data,'waifu.png'))