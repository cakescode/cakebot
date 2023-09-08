import discord.ext
from discord.ext import commands

class error_traceback(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def traceback(ctx, e):
		print(f'{e}`')
		embed = discord.Embed(
			title='Traceback (most recent call):',
			description=f'```{e}```',
			color=0xea623b)
		embed.set_image(url='https://media.tenor.com/zpvRLlcI5mEAAAAC/anime_blush_error_moan.gif')
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(error_traceback(bot))
