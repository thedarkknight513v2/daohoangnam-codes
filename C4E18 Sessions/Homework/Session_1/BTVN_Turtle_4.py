#Draw multiple circle

Number_of_circle = int(input("Please input number of circles"))
Degree = int(360/Number_of_circle)

from turtle import *
color("green")
speed(-1)

for i in range(Number_of_circle):
    circle(50,None,None)
    left(Degree)

mainloop()


