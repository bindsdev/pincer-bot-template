<h1 align="center">Pincer Discord Bot Template (Python)</h1>

> **WARNING**: Pincer is still in its alpha/planning stage, therefore it is not 100% stable. Create a bot with Pincer at your own risk.

This repository is a template for a Discord bot using the Pincer library in Python, which is meant to interact with the Discord API similar to libraries like [**nextcord.py**](https://github.com/nextcord/nextcord), [**discord.py**](https://github.com/Rapptz/discord.py) and [**disnake**](https://github.com/DisnakeDev/disnake).

## What is Pincer?
Pincer is a new Discord.py-like library for creating Discord bots in Python. It is very new, and in its alpha stage, but I believe that it is very promising and could be the future of Python Discord bots. From the [**Pincer GitHub Repository**](https://github.com/Pincer-org/Pincer), it says that it is a "snappy, asynchronous Discord API wrapper written with aiohttp". From the [**Pincer PyPi Page**](https://pypi.org/project/pincer/), it says that it is a "Discord API wrapper rebuild from scratch".

## How do I set a Discord bot up?
- Step 1: Create a Discord bot application at the [**Discord Developer Portal**](https://discord.com/developers/applications) by pressing *New Application*, and naming it.
- Step 2: Go to the *Bot* section, and build your bot.
- Step 3: Under the *token* section, you can reveal your token if you'd like, but press copy. Make sure to enable all *privileged gateway intents* which include *presence, server members, and message content intents*.
- Step 4: To invite your bot to your testing server, head to *OAuth2* -> *URL Generator*. Select *bot* in the second column, and *applications.commands* in the third column. Now copy your link, paste it into a new tab and invite the bot to the guild you want to test it in.
- Step 5: Create a *.env* file in the root of your cloned version of the GitHub repository. Inside of it, put *TOKEN=yourtoken*, as shown in the [*.env.example file*](.env.example).
- Step 6: Enter your terminal (in VSCode or PyCharm you can enter the terminal with *Ctrl+`*), and type ``python -m src.__main__``. You have successfully setup and ran your first bot! Now you can create any commands you want, and add all of your own functionality.

## Extra Links
- [**Pincer Docs**](https://docs.pincer.dev/en/latest/)
- [**Pincer Discord Server**](https://discord.gg/Txy9qFz4Gg)
