from discord.ext import commands
from discord import utils
import discord
import asyncio

class onMessage(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot:
			return

		if isinstance(message.channel, discord.DMChannel):
			guild = self.bot.get_guild(862944848919003156)
			categ = utils.get(guild.categories, name = "Modmail Tickets")
			files  = message.attachments
			if not categ:
				overwrites = {
					guild.default_role : discord.PermissionOverwrite(read_messages = False),
					guild.me : discord.PermissionOverwrite(read_messages = True)
				}
				categ = await guild.create_category(name = "Modmail tickets", overwrites = overwrites)

			channel = utils.get(categ.channels, topic = str(message.author.id))
			if not channel:
				channel = await categ.create_text_channel(name = f"{message.author.name}#{message.author.discriminator}", topic = str(message.author.id))
				await channel.send(f"Attention! <@&863438883631005717> , <@&862945401837191179>, <@&866261097442312202>, <@&862962601754492929> and <@&866261099371167754> \n New modmail created by {message.author.mention}")
				embed = discord.Embed(title = "ModMail Sucessful!", description = "A new thread was created sucessfully in the server! Please wait. The mods will reach out to you soon. \n `Thank You for using this service!`", color = 0x00ff00)
				await message.author.send(embed = embed)
				await message.add_reaction("✅")

			embed = discord.Embed(description = message.content, colour = 0x696969)
			for file in files:
				await channel.send(file.url)
			embed.set_author(name = message.author, icon_url = message.author.avatar_url)
			await channel.send(embed = embed)

		elif isinstance(message.channel, discord.TextChannel):
			files = message.attachments
			if message.content.startswith(self.bot.command_prefix):
				pass
			else:
				topic = message.channel.topic
				if topic:
					member = message.guild.get_member(int(topic))
					if member:
						for file in files:
							await member.send(file.url)
						embed = discord.Embed(description = message.content, colour = 0x696969)
						embed.set_author(name=message.author, icon_url=message.author.avatar_url,
						                 url=f"https://discordapp.com/users/{message.author.id}")
						await member.send(embed = embed)

	@commands.command()
	async def close(self, ctx, *, text = None):
		if ctx.channel.category.name == "Modmail Tickets":
			if text == None:
				text = "N/A"
			id = int(ctx.channel.topic)
			member = self.bot.get_user(id)
			await member.send("The thread is closing in 10s!")
			await ctx.send("Deleting the channel in 10 seconds!")
			await asyncio.sleep(10)
			embed = discord.Embed(title = "Thread Closed", description = f"This thread was closed by {ctx.author.name}\n Reason: {text}")
			await member.send(embed = embed)
			await ctx.channel.delete()

def setup(bot):
	bot.add_cog(onMessage(bot))
