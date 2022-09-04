import discord
from discord import Option
from discord.ext import commands
from discord.ext.commands import MissingPermissions

class MemberModeration(discord.Cog):

    def __init__(self, client):
        self.client = client

    @discord.slash_command(guild_ids=[862944848919003156], name='kick', description='Kicks a member')
    @commands.has_permissions(kick_members = True, administrator = True)
    async def kick(self, ctx, member: Option(discord.Member, description = "Whom do you want to kick?"), reason: Option(str, description = "Why?", required=False)):
        if member.id == ctx.author.id:
            await ctx.respond("I am pretty sure, you do not want to kick yourself.", ephemeral = True)
        elif member.guild_permissions.administrator:
            await ctx.respond("You cannot kick an administrator!", ephemeral= True)
        else:
            if reason == None:
                reason = f'None, provided by {ctx.author}'
            await member.kick(reason = reason)
            await ctx.respond(f"<@{ctx.author.id}>, <@{member.id}> has been kicked sucessfully from this server!\nReason: {reason}")
    
    @kick.error
    async def kickerror(ctx, error):
        if isinstance(error,MissingPermissions):
            await ctx.respond("You do not have appropriate permissions to kick a member!")
        else:
            await ctx.respond("something went wrong...")
            raise error


def setup(client):
    client.add_cog(MemberModeration(client))
