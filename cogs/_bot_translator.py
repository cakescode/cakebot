import discord.ext
from discord.ext import commands
from translate import Translator
# from __main__ import prefix
import json
# import translators

class bot_translator(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# load all kanjis from json as read only mode
	kanji = json.load(open('_kanji.json', 'r'))

	# initiate cog that listens to all messages
	@commands.Cog.listener()
	async def on_message(self, message):
		# if message wasnt sent by a bot
		if not message.author.bot and not message.content.startswith('>'):
			# check each character in message
			for char in message.content:
				# if character is a kanji that is in the json
				if char in bot_translator.kanji['kanji'] or char in bot_translator.kanji['kana']:
					# attempt to translate, if it throws an error it wont break the bot
					try:
						# set translation to variable
						auto_ts = Translator(to_lang='en', from_lang='ja')
					# if no error was thrown
					finally:
						# send the resulting translation to the channel the msg was sent to
						await message.channel.send(
							embed=discord.Embed(title='auto-translation:', description=f'{auto_ts.translate(message.content)}'))
					# the break is so the first kanji it sees in the message,
					# it stops scanning and starts the translation pipeline.
					# this makes is more efficient bc it doesnt have to scan
					# the entire message, unless the kanji is either at the 
					# end or the message doesnt contain any kanji.
					break

	@commands.command()
	async def en(self, ctx, message):
		try:
			en_ts = Translator(to_lang='en', from_lang='ja')
			en_translation = en_ts.translate(message)
		except TypeError as e:
			print(e)
		except NameError as ne:
			await ctx.send(embed=discord.Embed(description='Invalid input!'))
			print(ne)
		finally:
			await ctx.send(embed=discord.Embed(description=en_translation))

	@commands.command()
	async def ja(self, ctx, message):
		try:
			ja_ts = Translator(to_lang='ja')
			ja_translation = ja_ts.translate(message)
		except TypeError as e:
			print(e)
		except NameError as ne:
			await ctx.send(embed=discord.Embed(description='Invalid input!'))
			print(ne)
		finally:
			await ctx.send(embed=discord.Embed(description=ja_translation))

	@commands.command()
	async def nor(self, ctx, message):
		try:
			nor_ts = Translator(to_lang='nor')
			nor_translation = nor_ts.translate(message)
		except TypeError as e:
			print(e)
		except NameError as ne:
			await ctx.send(embed=discord.Embed(description='Invalid input!'))
			print(ne)
		finally:
			await ctx.send(embed=discord.Embed(description=nor_translation))

def setup(bot):
	bot.add_cog(bot_translator(bot))
