file_path = 'C:/Users/nonygale/source/repos/y/PythonCrashCourse/Kapittel 10/'

filename = 'pi_digits.txt'

# Her kjører vi alt en gang til.. men nå lager vi alle linjene i fila som en lang streng i steden.

with open(file_path+filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))