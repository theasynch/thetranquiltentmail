from discord.ext import commands
from discord import utils
import asyncio
import discord
class PrivVC(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command()
	async def hi(self,ctx):
		await ctx.send('Hi')


	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		guild = self.client.get_guild(862944848919003156)
		categ = utils.get(guild.categories, name = 'Voices')
		
		if before.channel is None and after.channel is not None:
			if after.channel.name == "Join to create VC":
				overwrites = {
					guild.default_role : discord.PermissionOverwrite(view_channel = False),
					member : discord.PermissionOverwrite(view_channel = True, speak = True, create_instant_invite =True)
				}
				priv_vc = utils.get(categ.channels, name=f"{member.display_name}'s VC")
				if not priv_vc:
					priv_vc = await categ.create_voice_channel(name = f"{member.display_name}'s VC", overwrites = overwrites)
					embed = discord.Embed(
                                            title="New Private Voice Channel Created!",
                                            description=f"Hello {member.mention}! Your new Private Voice Channel has been created and you have been moved to the channel.\n Cheers!",
                                            color=0x00ff00,
                                        )
					embed.set_footer(text="Type '!help priv_vc' for more actions")
					embed.set_thumbnail(
                                            url="https://github.com/SudhanPlayz/Discord-MusicBot/blob/master/assets/logo.gif?raw=true")
					await member.send(embed=embed)
				await member.move_to(priv_vc)

	@commands.command()
	async def invc(self, ctx, member: discord.Member = None):
		def check(reaction, user):
			return user == member and str(reaction.emoji) == '✅'
		if ctx.author.voice == True and ctx.author.VoiceState.channel == f"{ctx.author.display_name}'s VC":
			if member is None:
				await ctx.reply("Please mention a valid member to invite.")
			else:
				embed = discord.Embed(
					title = 'Private VC Invite!',
					description = f"{member.mention}, you have been invited by {ctx.author.mention} to their private VC. \nPlease react with the ✅ to join the channel.",
					color=0xfbd428
				)
				await member.send(embed=embed)
				await embed.add_reaction('✅')
				try:
					check = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
				except asyncio.TimeoutError:
					await member.send('You took too long to react. The invite has been cancelled.')
				else:
					await member.send('Invite accepted!Please refer to  below link to join the channel.')
		elif ctx.author.voice == False:
			await ctx.reply("You are not in a private VC! [Type: `!help priv_vc` for more info]")
				

def setup(client):
	client.add_cog(PrivVC(client))
