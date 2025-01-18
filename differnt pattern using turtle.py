from turtle import *

bgcolor("black")
speed(0)


for i in range(220):
    color("green")
    circle(i)
    color("blue")
    circle(i*0.5)
    right(3)
    forward(3)

done()