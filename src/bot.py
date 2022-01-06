from pincer import Client as _Client, Intents

from os import getenv, listdir
from dotenv import load_dotenv


class Bot(_Client):
    def __init__(self):
        self.load_cogs()

        load_dotenv()
        super().__init__(token=getenv('TOKEN'), intents=Intents.all())

    def load_cogs(self):
        try:
            for filename in listdir("./src/cogs"):
                if filename.endswith(".py"):
                    self.load_cog(f"src.cogs.{filename[:-3]}")

                    print("Loaded cogs.")
        except Exception as e:
            print(f"Failed to load cogs: {e}")

    @_Client.event
    async def on_ready(self):
        print("Bot is online.")