from discord.ext import commands
from __main__ import bot

class onStartup(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    """
    This is just a 'listener' that shows somehting in the CMD line
    when your bot is ready to go. 
    """
    @commands.Cog.listener()
    async def on_ready(self):
        # print('Loading the following cogs:')
        # for cog in commands.Cog():
        #     print(f'\t- {cog}')
        print(f'\n{bot.user} [{bot.user.id}] is connected to the following guilds:')
        for guild in bot.guilds:
            print(f'\t- {guild.name}(id: {guild.id})')

def setup(bot):
    bot.add_cog(onStartup(bot))