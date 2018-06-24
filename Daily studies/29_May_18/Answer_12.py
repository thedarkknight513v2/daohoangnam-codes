# ii.	Ask users to enter a number n, then print n x n 1’s and 0’s, consecutively

n = int(input("Please enter n"))

for i in range(1, n+1):
    for j in range(1,n+1):
        if (i+j) % 2 == 0:
            print("1", end ="\t")
        else:
            print("0", end="\t")
    print()