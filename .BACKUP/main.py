"""
TO INSTALL:

pip install discord.py
pip install py-cord

"""

import os, sys, discord
from discord.ext import commands

# This sets the prefix to use for commands. 
bot = commands.Bot(command_prefix = '/', intents=discord.Intents.all())

# In this function, we load all the files from the Cogs folder.
# Cogs are just files that hold our commands.
def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            bot.load_extension("cogs." + file[:-3])

# In this function, we use an argument to load the Bot-Token.
# To run your bot, you would use: 'python main.py TOKEN'
def load_token_and_run():
    if len(sys.argv) > 1:
        TOKEN = sys.argv[1]
        bot.run(TOKEN)
    else:
        print('ERROR: You must include a bot token.')

if __name__ == "__main__":
    load_cogs()
    load_token_and_run()
