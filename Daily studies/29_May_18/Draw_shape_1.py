# Draw a square
from turtle import*
shape("turtle")
color("green")
fillcolor("yellow")

length = int(input("Please input length of square"))

begin_fill()
for i in range(4):
    forward(length)
    left(90)

end_fill()

mainloop()