#Input color
print("1. Red")
print("2. Green")
print("3. Yellow")
print("4. Purple")
print("5. Black")
print("6. White")

color_choice = int(input("Please input your number"))

if color_choice == 1:
    print("You choose red")
elif color_choice == 2:
    print("You choose green")
elif color_choice == 3:
    print("You choose Yellow")
elif color_choice == 4:
    print("You choose purple")
elif color_choice == 5:
    print("You choose black")
elif color_choice == 6:
    print("You choose white")
else:
    print("Wrong input")