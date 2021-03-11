from discord.ext.commands import Cog
from discord.ext.commands import command

class Welcome(Cog):
    def __init__(self, client):
        client.bot = client

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("welcome")
    
    @Cog.listener()
    async def on_member_join(self, member):
        pass

    @Cog.listener
    async def on_member_leave(self, member):
        pass


def setup(client):
    client.add_cog(Welcome(client))