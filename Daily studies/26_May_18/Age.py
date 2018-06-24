age = int(input("Please input your age"))

if age < 10:
    print("Baby")
elif (age >= 10) and (age <= 18):
    print("Teenager")
elif age == 24:
    print("Get married")
else:
    print("Beside the scope of this program")

print("Bye bye")