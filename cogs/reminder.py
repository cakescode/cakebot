from discord.ext import tasks, commands
import datetime, asyncio
from __main__ import bot

class reminder(commands.Cog):
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

	@bot.event
	async def coding_reminder(self, ctx):
		while True:
			if '17:00:00' <= datetime.datetime.now() <= '17:10:00':
				await ctx.send('time test')
				await asyncio.sleep(600)

def setup(bot):
	bot.add_cog(reminder(bot))
