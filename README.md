# hazeBot
hazeBot is a Discord Bot for Genshin Impact players.

Invite Bot : **Work in Progress (WIP)**

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
hz.addme `<ltoken>` `<ltuid>` `<uid>` | Add your stats using HoyoLab cookie, more information check [below.](https://github.com/hazekezia/hazebot_DiscordBot#how-can-i-get-my-cookies)
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

## How can I get my cookies?
1. go to [hoyolab.com](https://www.hoyolab.com/genshin/)
2. login to your account
3. press `F12` to open inspect mode (aka Developer Tools)
4. go to `Application`, `Cookies`, `https://www.hoyolab.com`.
5. copy `ltuid` and `ltoken`
6. use `set_cookie(ltuid=..., ltoken=...)` in your code

## Requirements
- Runtime `Python 3.8.10`
- Library `Discord.py`, `pytz`, `requests`, `genshinstats`, `mysql-connector-python`

## Credits
- https://discordpy.readthedocs.io/en/latest/
- https://genshin.dev/ - for API (**api.genshin.dev**)
- https://waifu.pics/ - Waifu Pics API (**waifu.pics/docs**)
- https://github.com/thesadru/genshinstats - Grab information from HoyoLab
- Someone :sparkling_heart:
