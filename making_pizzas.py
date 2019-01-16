# I dette eksemplet ligger funksjonene i filen pizza.py
# Vi importerer pizza.py og deretter kan vi kjøre funksjonene fra hovedkoden

import pizza
# alternativt kan vi skrive from pizza import make_pizza, da importerer vi bare den funksjonen. Da trenger vi ikke skrive pizza.make_pizza
# vi kan også skrive from pizza import make_pizza as mp, da trenger vi bare skrive mp
# man kan også importere hele modulen med alias, import pizza as p, da blir det p.make_pizza()
# Hvis man skriver from pizza import *, blir alt kopiert inn i programmet, da kan man bare skrive make_pizza()

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')