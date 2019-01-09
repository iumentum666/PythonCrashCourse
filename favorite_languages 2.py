favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# Nå looper vi igjennom alle som har registrert favorittspråk
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")