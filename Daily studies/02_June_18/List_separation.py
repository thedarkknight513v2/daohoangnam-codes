# enter_list = input("Please enter your list, separated by space")
# new_list = enter_list.strip().split(sep=" ")

# # list ko ro sort chua
# numbers =[]
# # final list
# sorted_list = []

# length = len(new_list)

# # chuyen list sang int
# for item in new_list:
#     numbers.append(int(item))

# # Solution
# print(numbers)
# is_sorted = True
# for i in range(len(numbers)-1):
#     if numbers[i] > numbers[i+1]:
#         is_sorted = False
#         break

# if is_sorted:
#     print("Your sequence is sorted")
# else:
#     print("Your sequence is not sorted")
#     print()
#     for j in range(0,len(numbers)):
#         min_number = min(numbers)
#         position = numbers.index(min_number)
#         del numbers[position]
#         sorted_list.append(min_number)
        
    # print("After sorted: ",sorted_list)


# unsorted_list = input("Please input your list")
# new_list_str = unsorted_list.split(sep=" ")
# new_list_int = []
# sorted_list = []

# for item in new_list_str:
#     new_list_int.append(int(item))

# # print(new_list_int)
# # print(min(new_list_int))

# # is_sorted = True
# length = len(new_list_int)

# for i in range(1,length-1):
#     if new_list_int[i-1] < new_list_int[i]:
#         print("Your list is already sorted")
#         break
#     else:
#         print("Your list is not sorted yet")
#         for j in range(length -1):
#             min_number = min(new_list_int)
#             sorted_list.append(min_number)
#             position = new_list_int.index(min_number)
#             del new_list_int[position]
#         print(sorted_list)

