from discord.ext import commands
import random

class cipher(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command()
	async def encode(self, ctx, message): # TODO: fix encoder
		alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		encoded = ''
		encoded_index = []
		key_one = ''
		key_two = ''
		# convert each letter into a number and apply each shift individually
		for char in message():
			if char in alp:
				shift_one = random.randrange(51, 99) # first key
				shift_two = random.randrange(27, 50) # second key
				encoded = alp.index(char) - shift_one # first layer of encryption
				key_one += str(f'{shift_one:02} ') # add first key to key list
				encoded = alp[encoded % 26] # convert first encryption num to letter
				encoded = alp.index(encoded) - shift_two # second layer of encryption
				key_two += str(f'{shift_two:02} ') # add second key to key list
				encoded = alp[encoded % 26] # convert second encryption num to letter
				encoded_index.append(str(f'{alp.index(encoded) + int(1):02}')) # output result
			elif char == ' ': # spaces are removed
				pass
			else: # any other characters besides letters or spaces will result in following error
				ctx.send(f'Error: Character \'{char}\' is not allowed in the input')
				break
		encoded_index = ' '.join(encoded_index) # convert to string and sep with ' '
		output = f'{key_one}{key_two}{encoded_index}'
		ctx.send(output)

def setup(bot):
	bot.add_cog(cipher(bot))
