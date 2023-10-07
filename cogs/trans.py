import discord.ext, googletrans, json
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
		self.N = '\n\n'
		self.COLOR = discord.Color.red()

	@commands.Cog.listener()
	async def on_message(self, message):

		# initial checks
		if message.author.bot: return

		try: 
			# with json.load(open('data.json', 'r'))['blacklist'] as blacklist:
			# 	if message.content in blacklist: return
			detected = self.translator.detect(message.content)
			lang = detected.lang
			multi_lang = isinstance(lang, list) # check if output is list
			
			# if detection picks up 2 potential languages
			if multi_lang:
				# quick fix bc the self.gl keys dont match with API dict from detect()
				for l in lang:
					l = l.lower()
				detected.confidence = detected.confidence[0] * 100 # extract value from list
				detected_language = f'{self.gl[lang[0]]}/{self.gl[lang[1]]}' # for output
			# if LANGUAGE or within the confidence THRESHOLD of LANGUAGE then return
			elif lang in self.LANGUAGE: return
			elif detected.confidence < self.THRESHOLD: return
			else:
				lang = lang.lower()
				detected_language = f'{self.gl[lang]}'

			# translate message to english
			translation = self.translator.translate(message.content, dest=self.LANGUAGE)
			if translation == message.content: return # if translation == message, dont translate
			pronunciation = translation.extra_data['translation'][-1]

			# send results of translation as embed
			embed = discord.Embed(title=f'{message.content}:',
				description=(f'{str(pronunciation[-1]).lower() + self.N if pronunciation else ""}'
					f'"{translation.text}"'))
			embed.set_footer(text=(f'translated from {detected_language} to english'
				f'\nauto detection confidence: {detected.confidence}%'))
			await message.channel.send(embed=embed)

		# if error, send error message to channel that caused it
		except Exception as e: await traceback(message.channel, e)


	@commands.slash_command(description=('Example: `/translate from english to japanese hello world`'))
	async def translate(self, ctx, old, new, message):
		# initial checks
		checklist = (old, new)
		for item in checklist:
			if item.casefold() in ('chinese', 'chinese simplified'): item = 'chinese (simplified)'
			elif item.casefold() in ('chinese traditional'): item = 'chinese (traditional)'
			elif item.casefold() in ('kurdish', 'kurmanji'): item = 'kurdish (kurmanji)'
			elif item.casefold() in ('myanmar', 'burmese'): item = 'myanmar (burmese)'

		try:
			translation = self.translator.translate(message, dest=self.gl_codes[new.casefold()])
			pronunciation = translation.extra_data['translation'][-1]
			embed = discord.Embed(title=f'{message}:', description=(
				f'{str(pronunciation[-1]).lower() + self.N if pronunciation else ""}'
				f'"{translation.text}"'))
			embed.set_footer(text=f'translated from {old} to {new}')

		except ValueError:
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