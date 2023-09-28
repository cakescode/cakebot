"""
TO INSTALL:

pip install py-cord
pip install translate
pip install 
pip install 

"""
import os
import sys
import discord
from discord.ext import commands, tasks

prefix = '>'

# This sets the prefix to use for commands. 
bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix),
                   intents=discord.Intents.all())

async def traceback(ctx, e):
    print(f'{e}')
    embed = discord.Embed(
        title='Traceback (most recent call):',
        description=f'```{e}```',
        color=0xea623b)
    embed.set_image(url='https://media.tenor.com/zpvRLlcI5mEAAAAC/anime_blush_error_moan.gif')
    await ctx.send(embed=embed)

# In this function, we load all the files from the Cogs folder.
# Cogs are just files that hold our commands.
def load_cogs():
    errors = 0
    for file in os.listdir('./cogs'):
            if file.endswith('.py') and not file.startswith('_'):
                print(f'Loading Cog: {file[:-3]}')
                try:
                    bot.load_extension('cogs.' + file[:-3])
                except Exception as e:
                    errors += 1
                    print(f'File {file[:-3]} caused the following error:\n{e}')
    print(f'\nTotal broken cogs: {errors}')

# In this function, we use an argument to load the Bot-Token.
# To run your bot, you would use: python main.py TOKEN
def load_token_and_run():
    if len(sys.argv) > 1:
        TOKEN = sys.argv[1]
        bot.run(TOKEN)
    else:
        print('ERROR: You must include a bot token.')

if __name__ == '__main__':
    load_cogs()
    load_token_and_run()
