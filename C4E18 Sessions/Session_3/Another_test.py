

# list 
#Create
menu = ["Salad nga","My tom","Pho","So","Chocolate"]

#Read
#Separator
print(*menu, sep=",")

# 3 cach doc list

# menu.append("Banh muot")
print(*menu, sep=",")
print(len(menu))

first_item = menu[-1]
print(first_item)

for i in range(0,5):
    print(i+1, ".", menu[i], sep="")

for i in range(5):
    print("{0}. {1}".format(i+1, menu[i]))

#cach 2
print("*" * 20)
for index, item in enumerate(menu):
    print("{0}. {1}".format(index+ 1,item))

print("*" * 20)

for item in menu:  #cach 3
    print(item)

menu[2]="Cua"
print(*menu, sep=",")