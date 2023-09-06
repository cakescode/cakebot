import discord.ext
import googletrans
from discord.ext import commands
from googletrans import Translator
from __main__ import traceback

class googletrans_func(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		THRESHOLD = 0.85
		multi_lang = False
		try: 
			if message.author.bot: return
			translator = Translator()
			detected = translator.detect(message.content)
			lang, confidence = detected.lang, detected.confidence
			# if detection picks up 2 potential languages
			if isinstance(lang, list):
				multi_lang = True
				confidence = confidence[0]
				lang, lang_2 = lang[0], lang[1]
			# if english or less than 80% sure its not english & not > 1 language
			if lang == 'en' or confidence < THRESHOLD and not multi_lang: return
			if lang == 'zh-CN': lang = 'zh-cn' # fix bc the dict keys dont match
			# translate message
			translation = translator.translate(message.content, dest='en')
			gl = googletrans.LANGUAGES # googletrans dictionary of languages
			if multi_lang: detected_language = f'{gl[lang]}, {gl[lang_2]}'
			else: detected_language = f'{gl[lang]}'
			# send results of translation as embed
			embed = discord.Embed(
				title=f'{message.content}:',
				description=f'{translation.text}')
			embed.set_footer(text=f'''
translated from {detected_language}
confidence: {confidence * 100}%''')
			await message.channel.send(embed=embed)
		# if error, send error message to channel that caused it
		except Exception as e:
			await traceback(message.channel, e)

	@commands.slash_command()
	async def japanese(self, ctx, message):
		try:
			translator = Translator()
			gl = googletrans.LANGUAGES
			translated = translator.translate(message, dest='ja')
			embed = discord.Embed(
				title=f'translation for "{message}"',
				description=translated.text
			)
			embed.set_footer(text=f'translated from {gl[translated.dest]}')
			await ctx.respond(embed=embed)
		except Exception as e:
			await traceback(ctx, e)
		

def setup(bot):
	bot.add_cog(googletrans_func(bot))
