# import turtle
from turtle import *
shape("turtle")
color("blue")
speed(-1)

movement_length = int(input("Length of movement?"))
for i in range(4):
    forward(movement_length)
    left(90)



mainloop()