from discord.ext import commands
from __main__ import traceback
import random

class kuriyama(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	gifs = [
		'https://tenor.com/view/kyoukai-no-kanata-beyond-the-boundary-gif-24994036',
		'https://tenor.com/view/mirai-kuriyama-beyond-the-boundary-kyoukai-no-kanata-icon-gif-22444024',
		'https://tenor.com/view/mirai-kuriyama-beyond-the-boundary-cry-sad-gif-21175183',
		'https://tenor.com/view/anime-gif-18993238',
		'https://tenor.com/view/fuyukaidesu-gif-24177067',
		'https://tenor.com/view/anime-cute-eyeglasses-look-gif-17723860',
		'https://tenor.com/view/mirai-kuriyama-gif-22718862',
		'https://tenor.com/view/money-anime-kyoto-animation-cute-girl-glasses-gif-17986159',
		'https://tenor.com/view/r-eal-gif-24518135',
		'https://tenor.com/view/mirai-kuriyama-cleaning-kyoukai-no-kanata-wiping-glasses-gif-8962880',
		'https://tenor.com/view/anime-gif-18993238',
		'https://tenor.com/view/kyoukai-no-kanata-mirai-kuriyama-mitsuki-nase-mitsurai-yuri-gif-23549524',
		'https://tenor.com/view/mirai-beyond-the-boundary-anime-mirai-kuriyama-kyoukai-no-kanata-gif-18824352',
		'https://tenor.com/view/anime-kawaii-card-captor-sakura-gif-5018277',
	]
	
	gif_previous = []
	gif_choice = random.choice(gifs)

	@commands.Cog.listener()
	async def on_message(self, message):
		message_split = message.content.lower().split(' ')
		for word in message_split:
			if message.author.bot:
				break
			if word in ('kuriyama', 'mirai'):
				while kuriyama.gif_choice in kuriyama.gif_previous:
					if len(kuriyama.gif_previous) == len(kuriyama.gifs) - 1:
						kuriyama.gif_previous = []
					kuriyama.gif_choice = random.choice(kuriyama.gifs)
				kuriyama.gif_previous.append(kuriyama.gif_choice)
				try:
					await message.channel.send(kuriyama.gif_choice)
				except Exception as e:
					await traceback(message.channel, e)
				break


def setup(bot):
	bot.add_cog(kuriyama(bot))
