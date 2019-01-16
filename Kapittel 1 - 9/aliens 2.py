# her tester vi nesting. Vi putter dictionaries inn i en liste og viser de..
# I det første eksemplet genererte vi listen manuelt. Nå gjør vi det litt mer maskinelt

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Og så modifiserer vi de tre første. Slenger også på en ELIF som endrer gule til røde osv
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Shot the first 5 aliens
for alien in aliens[:5]:
    print(alien)

print("...")

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))