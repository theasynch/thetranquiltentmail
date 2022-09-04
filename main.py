import discord
from discord.ext import commands
import psutil
import os
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.voice_states = True

client = discord.Bot(debug_guilds=[862944848919003156])
bot = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
	print("The client is online!")
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name='The Dank Camp'))
	
@client.slash_command(name = 'test', description = "How about a test bruh?")
async def test_it(ctx):
	await ctx.respond("hey!")

@client.slash_command(name = 'test2', description = "Just and embed test.")
async def test2_it(ctx):
    embed = discord.Embed(

    )

@client.slash_command(name = 'ping', description = "pong?")
async def ping(ctx):
    latency = round(client.latency, 2)
    embed = discord.Embed(title='Stats from `Wissen`', color=0x4b33d3)
    embed.add_field(name='General Stats',
                    value=f"```yaml\nLatency: {latency} \n Client Version: v1.2.5\n Pycord Version: v2.0.1\n```", inline=False)
    embed.add_field(name="Server Stats",
                    value=f"```yaml\n OS: Windows\n CPU Usage: {psutil.cpu_percent()}%\n RAM Usage: {psutil.virtual_memory()[2]}%\n```")
    await ctx.send(embed=embed)


for filename in os.listdir('./cogs'):
    # Slicing the extension for cogs.py. so that the program can understand the language.
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('MTAwNzk4MDMzMjg3MzY5NTI2Mg.GvsB3c.xWGn1FC5qWBC-FvciM4mkMZ63nLBKpJKlHY9SA')
