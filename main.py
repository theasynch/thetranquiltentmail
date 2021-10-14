from discord.ext import commands
import discord
import os

intents = discord.Intents.default()
# we need members intent too
intents.members = True

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
	print("The bot is online!")
	bot.load_extension("cogs.onMessage")
	await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name='DMs for Help.'))

@bot.command()
async def mail(ctx,member: discord.Member = None, *,body):
	user = ctx.author
	if member == None:
		await ctx.send("No member specified, or the member is not found!")
	embed = discord.Embed(title = "Message from the Mods!", description = f"Hey {member.mention}!, You have received a message from the Mods @Dank Camp.")
	embed.add_field(name = "__Author__:", value = f"{user.mention}", inline = False)
	embed.add_field(name = "__Message__", value = f"{body}", inline = False)
	await member.send(embed=embed)

bot.run('ODk3MzYzNTMxNjgxMzk0NzE4.YWUk6g.bvbRcMO02yioTyfn64rO7qovlUY')
