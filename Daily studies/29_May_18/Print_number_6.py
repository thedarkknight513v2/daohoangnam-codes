# i.	10 x 10 1’s and 0’s, consecutively

n = int(input("Please input n"))

for i in range(1,n):
    for j in range(1,n):
        if j % 2 == 0:
            print("0", end = "\t")
        else:
            print("1", end ="\t")
    print()
        

