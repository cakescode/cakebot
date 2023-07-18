from discord.ext import commands
import random
import time

class uwu(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	gifs = ['https://media.tenor.com/-7xFCtnyUCcAAAAM/uwu-ts-team-uwu.gif',
	  'https://c.tenor.com/8qTl-eokkR4AAAAC/uwu-smug.gif',
	  'https://c.tenor.com/tNIXtOf62wQAAAAd/tenor.gif',
	  'https://media.tenor.com/bn4xnRtfzosAAAAC/muy-bien.gif',
	  'https://media.tenor.com/AR8p1LHTOFEAAAAC/discord-uwu-sweat.gif',
	  'https://c.tenor.com/7FmzekCozzYAAAAM/uwu-cat.gif',
	  'https://c.tenor.com/CfmWkEvWvSUAAAAj/dance-uwu.gif',
	  'https://c.tenor.com/RLp8XZj8QzwAAAAj/uwu.gif',
	  'https://i.pinimg.com/originals/b7/5f/2c/b75f2c027971a82e62447a836466aa34.gif',
	  'https://i.pinimg.com/originals/07/b6/27/07b6274c203957bf2bf42c82ca2cf91c.gif',
	  'https://c.tenor.com/VrfSZUjiWn4AAAAC/tenor.gif',
	  'https://cdn130.picsart.com/236413993006201.gif',
	  'https://media.tenor.com/yhTraOnJ1DgAAAAd/cement-uw-u.gif',
	  'https://media.tenor.com/s8R4ZiyKBzkAAAAM/uw-u-de-awa.gif',
	  'https://media.tenor.com/MQ-EY9f1kEcAAAAM/uw-u-furry.gif',
	  'https://media.tenor.com/iPd7tVaqhzYAAAAM/rina-uwu.gif',
	  'https://media.tenor.com/0di09DwQRSYAAAAM/dance-uwu.gif',
	  'https://media.tenor.com/-7xFCtnyUCcAAAAM/uwu-ts-team-uwu.gif',
	  'https://media.tenor.com/maR9CUaIJj0AAAAM/uwu.gif',
	  'https://media.tenor.com/RxnWCMD50icAAAAM/uwu.gif',
	  'https://media.tenor.com/d6KFrVXhlM0AAAAM/uw-u-clan-discord-gif.gif',
	  'https://media.tenor.com/jnnoarCs6QkAAAAM/possibly-people-uwu.gif',
	  'https://media.tenor.com/6MlCrn7q6i8AAAAM/uwu-meme.gif',
	  'https://media.tenor.com/X6JOu2zG0dgAAAAM/uwu.gif',
	  'https://media.tenor.com/LEbXrENImIsAAAAM/uwu-nod.gif',
	  'https://media.tenor.com/COM7-eId_JEAAAAM/shion-sonozaki-what.gif',
	  'https://media.tenor.com/CLGeezSFPfEAAAAM/uw-u.gif',
	  'https://media.tenor.com/tZyMjllVkKkAAAAM/uwu.gif',
	  'https://media.tenor.com/mpvtsV8EtyQAAAAM/doding-doding-daga.gif',
	  ]
	
	anti_spam = 30
	gif_previous = []
	gif_choice = random.choice(gifs)
	last_msg = time.time()
	time_between = anti_spam
	warned = False

	@commands.Cog.listener()
	async def on_message(self, message):
		step = 1
		if message.content.lower() == 'uwu' and uwu.time_between >= uwu.anti_spam and not message.author.bot:
			while uwu.gif_choice in uwu.gif_previous:
				if len(uwu.gif_previous) == len(uwu.gifs) - 1:
					uwu.gif_previous = []
				uwu.gif_choice = random.choice(uwu.gifs)
				uwu.last_msg = time.time()
				step += 1
			uwu.gif_previous.append(uwu.gif_choice)
			await message.channel.send(uwu.gif_choice)
			uwu.warned = False
		elif message.content.lower() == 'uwu' and not message.author.bot:
			await message.delete()
			if not uwu.warned:
				await message.channel.send('please dont spam uwu lmao')
				uwu.warned = True
		uwu.time_between = abs(uwu.last_msg - time.time())


def setup(bot):
	bot.add_cog(uwu(bot))
