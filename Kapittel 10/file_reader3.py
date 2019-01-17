file_path = 'C:/Users/nonygale/source/repos/y/PythonCrashCourse/Kapittel 10/'

filename = 'pi_digits.txt'

# Når man bruker en with blokk for å åpne en fil, så er bare fila tilgjengelig inn i with blokken. Den lukkes automatisk
# For å ha dataene tilgjengelig utenfor, lagrer vi de her i en liste

with open(file_path+filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())