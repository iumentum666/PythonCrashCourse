# Her gjentar vi parrotkoden, men denne gangen med en while l�kke!

# I denne varianten så bruker vi et såkalt flagg for å styre hvorvidt programmet skal kjøre eller ikke

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)