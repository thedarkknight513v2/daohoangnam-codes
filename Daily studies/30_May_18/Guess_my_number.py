from random import randint

correct_number =randint(1,100)
print(correct_number)

while True:
    guessed_number = int(input("Please input your guest number"))
    if guessed_number == correct_number:
        print("Bingo")
        break
    elif guessed_number < correct_number:
        print("Bigger")
    else:
        print("Smaller")