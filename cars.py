cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Her er den orginale listen:")
print(cars)

# Sort funksjonaliteten sorterer i dette tilfellet alle bilene i alfabetisk rekkefølge
# cars.sort()
# print(cars)

# Sorterting av lister med sorted() funksjonen
# print("\nHer er den sorterte listen:")
# print(sorted(cars))
# print("\nHer er den orginale listen igjen:")
# print(cars)

# Og her reverserer vi rekkefølgen på listen. Denne endringen er permanent, men man kan få den orginale listen tilbake ved å gjøre det en gang til
# cars.reverse()
# print(cars)

# man finner lengden på lister ved å skrive len(cars). Den starter tellingen på 1
# print(len(cars))

# Indexfeil får man når man forsøker å hente ting fra listen som er utenfor rangen
# print(cars[4])

# Hvis man ønsker siste itemet i en liste, kan man alltid bruke -1
print(cars[-1])

# Dette feiler dog hvis  listen er tom...