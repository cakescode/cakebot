import discord.ext
import googletrans
from discord.ext import commands
from __main__ import traceback

def is_multi_lang(lang):
	if isinstance(lang, list): return True
	else: return False

class googletrans_func(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.gl = googletrans.LANGUAGES
		self.translator = googletrans.Translator()
		self.THRESHOLD = 0.85
		self.LANGUAGE = 'en' # print(googletrans.LANGUAGES) to get lang codes


	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot: return

		try: 
			detected = self.translator.detect(message.content)
			lang = detected.lang
			multi_lang = is_multi_lang(lang)

			# if LANGUAGE or within the confidence THRESHOLD of LANGUAGE then return
			if lang == self.LANGUAGE or multi_lang and self.LANGUAGE in lang:
				return
			if detected.confidence < self.THRESHOLD and not multi_lang: 
				return
			
			# if detection picks up 2 potential languages
			if multi_lang:
				detected.confidence = detected.confidence[0] # extract value from list
				lang, lang_2 = lang[0], lang[1]
				detected_language = f'{self.gl[lang]}, {self.gl[lang_2]}' # for output

				# quick fix bc the self.gl keys dont match with API dict from detect()
				for l in range(2):
					if lang[l] == 'zh-CH': lang[l] = 'zh-ch'

			else:
				if lang == 'zh-CN': lang = 'zh-cn'
				detected_language = f'{self.gl[lang]}'

			# translate message
			translation = self.translator.translate(message.content, dest=self.LANGUAGE)

			# send results of translation as embed
			embed = discord.Embed(title=f'{message.content}:',
				description=f'{translation.text}')
			embed.set_footer(text=(f'translated from {detected_language}'
				f'\nauto detection confidence: {detected.confidence * 100}%'))
			await message.channel.send(embed=embed)

		# if error, send error message to channel that caused it
		except Exception as e:
			await traceback(message.channel, e)


	@commands.slash_command()
	async def translate(self, ctx, langauge, message):
		try:
			translated = self.translator.translate(message, dest=langauge.lower())
			embed = discord.Embed(title=f'{message}:', description=translated.text)
			embed.set_footer(text=f'translated from {self.gl[langauge]}')
			await ctx.respond(embed=embed)

		except ValueError as v:
			languages = ''
			for key, value in gl.items():
				languages += f'{key}: \t{value}\n'
			embed = discord.Embed(title='Valid Language Codes:', description=languages)
			embed.set_footer(text=('Please use the code on the left'
				'\nto select the language on the right'))
			await ctx.send(embed=embed)

		except Exception as e:
			await traceback(ctx, e)

def setup(bot):
	bot.add_cog(googletrans_func(bot))
