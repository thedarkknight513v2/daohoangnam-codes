from turtle import*
shape("turtle")
speed(-1)

length = int(input("Please input length"))

for i in range(3,7,1):
    if i % 2 ==0:
        color("red")
    else:
        color("blue")
    for j in range(i):
        forward(length)
        left(360/i)

mainloop()