scores = [10, 13, -5, 4, 0, 9]
sorted_list =[]
length = len(scores)

for i in range(0,length):
    min_number = min(scores)
    position = scores.index(min_number)
    del scores[position]
    sorted_list.append(min_number)

print(sorted_list)



