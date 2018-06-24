print("Guess your number games")
input() 
# print()
print("""
All you have to do is answer to guess
'c' if my guess is correct
's' if my guess is smaller than your number
'l' if my guess is larger than your number
""")

correct_number = int(input("Enter your number"))

low = 0
high = 100

while True:
    mid = (low + high) // 2
    answer = input("Is {0} your number?".format(mid))
    if answer == "c":
        print("correct")
        break
    elif answer == "l":
        low = mid
    elif answer == "s":
        high = mid 
    else:
        print("Ezz")
    
  


    


