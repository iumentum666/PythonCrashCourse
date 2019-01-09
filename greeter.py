# Det er viktig at man forteller brukeren hva man vil at brukeren skal skrive inn

name = input("Please enter your name: ")
print("Hello, " + name + "!")

# Man kan hvis man vil ha en lang tekst, lagre denne teksten i en variabel, og så bruke den mot input()

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")