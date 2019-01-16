# Modulo operatoren deler et tall på et annet og gir deg det som er igjen... Man kan benytte dette f.eks. til å avgjøre om et tall er partall eller oddetall

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")