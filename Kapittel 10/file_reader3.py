file_path = 'C:/Users/nonygale/source/repos/y/PythonCrashCourse/Kapittel 10/'

filename = 'pi_digits.txt'

# N�r man bruker en with blokk for � �pne en fil, s� er bare fila tilgjengelig inn i with blokken. Den lukkes automatisk
# For � ha dataene tilgjengelig utenfor, lagrer vi de her i en liste

with open(file_path+filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())