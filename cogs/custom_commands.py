from discord.ext import commands

class custom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command()
	async def hello(self, ctx):
		await ctx.respond("こんにちは『hello』!")

def setup(bot):
	bot.add_cog(custom(bot))
