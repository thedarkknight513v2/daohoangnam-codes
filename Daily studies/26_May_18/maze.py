# for importing turtle
from turtle import*
shape("turtle")
color("purple")
speed(-1)

#specify distance
distance = int(input("Please specify the distance"))

# specify the incremental movement
incremental_movement = int(input("Please specify the incremental movement"))

distance += incremental_movement

# turtle movement

for j in range(distance):
    left(90)
    forward(j)

mainloop()

