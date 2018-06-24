print("So canh trong hinh?")
so_canh = int(input("So canh trong hinh?"))
angle = int(360 / so_canh)
print(angle)

from turtle import *
shape("turtle")
color("red")
speed(-1)

for i in range (so_canh):
    forward(50)
    left(360 / so_canh)
   
mainloop()

