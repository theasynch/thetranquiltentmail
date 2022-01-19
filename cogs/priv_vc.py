from discord.ext import commands
from discord import utils
import discord
class PrivVC(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command()
	async def hi(self,ctx):
		await ctx.send('Hi')


	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		guild = self.client.get_guild(931771066387431505)
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
				await member.move_to(priv_vc)
				embed = discord.Embed(
					title = "New Private Voice Channel Created!",
					description = f"Hello {member.mention}! Your new Private Voice Channel has been created and you have been moved to the channel.\n Cheers!",
					color = 0x00ff00,
				)
				embed.set_footer(text = "Type '!help priv_vc' for more actions")
				embed.set_thumbnail(
					url="https://media.istockphoto.com/vectors/vinyl-record-player-in-modern-flat-style-vector-id1282459424?k=20&m=1282459424&s=612x612&w=0&h=4Xbaj5StcZESTvEG-2e7dgNQcMSlLiTHlK1zVnI4XvI=")
				await member.send(embed=embed)

def setup(client):
	client.add_cog(PrivVC(client))
