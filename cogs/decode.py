from discord.ext import commands

class decoder(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	allowed_role = 'cake'
	alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	@commands.slash_command()
	@commands.has_any_role(allowed_role)
	async def decode(self, ctx, message):
		message = message.split(' ')
		# mark the length of the message based on len of the input // 3
		length = len(message) // 3
		# split the list into 3 parts (the two keys and the message)
		key_one = message[:length]
		key_two = message[length:length * 2]
		encoded_list = message[length * 2:]
		decoded = ''
		worked = True
		# for each number in the length, apply the keys and output index of alp
		for index, key in enumerate(encoded_list):
			if len(encoded_list) == length:
				key = int(key) # convert key to int
				k_one = int(key_one[index])
				k_two = int(key_two[index])
				final_key = key + (k_one + k_two) - 1
				decoded += decoder.alp[int(final_key) % 26]
			elif len(encoded_list) < length:
				await ctx.respond('Error: Message is longer than keys')
				worked = False
				break
			elif len(encoded_list) > length:
				await ctx.respond('Error: Message is shorter than keys')
				worked = False
				break
		if worked:
			await ctx.respond(f'```{decoded}```')

def setup(bot):
	bot.add_cog(decoder(bot))
