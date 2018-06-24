# draw an equilateral triangle

from turtle import*
shape("turtle")
color("green")
speed(-1)
fillcolor("yellow")

begin_fill()

length = int(input("Please input the length"))

for i in range(3):
    forward(length)
    left(120)

end_fill()

mainloop()