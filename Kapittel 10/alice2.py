filename = 'alice.txt'

# This is a test of files that are not found. If the file is not present,
# This will throw an error. We need to handle that error.
# In the previous file, we had an error. Here we will create the file

try:
	with open(filename, encoding='utf-8') as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
else:
	# Count the approximate number of words in the file.
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")