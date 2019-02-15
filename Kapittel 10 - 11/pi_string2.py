# file_path = 'C:/Users/nonygale/source/repos/y/PythonCrashCourse/Kapittel 10/'

filename = 'pi_million_digits.txt'

# Her kjorer vi alt en gang til.. men na lager vi alle linjene i fila som en lang streng i steden.

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52] + "...")
print(len(pi_string))