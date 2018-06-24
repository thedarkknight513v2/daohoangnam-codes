# import turtle

from turtle import *
shape("turtle")
color("green")

so_canh = int(input("So canh trong hinh?"))
degree = 360 / so_canh
print("degree = ", degree)

chieu_dai = int(input("chieu dai?"))
print(chieu_dai)

for i in range(so_canh):
    forward(chieu_dai)
    left(degree)





mainloop()