number = int(input("Please input number"))
is_prime = True

# Process
for i in range(2,number):
    if number % i == 0 :
        is_prime = False
        break

# Output
if is_prime == True:
    print("{0} is a prime number".format(number))
else:
    print("{0} is not a prime number".format(number))


