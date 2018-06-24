from random import randint

correct_number = randint(0,100)
# print(correct_number)

playing = True

while playing:
    guessed_number = int(input("Please input your number"))
    if correct_number == guessed_number:
        print("Correct")
        playing = False
    elif correct_number < guessed_number:
        print("Smaller")
    else:
        print("Bigger")