from discord.ext import commands
from discord import utils, Option
import asyncio
import discord
class PrivVC(commands.Cog):
	def __init__(self, client):
		self.client = client



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
					
					embed.set_thumbnail(
                                            url="https://github.com/SudhanPlayz/Discord-MusicBot/blob/master/assets/logo.gif?raw=true")
					await member.send(embed=embed)
				await member.move_to(priv_vc)
				await asyncio.sleep(1500)
				await member.send('Notice!\nYou have 5 minutes left until your private vc is deleted!')
				await asyncio.sleep(300)
				await priv_vc.delete()
				await member.send('Private VC time exhausted. Private VC had been delted.')

	'''@discord.slash_command(name = 'invite_vc', description = 'Invite a friend to your private VC!')
	async def invite_vc(self, ctx, member: Option(discord.Member, description = 'Whom do you want to invite?')):
		if ctx.author.voice.channel is None:
			ctx.respond('You are not in a Voice Channel. You cannot invite someone!', ephemeral = True)
		elif ctx.author.voice is not None:
			if ctx.author.voice.channel.name == '''




def setup(client):
	client.add_cog(PrivVC(client))
