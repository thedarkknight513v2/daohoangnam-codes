n = int(input("enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        a = i+j
        if a%2 != 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()