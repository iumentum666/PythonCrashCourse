# Denne viser hvordan continue f�r en while l�kke til � starte fra begynnelsen uten � eksekvere resten av koden i l�kken
# Siden vi bruker %, s� sjekker vi om tallet er partall eller ikke, og printer derfor bare oddetall
# Bruker vi % 2 != 0 s� printer vi bare partall

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)