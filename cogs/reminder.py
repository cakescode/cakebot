from discord.ext import tasks, commands
import datetime, asyncio

class reminder(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	loop_val = 1

	@tasks.loop(minutes=5)
	async def coding_reminder(self):
		await print(f'debug: loop lap {loop_val}')
		loop_val += 1
		reminder_channel = self.bot.get_channel(1125139363517436014)
		if '22:35:00' <= datetime.datetime.now() <= '22:45:00':
			await reminder_channel.send('time test')
			await print('debug: time test')
			await asyncio.sleep(600)

def setup(bot):
	bot.add_cog(reminder(bot))

# TODO : Fix coding_reminder()