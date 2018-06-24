n = int(input("Please input n"))

# for i in range(n):
#     for j in range(n):
#         print(" ", end= "*")

#     print()


# # Solution
# for i in range (10):
#     for j in range(10):
#         if j <= 10 - i - 1:
#             print("  ", end="")
#         else:
#             print("* ", end="")

# #break
#     print() 

for i in range(n):
    for j in range(n):
        if j<= 10 - 1 - i:
            print(" ",end="")
        else:
            print("*",end="")
    print()