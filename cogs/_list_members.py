from discord.ext import commands, tasks
from __main__ import bot

class list_members(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.list_all_members.start()

	@tasks.loop(minutes=5)
	async def list_all_members(self):
		members = []
		print(bot.guilds)
		for member in bot.guilds.Guild.members:
			members.append(member)
			print(member)
			await self.bot.get_channel(1125139363517436014).send(member)
		


def setup(bot):
	bot.add_cog(list_members(bot))
