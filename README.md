# hazeBot
hazeBot is a Discord Bot for Genshin Impact players.

Invite Bot : https://bit.ly/3dlTcMv

[![GitHub license](https://img.shields.io/github/license/hazekezia/hazebot_DiscordBot?style=flat)](https://github.com/hazekezia/hazebot_DiscordBot)

## Arguments 
**Genshin Impact Wikipedia**

Commands | Description
---------- | ----------
hz.artifact `<artifacts name>` | Show artifact descriptions.
hz.nation `<nation>` | Show nations descriptions on Teyvat.
hz.weapon `<weapon name>` | Show weapon descriptions.

#### Genshin Impact Stats
Commands | Description
------------ | -------------
hz.addme `<ltoken>` `<ltuid>` `<uid>` | Add your stats using HoyoLab cookie, more information check [below.](https://github.com/hazekezia/hazebot_DiscordBot#how-to-use-addme-command)
hz.checkme | Check if your cookie is already in database.
hz.myresin | Check your resin.
hz.myrealm | Check your realm currency.
hz.claimdaily | Claim your daily reward from HoyoLab
hz.resintimer `<current resin>` `<desired resin>` | Set resin timer.

#### Misc: Autism, do not try.
Commands | Description
------------ | -------------
hz.wangy `<your waifu>` | Wangy Wangy Copypasta. If you know, you know.
hz.waifu | Random anime pictures.

## How To Use addme Command
1. Go to [hoyolab.com](https://www.hoyolab.com/genshin/)
2. Login to your account
3. Press `F12` to open Developer Tools.
4. Go to `Application`, `Cookies`, `https://www.hoyolab.com`.
5. Search for `ltoken` and `ltuid`, for `UID` you can found under your profile in-game.
6. Then use command `hz.addme <ltoken> <ltuid> <uid>`

## Requirements
- Runtime `Python 3.8.10`
- Library `Discord.py`, `pytz`, `requests`, `genshinstats`, `mysql-connector-python`

## Credits
- https://discordpy.readthedocs.io/en/latest/
- https://genshin.dev/ - for API (**api.genshin.dev**)
- https://waifu.pics/ - Waifu Pics API (**waifu.pics/docs**)
- https://github.com/thesadru/genshinstats - Grab information from HoyoLab
- Someone :sparkling_heart:
