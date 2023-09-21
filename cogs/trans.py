import discord.ext, googletrans, random
from discord.ext import commands
from __main__ import traceback

class googletrans_func(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.gl = googletrans.LANGUAGES # all supported langs in a dict
		self.gl_codes = googletrans.LANGCODES # reverse of self.gl
		self.translator = googletrans.Translator()
		self.THRESHOLD = 0.85 # if confidence lower than this & not multi_lang then return
		self.LANGUAGE = 'en' # print(googletrans.LANGUAGES) to get lang codes


	@commands.Cog.listener()
	async def on_message(self, message):
		# initial check
		if message.author.bot: return

		try: 
			detected = self.translator.detect(message.content)
			lang = detected.lang
			multi_lang = isinstance(lang, list)

			# if LANGUAGE or within the confidence THRESHOLD of LANGUAGE then return
			if lang in self.LANGUAGE: return
			if detected.confidence < self.THRESHOLD and not multi_lang: return
			
			# if detection picks up 2 potential languages
			if multi_lang:
				# quick fix bc the self.gl keys dont match with API dict from detect()
				for l in len(lang):
					l = l.lower()
				detected.confidence = detected.confidence[0] # extract value from list
				detected_language = f'{self.gl[lang[0]]}/{self.gl[lang[1]]}' # for output

			else:
				lang = lang.lower()
				detected_language = f'{self.gl[lang]}'

			# translate message to english
			translation = self.translator.translate(message.content, dest=self.LANGUAGE)
			pronunciation = translation.extra_data['translation'][1:]
			n = '\n'

			# send results of translation as embed
			embed = discord.Embed(title=f'{message.content}:',
				description=(f'{pronunciation[0][-1] + n if pronunciation else ""}'
					f'"{translation.text}"'))
			embed.set_footer(text=(f'translated from {detected_language} to english'
				f'\nauto detection confidence: {detected.confidence * 100}%'))
			await message.channel.send(embed=embed)

		# if error, send error message to channel that caused it
		except Exception as e: await traceback(message.channel, e)


	@commands.slash_command(description='Type /languages to get a list of supported languages.')
	async def translate(self, ctx, langauge, message):
		# initial checks
		if langauge.casefold() in ('chinese', 'chinese simplified'): langauge = 'chinese (simplified)'
		elif langauge.casefold() in ('chinese traditional'): langauge = 'chinese (traditional)'
		elif langauge.casefold() in ('kurdish', 'kurmanji'): langauge = 'kurdish (kurmanji)'
		elif langauge.casefold() in ('myanmar', 'burmese'): langauge = 'myanmar (burmese)'

		try:
			translated = self.translator.translate(message, dest=self.gl_codes[langauge.casefold()])
			embed = discord.Embed(title=f'{message}:', description=translated.text)
			embed.set_footer(text=f'translated from english to {langauge}')

		except ValueError as v:
			embed = discord.Embed(title='Not a supported language!',
				description='Please enter a supported language.')
			embed.set_footer(text=('Type /languages to get a list of supported languages.'))
			await ctx.send(embed=embed)

		except Exception as e: await traceback(ctx, e)

		finally: await ctx.respond(embed=embed)


	@commands.slash_command(description='All supported languages for /translate')
	async def languages(self, ctx):
		languages = ''

		for lang in self.gl.items(): languages += f'\n- {lang[1].title()}'

		try:
			embed = discord.Embed(title='Supported Languages:', description=languages)
			embed.set_footer(text='Not case sensitive but must otherwise be entered as seen')
			await ctx.respond(embed=embed)
			
		except Exception as e: await traceback(ctx, e)


def setup(bot):
	bot.add_cog(googletrans_func(bot))

# TODO: if output == input: return