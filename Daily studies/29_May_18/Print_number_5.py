
# i.	Ask user to enter a number n, then print n x n numbers, following multiplication table pattern:

n = int(input("Please enter n"))

for i in range(1, n+1):
    for j in range(1,n+1):
        table = i * j
        print(table, end = "\t")
    print()