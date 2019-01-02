# Test av bruk av lister
# Bygger først en liste fra bunnen
# Deretter slettes en plass

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')

print(motorcycles)

# Listen kan også bygges slik:
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati')
 
# POP kan hente enten siste verdi ved å ikke spesifisere noe: first_owned = motorcycles.pop()
# Eller man kan hente hvilken verdi som helst slik:
# first_owned = motorcycles.pop(0)
# print("The first motorcycle I owned was a " + first_owned.title() + ".")b

# Remove brukes hvis man ønsker å fjerne verdien, men ikke vet hvor i listen den verdien er. Remove fjerner bare den første gangen man finner verdien. Er den der flere ganger, må man bruke en loop for å identifisere alle.

# motorcycles.remove('ducati')
# print(motorcycles)

# Her bruker vi en variabel for å ta en remove, og så kan man bruke den variabelen for å fortelle hva man removet

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")