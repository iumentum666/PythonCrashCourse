# Denne koden demonstrerer hvordan man kan fjerne alle instanser av en verdi fra en liste

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)