# i.	1’s and 0’s, consecutively

n = int(input("Please input n"))

for i in range(1,n+1):
    if i % 2 == 0:
        print("0", end= " ")
    else:
        print("1", end=" ")

print()