# Her l�rer vi � sende informasjon til en funksjon
# variabelen vi sender til funksjonen kalles en parameter
# Verdien av variabelen n�r vi sender til den kalles argument


def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')