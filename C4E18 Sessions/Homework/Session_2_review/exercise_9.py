value = input("Type less than 6 characters: ")
letter_number =1

for Letter in value:
    print("Letter ", letter_number,"is ",Letter)
    letter_number +=1
    if letter_number > 6:
        print("The string is too long")
        break