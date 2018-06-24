# Draw a circle

radius = int(input("Please input the radius"))
from turtle import*
shape("turtle")
color("green")
speed(-1)
fillcolor("yellow")

begin_fill()
circle(radius)
end_fill()

mainloop()