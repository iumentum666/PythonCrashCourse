# This program creates a file and writes what ever that is in the with block to it
# W in open, means that we open the file in write mode
# R = Read mode
# A = append mode

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	# Write function does not add newline
	file_object.write("I love creating new games.\n")