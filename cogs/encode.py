from discord.ext import commands
import random

class encoder(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	allowed_role = 'cake'
	alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	@commands.slash_command()
	@commands.has_any_role(allowed_role)
	async def encode(self, ctx, message):
		worked = True
		encoded = ''
		encoded_index = []
		key_one = ''
		key_two = ''
		message = message.upper() # make message uppercase
		# convert each letter into a number and apply each shift individually
		for char in message:
			if char in encoder.alp:
				shift_one = random.randrange(51, 99) # first key
				shift_two = random.randrange(27, 50) # second key
				encoded = encoder.alp.index(char) - shift_one # first layer of encryption
				key_one += str(f'{shift_one:02} ') # add first key to key list
				encoded = encoder.alp[encoded % 26] # convert first encryption num to letter
				encoded = encoder.alp.index(encoded) - shift_two # second layer of encryption
				key_two += str(f'{shift_two:02} ') # add second key to key list
				encoded = encoder.alp[encoded % 26] # convert second encryption num to letter
				encoded_index.append(str(f'{encoder.alp.index(encoded) + int(1):02}')) # output result
			elif char == ' ': # spaces are removed
				pass
			else: # any other characters besides letters or spaces will result in following error
				await ctx.respond(f'Error: Character \'{char}\' is not allowed in the input')
				worked = False
				break
		encoded_index = ' '.join(encoded_index) # convert to string and sep with ' '
		output = f'{key_one}{key_two}{encoded_index}'
		if worked:
			await ctx.respond(f'```{output}```')

def setup(bot):
	bot.add_cog(encoder(bot))
