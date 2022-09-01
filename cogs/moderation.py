import discord

class Moderation(discord.Cog):

    def __init__(self, client):
        self.client = client

        @discord.slash_command(debug_guilds=[862944848919003156], name='bye', description='something')
        async def goodbye(self, ctx):
            await ctx.respond('Goodbye')


def setup(bot):
    bot.add_cog(Moderation(bot))
