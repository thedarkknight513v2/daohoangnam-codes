correct_username = "Dao Hoang Nam"
correct_password = "ilovefinance"

count = 0
loop = True

while loop:
    input_username = input("Please input username")
    if input_username == correct_username:
        input_password = input("Please input password")
        if input_password == correct_password:
            print("Welcome")
            break
        else:
            print("incorrect password")
    else:
        print("There is no such user")

    count += 1
    if count == 3:
        print("You fail to login 3 times")
        break
            
