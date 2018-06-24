from turtle import*
color("green")
speed(-1)
shape("turtle")

# length = 5
# # length of maze
# # for i in range(0,400,5):
# length += 5 # length = length + 5

n = int(input("Please input n"))

# Draw the maze
for i in range(n):
    left(90)
    forward(i)

mainloop()