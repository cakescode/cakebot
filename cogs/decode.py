from discord.ext import commands
import random

class decoder(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	allowed_role = 'cake'
	alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	@commands.slash_command()
	@commands.has_any_role(allowed_role)
	async def decode(self, ctx, message): # TODO: fix decoder
		true_message = ''
		for char in message:
			if char != ' ':
				true_message += char
		print(true_message)
		# mark the length of the message based on len of the input // 3
		length = len(true_message) // 3
		# split the list into 3 parts (the two keys and the message)
		key_one = true_message[:length]
		key_two = true_message[length:length * 2]
		encoded = true_message[length * 2:]
		decoded = ''
		worked = True
		# for each number in the length, apply the keys and output index of alp
		for index, key in enumerate(encoded):
			if len(encoded) == length:
				key = int(key) # convert key to int
				print(f'key = {key}')
				k_one = int(key_one[index])
				print(f'k_one = {k_one}')
				k_two = int(key_two[index])
				print(f'k_two = {k_two}')
				final_key = key + (k_one + k_two) - 1
				print(f'key({key}) + (k_one({k_one}) + k_two({k_two})) - 1 = {final_key}')
				decoded += decoder.alp[(int(encoded) - final_key) % 26]
				print(f'decoded = {decoded}')
			elif len(encoded) < length:
				await ctx.respond('Error: Message is longer than keys')
				worked = False
				break
			elif len(encoded) > length:
				await ctx.respond('Error: Message is shorter than keys')
				worked = False
				break
		if worked:
			await ctx.respond(decoded)

def setup(bot):
	bot.add_cog(decoder(bot))
