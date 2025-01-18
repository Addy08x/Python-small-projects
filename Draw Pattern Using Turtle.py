import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('black')
t.speed(0)

n=36
h=80

for i in range (50):
    c=colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.color(c)
    t.lt(145)
    for j in range(5):
        t.fd(300)
        t.left(150)
