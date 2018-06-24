enter_list = input("Please enter your list, separated by space")
new_list = enter_list.strip().split(sep=" ")

# list ko ro sort chua
numbers =[]
# final list
sorted_list = []

length = len(new_list)

# chuyen list sang int
for item in new_list:
    numbers.append(int(item))

# Solution
print(numbers)
is_sorted = True
for i in range(len(numbers)-1):
    if numbers[i] > numbers[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("Your sequence is sorted")
else:
    print("Your sequence is not sorted")
    print()
    for j in range(0,len(numbers)):
        min_number = min(numbers)
        position = numbers.index(min_number)
        del numbers[position]
        sorted_list.append(min_number)
        
    print("After sorted: ",sorted_list)

