from discord.ext import commands
import random
import datetime

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command()
	async def hello(self, ctx):
		if 10 <= datetime.datetime.now().hour < 19:
			await ctx.respond("こんにちは『good day』!")
		elif 19 <= datetime.datetime.now().hour <= 24:
			await ctx.respond("こんばんは『good evening』!")
		else:
			await ctx.respond("おはよう『good morning』!")

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.content.startswith('!testing'):
			await message.channel.send(f'This is a command with a listener')

		if message.content.startswith('!say'):
			await message.channel.send(f'{message.content.replace("!say", "")}')

		if message.content.startswith('thanks'):
			if message.content != 'thanks':
				await message.channel.send(message.content.replace("thanks ", "ur welcome "))

def setup(bot):
	bot.add_cog(Fun(bot))
