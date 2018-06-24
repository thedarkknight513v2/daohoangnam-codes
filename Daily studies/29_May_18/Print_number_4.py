# i.	9 x 9 numbers (multiplication table)

for i in range(1,10):
    for j in range(1,10):
        table = i * j
        print(table, end = "\t")
    print()
