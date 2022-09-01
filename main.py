import discord
import os
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Bot(debug_guilds=[862944848919003156])

@client.event
async def on_ready():
	print("The client is online!")
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name='DMs for Help.'))
	
@client.slash_command(name = 'test', description = "How about a test bruh?")
async def test_it(ctx):
	await ctx.respond("hey!")





for filename in os.listdir('./cogs'):
    # Slicing the extension for cogs.py. so that the program can understand the language.
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('MTAwNzk4MDMzMjg3MzY5NTI2Mg.GvsB3c.xWGn1FC5qWBC-FvciM4mkMZ63nLBKpJKlHY9SA')
