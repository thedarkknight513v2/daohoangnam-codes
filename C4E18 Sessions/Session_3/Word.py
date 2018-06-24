from random import choice

word = "champion"

characters = list(word)
print(characters)
print(choice(characters)) # dung vong lap lay chu cai ra cho vao list moi


for i in range(len(word)):
    print(choice(word), end =" ")
