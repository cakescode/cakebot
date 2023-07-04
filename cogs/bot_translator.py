from discord.ext import commands
from translate import Translator
import translators

class bot_translator(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def japanese(self, ctx, message):
		try:
			english_translation = translators.translate_text(message, from_language='en', to_language='ja')
			await ctx.send(english_translation)
		except TypeError as te:
			await ctx.send(f'TypeError: {te}')
		except NameError as ne:
			await ctx.send(f'NameError: {ne}')
		except AttributeError as ae:
			await ctx.send(f'AttributeError: {ae}')

	@commands.command()
	async def en(self, ctx, message):
		try:
			en_ts = Translator(to_lang='en', from_lang='ja')
			en_translation = en_ts.translate(message)
		except TypeError as e:
			print(e)
		except NameError as ne:
			await ctx.send('Invalid input!')
			print(ne)
		finally:
			await ctx.send(en_translation)

	@commands.command()
	async def ja(self, ctx, message):
		try:
			ja_ts = Translator(to_lang='ja')
			ja_translation = ja_ts.translate(message)
		except TypeError as e:
			print(e)
		except NameError as ne:
			await ctx.send('Invalid input!')
			print(ne)
		finally:
			await ctx.send(ja_translation)

def setup(bot):
	bot.add_cog(bot_translator(bot))
