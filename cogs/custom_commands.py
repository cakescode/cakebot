from discord.ext import commands


class custom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# @commands.slash_command()
	# async def hello(self, ctx):
	# 	await ctx.respond("Oh, Hi there.")

	# @commands.Cog.listener()
	# async def on_message(self, message):
	# 	if message.content.startswith('!testing'):
	# 		await message.channel.send(f'This is a command with a listener')

	# 	if message.content.startswith('!say'):
	# 		await message.channel.send(f'{message.content.replace("!say", "")}')

	@commands.command()
	async def test(self, ctx):
		await ctx.send('this is a test')

def setup(bot):
	bot.add_cog(custom(bot))
