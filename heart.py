#heart

import turtle

#setting up the turtle environment

turtle.speed(1) #drawing speed, can be set to 0 for the fastest speed
turtle.bgcolor("black")  #background color
turtle.pensize(3)   #pen thickness

#defining the curved path of the heart
def func(): 
    for i in range(200):
        turtle.right(1) #rotate slightly to the right
        turtle.forward(1)   #move forward by 1 unit

#setting the pen color to red and the inside filling color to pink
turtle.color("red", "pink")
turtle.begin_fill()

#draw the heart shape
turtle.left(140)
turtle.forward(111.65)  #draw the first line of the heart
func() #left curve of the heart
turtle.left(120) 
func() #right curve of the heart
turtle.forward(111.65) #draw the second line of the heart
turtle.end_fill() #fill the heart with pink color
turtle.hideturtle() #hide the turtle cursor
turtle.done()
