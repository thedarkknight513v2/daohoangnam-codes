unsorted_list = input("Please input your list")
new_list_in_str = unsorted_list.strip().split()
new_list_in_int = []
sorted_list = []

for item in new_list_in_str:
    new_list_in_int.append(int(item))
print(min(new_list_in_int))

print("*"* 20)
length = len(new_list_in_int)

# print(new_list_in_int)
# print(min(new_list_in_int))


is_sorted = True
for i in range(1,length):
    if new_list_in_int[i-1] > new_list_in_int[i]:
        is_sorted = False


if is_sorted:
    print("Your list is already sorted")
else:
    print("Your list is not sorted yet")
    for j in range(length):
        min_number = min(new_list_in_int)
        print(min_number)
        position = new_list_in_int.index(min_number)
        del new_list_in_int[position]
        sorted_list.append(min_number)

print(sorted_list)
