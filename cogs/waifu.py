import discord.ext
from discord.ext import commands
import requests
from __main__ import traceback

class Waifu(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command()
	async def waifu(self, ctx, tag):
		url = 'https://api.waifu.im/search'
		params = {
			'included_tags': [f'{tag}'],
			'height': '>=2000'
		}
		response = requests.get(url, params=params)
		data = response.json()
		print(response, data, sep='\n') # debug
		if response.status_code == 200:
			try:
				await ctx.respond(embed=discord.Embed().set_image(url=data))
			except Exception as e:
				print(e)
				await traceback(ctx, e)
		else:
			await traceback(ctx, f'''Waifu request failed with code: {int(response.status_code)}
Reason: {response.json()}''')


def setup(bot):
    bot.add_cog(Waifu(bot))
