from discord.ext import commands
from discord import utils
import discord
import asyncio

class PrivVC(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@commands.Cog.listener
	async def on_voice_state_update(self, member, before, after):
		guild = self.client.get_guild(931771066387431505)
		categ = utils.get(guild.categories, name = 'Voices')
		
		if before.channel is None and after.channel is not None:
			if after.channel.name == "Join to create VC":
				overwrites = {
					guild.default_role : discord.PermissionOverwrite(view_channel = False),
					member : discord.PermissionOverwrite(view_channel = True, speak = True, create_instant_invite =True)
				}
				priv_vc = await categ.create_voice_channel(name = f"{member.display_name}'s VC", overwrites = overwrites)




def setup(client):
	client.add_cog(PrivVC(client))
