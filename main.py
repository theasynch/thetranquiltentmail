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

bot.run('ODk3MzYzNTMxNjgxMzk0NzE4.YWUk6g.Pbi6xsEwV9_LQIY46Qcd8SK1-Qg')
