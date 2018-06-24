# Solution
print("Hi there is a superuser gateway")
count = 0

while True:
    user_name = input("Username")
    if user_name == "c4e":
        password = input("Password: ")
        if password == "codethechange":
            print("welcome")
            break
        else:
            print("password incorrect")
    else:
        print("You are not a superuser")     

    count += 1
    if count == 3:
        print("You failed to login 3 times, go away")
        break   
