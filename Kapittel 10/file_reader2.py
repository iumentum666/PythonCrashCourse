file_path = 'C:/Users/nonygale/source/repos/y/PythonCrashCourse/Kapittel 10/'

filename = 'pi_digits.txt'

with open(file_path+filename) as file_object:
    for line in file_object:
        print(line.rstrip())