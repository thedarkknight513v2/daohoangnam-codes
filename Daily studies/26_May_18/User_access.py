# # Solution1
# if username == "c4e":
#     if password == "code the change":
#         print("welcome")
#     else:
#         print("Wrong password")

# else:
#     print("No such user. Go away!")

# #Solution 2
# if username =="c4e" and password == "codthechange":
#     print("Welcome")
# elif username =="C4e" and password != "codethechange":
#     print("Wrong password")
# else:
#     print("Go away")


# Solution by Nam
# Define username & password

username = input("Please input username")
password = input("Please input password")

valid_username = "Dao Hoang Nam"
valid_password = "NathanDrake"

if username == valid_username:
    if password == valid_password:
        print("Welcome ",valid_username)
    else:
        print("Wrong password")
else: 
    print("No such user. Go away")

