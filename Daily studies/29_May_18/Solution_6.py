n = int(input("enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i*j < 10:
            print(i*j, end="   ")
        elif i*j <100:
            print(i*j, end="  ")
        else:
            print(i*j, end=" ")
    print()