# Draw multiple circles

n = int(input("Please input the number of circles"))
radius = int(input("Please input the radius"))

from turtle import*
shape("turtle")
color("green")
speed(-1)
fillcolor("yellow")

begin_fill()

# Drawing
for i in range(n):
    circle(radius)
    left(360- 360/n)

end_fill()

mainloop()
