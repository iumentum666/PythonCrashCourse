# Verdier fra input er alltid string. Så man må bruker int() for å gjøre det om til tall...

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")