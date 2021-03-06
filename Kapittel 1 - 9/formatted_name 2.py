# Her jobber vi med returnering av verdier fra funksjoner
# Samme eksempel som tidligere, men vi gj�r et argument valgfritt ved � sette det til slutt
# med en default verdi som er tom

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

print(get_formatted_name('john', 'hooker', 'lee'))