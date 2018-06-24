number = int(input("Please input the number"))
prime = True


for i in range(2,number):
    if number % i == 0:
        prime = False
        break

if prime == True:
    print(number," is a prime number")
else:
    print(number," is not a prime number")

    