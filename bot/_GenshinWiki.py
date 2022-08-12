import discord, requests, os
from discord.ext import commands

class GenshinWiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    #WeaponDesc.py
    @commands.command(brief="Command showing weapon description")
    async def weapon(self, pesan, weapon):
        #Colors for rarity
        Colors = {5: 0xff8000, 4: 0xa335ee, 3: 0x0070dd, 2: 0x1eff00, 1: 0xffffff}

        #Lower Case
        Weapon = weapon.lower()
        WeaponList = requests.get("https://api.genshin.dev/weapons")
        WeaponList = WeaponList.json()

        #Check Weapon Array
        for CheckList in WeaponList:
            if Weapon in CheckList:
                Weapon = CheckList
                break
        
        #Weapon Check
        WeaponListRaw = requests.get("https://api.genshin.dev/weapons/{}".format(Weapon))
        JSONWeapon = WeaponListRaw.json()

        try:
            #Initialization
            Name = JSONWeapon["name"]
            Descriptons = "".join([":star:" for i in range(0, JSONWeapon["rarity"])])
            RarityColors = Colors[JSONWeapon["rarity"]]
            
            #Print
            Show = discord.Embed(title=Name, description=Descriptons, color=RarityColors)
            Show.set_thumbnail(url="https://api.genshin.dev/weapons/{}/icon".format(Weapon))
            Show.add_field(name="Type", value=JSONWeapon["type"])
            Show.add_field(name="Base Attack", value=JSONWeapon["baseAttack"])
            Show.add_field(name="Substat", value=JSONWeapon["subStat"])
            Show.add_field(name=JSONWeapon["passiveName"], value=JSONWeapon["passiveDesc"], inline=False)
            Show.add_field(name="How to Get This Weapon", value=JSONWeapon["location"], inline=False)

            #Send
            await pesan.reply(embed=Show)
            print("Send weapon description {} by {}".format(Name,pesan.author))
        except KeyError:
            await pesan.reply("Weapon not found. Please search again.")
            print("Send weapon description Not Found by {}".format(pesan.author))
            return

    #ArtifactsDesc.py
    @commands.command(brief="Command showing artifacts description")
    async def artifact(self, pesan, artifacts):
        #Colors for rarity
        Colors = {5: 0xff8000, 4: 0xa335ee, 3: 0x0070dd, 2: 0x1eff00, 1: 0xffffff}

        #Lower Case
        Artifacts = artifacts.lower()
        ArtifactsList = requests.get("https://api.genshin.dev/artifacts")
        ArtifactsList = ArtifactsList.json()

        #Check Artifacts Array
        for CheckList in ArtifactsList:
            if Artifacts in CheckList:
                Artifacts = CheckList
                break
        
        #Artifacts Check
        ArtifactsListRaw = requests.get("https://api.genshin.dev/artifacts/{}".format(Artifacts))
        JSONArtifacts = ArtifactsListRaw.json()

        try:
            #Initialization
            Name = JSONArtifacts["name"]
            Descriptons = "Rarity Max : " + "".join([":star:" for i in range(0, JSONArtifacts["max_rarity"])])
            RarityColors = Colors[JSONArtifacts["max_rarity"]]
            
            #Print
            Show = discord.Embed(title=Name, description=Descriptons, color=RarityColors)
            Show.set_thumbnail(url="https://api.genshin.dev/artifacts/{}/flower-of-life".format(Artifacts))
            Show.add_field(name="2-Piece Bonus", value=JSONArtifacts["2-piece_bonus"], inline=False)
            Show.add_field(name="4-Piece Bonus", value=JSONArtifacts["4-piece_bonus"], inline=False)
            Show.set_footer(text="Credits https://genshin.dev/")

            #Send
            await pesan.reply(embed=Show)
            print("Send artefact description {} by {}".format(Name,pesan.author))
        except KeyError:
            await pesan.reply("Artifact not found. Please search again.")
            print("Send artefact description Not Found by {}".format(pesan.author))
            return

    #NationDesc.py
    @commands.command(brief="Command showing nations on Teyvat.")
    async def nation(self, pesan, nation):
        nation = nation.lower()
        NationReq = requests.get("https://api.genshin.dev/nations/{}".format(nation))
        Nation = NationReq.json()

        if (nation=="mondstadt"):
            Description = "A city of freedom that lies in the northeast of Teyvat. From amongst mountains and wide-open plains, carefree breezes carry the scent of dandelions — a gift from the Anemo God, Barbatos — across Cider Lake to Mondstadt, which sits on an island in the middle of the lake."
            #Print
            Show = discord.Embed(title=Nation["name"], description=Description, color=0x1eff00)
            Show.set_thumbnail(url="https://api.genshin.dev/nations/{}/icon".format(nation))
            Show.add_field(name="Element", value=Nation["element"])
            Show.add_field(name="Archon", value=Nation["archon"])
            Show.add_field(name="Controlling Entity", value=Nation["controllingEntity"])
            Show.set_footer(text="Credits https://genshin.dev/")

            #Send
            await pesan.send(embed=Show)
            print("Send nation description {} by {}".format(Nation["name"],pesan.author))

        elif (nation=="liyue"):
            Description = "A bountiful harbor that lies in the east of Teyvat. Mountains stand tall and proud alongside the stone forest, that, together with the open plains and lively rivers, make up Liyue's bountiful landscape, which shows its unique beauty through each of the four seasons. Just how many gifts from the Geo God lie in wait amongst the rocks of Liyue's mountains?"
            #Print
            Show = discord.Embed(title=Nation["name"], description=Description, color=0xff8000)
            Show.set_thumbnail(url="https://api.genshin.dev/nations/{}/icon".format(nation))
            Show.add_field(name="Element", value=Nation["element"])
            Show.add_field(name="Archon", value=Nation["archon"])
            Show.add_field(name="Controlling Entity", value=Nation["controllingEntity"])
            Show.set_footer(text="Credits https://genshin.dev/")

            #Send
            await pesan.send(embed=Show)
            print("Send nation description {} by {}".format(Nation["name"],pesan.author))

        elif (nation=="inazuma"):
            Description = "An Isolated Archipelago Far East of Teyvat. Overcome endless thunderstorms and set foot on the islands of red maple and cherry blossoms. On winding shores and towering cliffs, and in forests and mountains full of secrets, witness the Eternity pursued by Her Excellency, the Almighty Narukami Ogosho."
            #Print
            Show = discord.Embed(title=Nation["name"], description=Description, color=0xa335ee)
            Show.set_thumbnail(url="https://api.genshin.dev/nations/{}/icon".format(nation))
            Show.add_field(name="Element", value=Nation["element"])
            Show.add_field(name="New Archon", value=Nation["archon"])
            Show.add_field(name="Controlling Entity", value=Nation["controllingEntity"])
            Show.set_footer(text="Credits https://genshin.dev/")

            #Send
            await pesan.send(embed=Show)
            print("Send nation description {} by {}".format(Nation["name"],pesan.author))
        
        else:
            await pesan.reply("Nation not found. Please search again.")
            print("Send nation description Not Found by {}".format(pesan.author))