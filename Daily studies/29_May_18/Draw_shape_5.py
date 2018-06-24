# Draw shapes

from turtle import*
speed(-1)
shape("turtle")
color("green")

# Hinh thoi co 2 goc 30' 
x = 100
y = x * (3 ** (0.5))
z = 2 * x

length = int(input("Please input the length"))

# for i in range(4):
#     left(30)
for j in range(4):
    left(30)
    forward(length)
    right(60)
    forward(length)
    right(120)
    forward(length)
    right(60)
    forward(length)
    left(30)
    left(90)




mainloop()

