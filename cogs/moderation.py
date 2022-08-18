import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(guild_ids=[862944848919003156], description="Test 1")
    async def slash_test(self, ctx):
        await ctx.respond("Slash COmmand Sucessful!")



def setup(client):
	client.add_cog(Moderation(client))
