unsorted_list = [1, 4, 3, 8, 10, 9, 12, 11, 2, 5, 7, 6]
sorted_list =[]


for i in range(len(0, unsorted_list)):
    min_number = min(unsorted_list)
    position = unsorted_list.index(min_number)
    del unsorted_list[position]
    sorted_list.append(min_number)

print(*sorted_list)