one = int(input("Input a number from 1-10"))
# two = int(input("Input a number from 1-10"))

# if 0 < one <= 10:
#     if 0 < two <= 10:
#         print("Your number is", one * two)
#     else:
#         print("Incorrect second number")
# else:
#     print("Incorrect first number")

if 0 < one <= 10:
    two = int(input("Input second number"))
    if 0 < two <= 10:
        print("Your number is ", one * two)
    else:
        print("Invalid second number")

else:
    print("Invalid first number")