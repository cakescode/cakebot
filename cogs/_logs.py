from discord.ext import commands
import random
import datetime
from __main__ import bot

class logs(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	log_channel = 1130165249912360980
	# guild_id = 1080972389808091136

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.guild().id == bot.guild().id and not message.author.bot:
			await bot.get_channel(self.log_channel).send(f'```Sent by: {message.author} | {message.author.id}```'
							f'```Message: {message.content}```')
	
	@commands.Cog.listener()
	async def on_message_delete(self, message):
		if message.guild().id == bot.guild().id and not message.author.bot:
			await bot.get_channel(self.log_channel).send(f'```Message by {message.author}[{message.author.id}] has been deleted!```'
							f'```Message: {message.content}```')

def setup(bot):
	bot.add_cog(logs(bot))
