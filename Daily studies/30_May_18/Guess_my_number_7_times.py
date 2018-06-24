from random import randint
correct_number = randint(1,100)
print(correct_number)

playing = True
count =1
while playing:
        if count <= 7:
            guessed_number = int(input("Please input your guessed number"))
            if guessed_number == correct_number:
                print("Bingo")
                playing = False
            elif guessed_number > correct_number:
                print("Smaller")
            else:
                print("Bigger")
        else:
            print("You lose")
            playing = False
        count += 1