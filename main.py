from discord.ext import commands
import discord
import os
intents = discord.Intents.default()
# we need members intent too
intents.members = True

client = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
	print("The client is online!")
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name='DMs for Help.'))
	

@client.command()
async def mail(ctx,member: discord.Member = None, *,body):
	user = ctx.author
	if member == None:
		await ctx.send("No member specified, or the member is not found!")
	embed = discord.Embed(title = "Message from the Mods!", description = f"Hey {member.mention}!, You have received a message from the Mods @Dank Camp.")
	embed.add_field(name = "__Author__:", value = f"{user.mention}", inline = False)
	embed.add_field(name = "__Message__", value = f"{body}", inline = False)
	embed.set_footer(text = "Please do not reply to this message unless you want to create a thread!")
	await member.send(embed=embed)


@client.command()
async def chnick(ctx, member: discord.Member = None):
	if ctx.author.id == 692295384868978710:
		await member.edit(nick="The Tranquil Tent")
		await ctx.send(f'Nickname was changed for {member.mention} ')
	else:
		pass

for filename in os.listdir('./cogs'):
    # Slicing the extension for cogs.py. so that the program can understand the language.
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('MTAwNzk4MDMzMjg3MzY5NTI2Mg.GvsB3c.xWGn1FC5qWBC-FvciM4mkMZ63nLBKpJKlHY9SA')
