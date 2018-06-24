from turtle import*
shape("turtle")
color("green")
speed(-1)

length = int(input("Please input the length"))

for i in range(4):
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