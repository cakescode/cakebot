import discord.ext
from discord.ext import commands
from __main__ import traceback

class rps(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.valid_choices = (
			'rock',
			'paper',
			'scissors',
		)
		self.cog_checkpossible_results = {
			'rock paper': False,
			'rock scissor': True,
			'paper scissors': False,
			'paper rock': True,
			'scissors rock': False,
			'scissors paper': True
		}
		self.contestants = []
		self.choices = []

	def rps_game(self, offense, defense):
		game_data = offense + defense
		print(f'game_data: {game_data}') # debug

		if offense == defense:
			return 'Tie'

		results = self.possible_results[game_data]
		print(f'results: {results}') # debug

		return results


	@commands.slash_command()
	async def rps(self, ctx, choice):
		if not choice.lower() in self.valid_choices:
			await ctx.respond(embed=discord.Embed(title='Valid choices:',
				description='You must choose one of the following:\n\n- Rock\n- Paper\n- Scissors'))

		elif len(self.contestants) < 2:
			self.contestants.append(ctx.author.id)
			self.choices.append(choice)
			await ctx.respond(embed=discord.Embed(title=f'{ctx.author.name} has started an Rock Paper Scissors Challenge!',
				description='Type /rps `your choice goes here` to accept the challenge!'))

		elif len(self.contestants) == 2:
			await ctx.respond(embed=discord.Embed(title='Rock Paper Scissors:',
				description=f'<@{self.contestants[1]}> has accepted a challenge by <@{self.contestants[0]}>'))
			results = self.rps_game(self.choices[0], self.choices[1])

			if results:
				winner = self.contestants[0]

			await ctx.send(embed=discord.Embed(
				title='RPS Results:',
				description=f'Winner: <@{winner}>'))

			self.contestants = [] # reset contestants list for next game


def setup(bot):
	bot.add_cog(rps(bot))
