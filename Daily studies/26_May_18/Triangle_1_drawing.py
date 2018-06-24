# # Solution
# for i in range (10):
#     for j in range(i):
#         print("* ", end="")

# #break
#     print()

n = int(input("Please input n"))
for i in range(n):
    for j in range(i):
        print("*",end="")
    
    print()