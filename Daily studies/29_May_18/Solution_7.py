for i in range(1,11):
    for j in range(1,11):
        a = i+j
        if a%2 != 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()