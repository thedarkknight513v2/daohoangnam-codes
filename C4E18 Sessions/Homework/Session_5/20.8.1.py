alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q","r", "s", "t", "u", "v", "w", "x", "y", "z"]
string_input = input("Please enter your string")
alphabet_length = len(alphabet)

list_1 = []
count = 0
loop = True

for i in string_input:
    j = i.replace(" ","")
    list_1.append(j)


# list_2 = set(list_1)
print(list_1)
length = len(list_1)


    
for v in range(alphabet_length):
    word_to_count = alphabet[v]
    for i in range(length):
        if list_1[i] == word_to_count:
            count += 1
    print(word_to_count, count)



#_______________
# number =[1, 6, 8, 1, 2, 1, 5, 6]
# length = len(number)

# number_to_count = int(input("Enter a number"))

# loop = True
# count = 0

# while True:
#     for i in range(length):
#         if number[i] == number_to_count:
#             count += 1
#     break
# print("{0} appears {1} times in my list".format(number_to_count,count))
   



    



