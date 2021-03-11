from typing import Optional
from discord.ext.commands import Cog, Greedy
from discord.ext.commands import CheckFailure
from discord.ext.commands import command, has_permissions, bot_has_permissions

class Mod(Cog):
    def __init__(self, client):
        self.client = client

    @command(name="mute")
    async def kick_members(self, ctx, targets: Greedy[Member], *, reason: Optional[str] = "No reason provided."):
        if not len(targets):
            await ctx.send()

    @command(name="ban")
    async def ban_members(self, ctx, targets: Greedy[Member]):
        pass

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("mod")

def setup(client):
    client.add_cog(Mod(client))