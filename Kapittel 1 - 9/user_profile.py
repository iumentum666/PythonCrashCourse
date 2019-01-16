# Eksempel på hvordan man kan lage en funksjon som godtar så mange argumenter man bare vil

def build_profile(first, last, **user_info): # To stjerner lager et tomt dictionary
    """
    Build a dictionary containing everything we know about a user.
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items(): # Looper igjennom og legger til verdiene med key i profilen
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)