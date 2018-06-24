# i.	1’s and 0’s, consecutively

n = int(input("Please input n"))
# half_n = int(n/2)

for i in range(n+1):
    if i % 2 ==0:
        print("1", end =" ")
    else:
        print("0", end =" ")


