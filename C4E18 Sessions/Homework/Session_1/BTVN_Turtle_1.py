# square in green

Number_of_line = int(input("Please input number of line"))
Length_of_line = int(input("Please input length of line"))
Degree = int(360 / Number_of_line)

from turtle import *
color("green")
fillcolor("yellow")
speed(-1)

begin_fill()

for i in range(Number_of_line):
    forward(Length_of_line)
    left(Degree)    
   
end_fill()

mainloop()
