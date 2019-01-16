squares = [] #definerer en liste
for value in range(1,11): # alle tall fra 1 til 10
    square = value**2 # ta kvadratet av tallet fra verdien
    squares.append(square) # legg til i listen
    # squares.append(value**2) # Forenklet variant
    
print(squares)