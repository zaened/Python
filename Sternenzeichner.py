# author : Zäned Pasagad
# date : 27.07.2021

import turtle

window = turtle.Screen()
window.colormode(255)
window.bgcolor(0,255,125)
tess = turtle.Turtle()
tess.shape('turtle')
tess.color('blue')

for i in range(12):
    tess.penup()
    tess.forward(100)
    tess.pendown()
    tess.forward(30)
    tess.penup()
    tess.forward(15)
    tess.pendown()
    tess.stamp()
    tess.penup()
    tess.forward(-145)
    tess.right(30)
    
window.mainloop()
