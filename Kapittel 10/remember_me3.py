import json

# Denne versjonen kombinerer funksjonaliteten som lagrer informasjon
# om brukeren med funksjonaliteten som sjekker info om brukeren
# Samme som foregående, men vi putter alt inn i en funksjon...

def get_stored_username():
	"""
	Get stored username if available.
	"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username	


def get_new_username():
	"""
	Prompt for a new username.
	"""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username


def greet_user():
	"""
	Greet user by name...
	"""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
			username = get_new_username()
			print("We'll remember you when you come back, " + username + "!")
		
greet_user()