# i.	10 x 10 1’s and 0’s, consecutively

for i in range(1,10):
    for j in range(1,10):
        if (i +j)% 2==0:
            print("1", end="\t")
        else:
            print("0", end="\t")

    print()