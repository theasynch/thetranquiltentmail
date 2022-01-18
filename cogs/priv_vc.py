from discord.ext import commands
from discord import utils
import discord
import asyncio

class PrivVC(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@commands.Cog.listener
	async def on_ready(self, client):
		guild = self.client.get_guild(931771066387431505)
		prim_vc = discord.utils.get(client.guild.voice_channels, name='CreateVC')
		members = prim_vc.members
		if not members:
			pass
		if members:
			priv_vc = utils.get



def setup(client):
	client.add_cog(PrivVC(client))
