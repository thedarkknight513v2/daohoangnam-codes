# Choose a breakfast item that will be served



meal_choice = int(input("Please choose a type of meal"))
print("1. Bread")
print("2.Pancakes")
print("3. Waffles")
print("4. Oatmeals")

# Declare the variables:
if meal_choice == 2:
    meal = "Pancakes"
if meal_choice == 3:
    meal = "Waffles"

# For bread:
if meal_choice == 1:
    print("You choose bread. Now what kind of bread do you want to serve:")
    bread_type = int(input("Choose a type of bread"))
    print("1. Wheat toast")
    print("2. Sour dough")
    print("3.Rye toast")
    print("4. Pancakes")

    if bread_type == 1:
        print("You choose wheat toast")
    elif bread_type == 2:
        print("You choose sour dough")
    elif bread_type == 3:
        print("You choose rye toast")
    elif bread_type == 4:
        print("You choose oatmeals")
    else:
        print("There is no such type of bread")

if meal_choice == 2 or meal_choice == 3:
    print("You choose ", meal)
    print("1. Syrup")
    print("2. Strawberries")
    print("3. Powdered sugar")
    toppings = int(input("Now choose a topping"))

    if toppings == 1:
        print("You choose ", meal, "with syrup")
    elif toppings == 2:
        print("You choose ",meal, "with strawberries")
    elif toppings == 3:
        print("You choose", meal, "with powdered sugar")
    else:
        print("There is no such kind of topping")

if meal_choice == 4:
    print("You choose oatmeals")

print("Thanks for coming")
