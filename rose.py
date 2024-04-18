from turtle import *
import colorsys
import math

speed(0.25)
bgcolor("black") 

# espirales
goto(0, -40)
h = 0

for i in range(16):#petalo
    for j in range(18):#rotacion
        c= colorsys.hsv_to_rgb(0.125 , 1, 1)
        color(c)
        rt(90)#derecha
        circle(150-j*6, 90)
        lt(90)#izquierda
        circle(150-j*6, 90)
        rt(180)#derecha
    circle(40, 24)
#central
color("black") 
shape("turtle")
fillcolor("brown")
phi = 137.508 * (math.pi/ 180.0)

for i in range (200):
    r = 4 * math.sqrt(i)
    theta = i*phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()

done()



