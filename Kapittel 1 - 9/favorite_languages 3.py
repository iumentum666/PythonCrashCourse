favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is" +
            favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Når man printer verdier fra et dictionary, kommer verdiene i tilfeldig rekkefølge... man kan bruke sorted for å fikse dette

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Vi kan også printe bare verdiene uten key fra et dictionary

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# problemet i denne rutinen, er at den bare lister opp, så man får dobbelt. Man kan bruke SET funksjonen for å sjekke om noe er unikt

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())