# Her lister vi opp hvis folk har flere favorittspråk. Vi bruker en liste inne i en dictionary

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

# Når vi ønsker å printe alt dette, nester vi to for statements sammen

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + " Has only one favorite language: " + language.title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())