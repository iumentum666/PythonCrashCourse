# Her mikser vi argumenter som bruker posisjon og de som er vilk�rlig p� antall...

def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    """
    print("\nMaking a " + str(size) + 
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')