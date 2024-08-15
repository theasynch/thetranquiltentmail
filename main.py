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
	


@client.slash_command(name = 'ping', description = "pong?")
async def ping(ctx):
    latency = round(client.latency, 2)
    embed = discord.Embed(title='Stats from `Camp Utilities`', color=0x4b33d3)
    embed.add_field(name='General Stats',
                    value=f"```yaml\nLatency: {latency} \n Client Version: v1.2.5\n Pycord Version: v2.0.1\n```", inline=False)
    embed.add_field(name="Server Stats",
                    value=f"```yaml\n OS: Windows\n CPU Usage: {psutil.cpu_percent()}%\n RAM Usage: {psutil.virtual_memory()[2]}%\n```")
    await ctx.respond(embed=embed)


for filename in os.listdir('./cogs'):
    # Slicing the extension for cogs.py. so that the program can understand the language.
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('bot_key')
