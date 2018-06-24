from turtle import*
speed(-1)
shape("turtle")

length = int(input("Please input length"))

for i in range(3,7,1):
    if i % 2 == 0:
        color("green")
    else:
        color("red")
    for j in range(i):
        forward(length)
        left( 360/i )

mainloop()




