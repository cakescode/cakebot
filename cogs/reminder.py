from discord.ext import tasks, commands
import datetime, asyncio


class reminder(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.coding_reminder.start()

	@tasks.loop(minutes=5)
	async def coding_reminder(self): # TODO : Fix coding_reminder()
		reminder_channel = self.bot.get_channel(1125139363517436014)
		current_year = datetime.datetime.now().year
		current_month = datetime.datetime.now().month
		current_day = datetime.datetime.now().day
		time_one = datetime.datetime(year=current_year, 
			       month=current_month,
				   day=current_day,
				   hour=21)
		time_two = datetime.datetime(year=current_year, 
			       month=current_month,
				   day=current_day,
				   hour=22)
		if time_one <= datetime.datetime.now() <= time_two:
			await reminder_channel.send('time test')
			await asyncio.sleep(6000)

def setup(bot):
	bot.add_cog(reminder(bot))
