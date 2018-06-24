yob = int(input("Please input YoB"))
age = 2018 - yob

# print(age) 

if age < 10: 
    print("baby")
elif age <= 18:
    print("Teenager")
elif age == 24:
    print("Lay chong thoi")
else:
    print("not baby")

print("bye")
