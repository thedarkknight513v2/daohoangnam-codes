number = int(input("Please input a number from 1 -100"))

print("""Please enter 'c' if my guess is correct
        enter "l" if my guess is larger
        enter "s" if my guess is smaller
        """)

loop = True
low = 0
high = 100


while loop:
    mid = (low + high) // 2
    response = input("Is {0} the correct number?".format(mid))
    if response == "c":
        print("Bingo")
        break
    elif response == "l":
        low = mid
    elif response == "s":
        high = mid
    else:
        print("Ezzz")