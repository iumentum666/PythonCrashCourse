filename = 'alice.txt'

# This is a test of files that are not found. If the file is not present,
# This will throw an error. We need to handle that error.

try:
	with open(filename, encoding='utf-8') as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)