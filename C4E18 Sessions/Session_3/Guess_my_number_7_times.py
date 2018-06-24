from random import randint
correct_number = randint(0,100)
# print(correct_number)
playing = True
count = 0

while playing:
    
    if count >= 7:
        print('You lose')
        playing = False
    else:
        guessed_number = int(input("Please input your number"))
        if correct_number == guessed_number:
            print("Correct")
        elif correct_number < guessed_number:
            print("Smaller")
        else:
            print("Bigger")
    
    count += 1