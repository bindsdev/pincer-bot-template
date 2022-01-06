from pincer import Client, command


class Cog:
    def __init__(self, client: Client) -> None:
        self.client = client

    @command(guild="YOUR_TESTING_GUILD_ID", name='ping', description='Pong!')
    async def ping(self):
        return "pong"


setup = Cog