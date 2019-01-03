# Her lærer vi om tuples. Lister som ikke kan endres
dimensions =(200,50) # tuples defineres med parantes og ikke square brackets

# print(dimensions[0])
# print(dimensions[1])

# dimensions[0] = 250 # Dette vil feile... Man kan ikke endre enn tuple slik

# Man kan loope igjennom alle verdier i en tuple

for dimensions in dimensions:
    print(dimensions)

# Man kan ikke modifisere en tuple, men man kan assigne nye verdier til variabelen som inneholder tupelen. Så for å endre må vi redefinere hele greia

dimensions = (400, 100)
print("\nModifid dimensions:")
for dimensions in dimensions:
    print(dimensions)