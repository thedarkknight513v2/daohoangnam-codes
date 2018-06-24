# from turtle import *

# color("red")
# speed(-1)

# for i in range(1):
#     left(15)
#     forward(50)
#     right(30)
#     forward(50)
#     right(150)
#     forward(50)
#     right(30)
#     forward(50)
#     # left(15)
    
#     # left(90)


# mainloop()

from turtle import *

for i in range(3,7,1):
    if i % 2 == 0:
        color("red")
    else:
        color("green")
    for j in range(i):
        forward(50)
        left(360/i)

mainloop()