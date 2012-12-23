import sys
from random import choice

def generate_reply(post):
	"""
	Runs through the logic of creating a comment to post as a reply to another post. 
	If the post is not worth replying to, an empty string will be returned. 
	
	Arguments:
	post - The post that is potentially being replied to.
	"""

	#Makes it easier for comparisons later.
	post = post.lower()

	message = ""

	#Feel free to add any sort of funny, condescending behavior!
	if "ironic" in post:
		message += "That's not ironic. It's just coindicental. "
	elif "idea" in post:
		message += "Wow. What a shitty idea. "

	message += "You " + insulting_adjective() + " " + insulting_noun() + "!"
	return message

def insulting_adjective():
	"""
	Returns a random adjective from our list of offensive adjectives. 
	"""

	try:
		with open("adjectives.txt") as adj_list:
			return choice(adj_list.read().split())
	except EnvironmentError:
		print "Dude! Make a list of adjectives!"
		sys.exit()

def insulting_noun():
	"""
	Returns a random noun from our list of offensive nouns
	"""

	try:
		with open("nouns.txt") as noun_list:
			return choice(noun_list.read().split())
	except EnvironmentError:
		print "Dude! Make a list of nouns!"
		sys.exit()

print generate_reply("I have an idea!")
print generate_reply("That is so ironic!")
