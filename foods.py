# Kopiering av lister
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:] # kopierer listen. Hvis man ikke bruker slicing, så vil de to variablene kobles sammen, og ikke kopieres.

# legger til unike ting i de to listene
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
