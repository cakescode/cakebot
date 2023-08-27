from discord.ext import commands
import googletrans
from googletrans import Translator
import json, sys
# import translators

class googletrans_func(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	async def token_aquirer(token):
		aquirer = googletrans.TokenAquirer()
		return aquirer.do(token)

	# load all kanjis from json as read only mode
	kanji = json.load(open('_kanji.json', 'r'))

	# initiate cog that listens to all messages
	@commands.Cog.listener()
	async def on_message(self, message):
		translator = Translator()
		# if message wasnt sent by a bot
		if not message.author.bot:
			# check each character in message
			for char in message.content:
				# if character is a kanji that is in the json
				if char in googletrans_func.kanji['kanji']:
					# send the resulting translation to the channel the msg was sent to
					try:
						token = googletrans_func.token_aquirer(message.content)
						await message.channel.send(
							f'auto-translation: {translator.translate(message.content)}')
					except:
						e_type, e_value, e_traceback = sys.exc_info()
						print(f'Type: `{e_type}`\nValue: `{e_value}`\nTraceback: `{e_traceback}`')
						await message.channel.send('https://tenor.com/view/anime_blush_error_moan-gif-19771348')
						await message.channel.send(f'Type: `{e_type}`\nValue: `{e_value}`\nTraceback: `{e_traceback}`')
					# the break is so the first kanji it sees in the message,
					# it stops scanning and starts the translation pipeline.
					# this makes is more efficient bc it doesnt have to scan
					# the entire message, unless the kanji is either at the 
					# end or the message doesnt contain any kanji. It also
					# keeps the function from translating more than once if
					# more than one kanji or kana are in the message content.
					break

def setup(bot):
	bot.add_cog(googletrans_func(bot))
