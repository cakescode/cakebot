import discord.ext
from discord.ext import commands
from __main__ import traceback
import random

class rps(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	valid_choices = (
		'rock',
		'paper',
		'scissors',
	)
	possible_results = {
		'rock paper': False,
		'rock scissor': True,
		'paper scissors': False,
		'paper rock': True,
		'scissors rock': False,
		'scissors paper': True
	}
	contestants = []
	choices = []

	def rps_game(self, offense, defense):
		game_data = offense + defense
		print(f'game_data: {game_data}') # debug
		offense_wins = None
		if offense == defense:
			return 'Tie'
		if offense == 'rock' and defense == 'paper':
			offense_wins = False
		if offense 

	@commands.slash_command()
	async def rps(self, ctx, message):
		if not message.content.lower() in rps.valid_choices:
			await ctx.send(embed=discord.Embed(
				title='Valid choices:',
				description='You must choose one of the following:\n\nRock\nPaper\nScissors'
			))
		elif len(rps.contestants) < 2:
			rps.contestants.append(message.author.id)
			rps.choices.append(message.content)
		elif len(rps.contestants) == 2:
			await ctx.send(embed=discord.Embed(
				title='Rock Paper Scissors:',
				description=f'<@{rps.contestants[1]}> has accepted a challenge by <@{rps.contestants[0]}>'))
			
			rps.contestants = []

def setup(bot):
	bot.add_cog(rps(bot))
