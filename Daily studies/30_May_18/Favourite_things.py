# favourite_things = ["games", "music", "movies", "finance"]

# # new_thing = input("What do you want to add")

# # favourite_things.append(new_thing)
# # print(*favourite_things,sep=" ")
# # print(len(favourite_things))

# replace_position = int(input("Position you want to update"))
# replace_item = input("Your replacing favourite")
# favourite_things[replace_position]= replace_item
# print(favourite_things)

# for index, item in enumerate(favourite_things):
#     print("{0} . {1}".format(index,item))

favourite_things = ["Games", "Humour", "Finance", "Programming","Books"]

new_thing = input("What do you want to add")

favourite_things.append(new_thing)
print(*favourite_things, end=" ")
print(len(favourite_things))

replace_position = int(input("Which position you want to replace?"))
replace_item = input("What do you want to replace")
favourite_things[replace_position] = replace_item
print(favourite_things)

for index, item in enumerate(favourite_things):
    print("{} . {}".format(index,item))