from discord.ext import commands, tasks
from __main__ import traceback
import random

class reminder_command(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if not message.author.bot and message.content.startswith('remind me in'):
			message_split = message.content.split(' ')
			if message_split[3] in (
				'seconds',
				'second',
				'secs',
				'sec',
				'minutes',
				'minute',
				'mins',
				'min',
				'hours',
				'hour',
				'hrs',
				'hr',
				'days',
				'day',
				'weeks',
				'week',
				'months',
				'month',
				'years',
				'year',
				'decades',
				'decade',
				'centuries',
				'century',
				'eons',
				'eon',
			):
				timer = message_split[3]
			timer_range = int(message_split[4])


	@commands.Cog.listener()
	async def on_message(self, message):
		message_split = message.content.lower().split(' ')
		for word in message_split:
			if message.author.bot:
				break
			if word in ('kuriyama', 'mirai'):
				while reminder_command.gif_choice in reminder_command.gif_previous:
					if len(reminder_command.gif_previous) == len(reminder_command.gifs) - 1:
						reminder_command.gif_previous = []
					reminder_command.gif_choice = random.choice(reminder_command.gifs)
				reminder_command.gif_previous.append(reminder_command.gif_choice)
				try:
					await message.channel.send(reminder_command.gif_choice)
				except Exception as e:
					await traceback(message.channel, e)
				break


def setup(bot):
	bot.add_cog(reminder_command(bot))
