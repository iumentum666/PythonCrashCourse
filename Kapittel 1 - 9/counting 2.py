# Denne viser hvordan continue får en while løkke til å starte fra begynnelsen uten å eksekvere resten av koden i løkken
# Siden vi bruker %, så sjekker vi om tallet er partall eller ikke, og printer derfor bare oddetall
# Bruker vi % 2 != 0 så printer vi bare partall

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)