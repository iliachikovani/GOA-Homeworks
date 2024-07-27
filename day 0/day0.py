from turtle import *

#we want to paint a house

#step 1: draw a square
speed(1)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door


forward(70)
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)


penup()
goto(200, 200)
pendown()
begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
goto(0,130)
pendown()
color("blue")
left(120)
forward(60)
left(90)
forward(65)

left(90)
forward(60)
left(90)
forward(65)

left(90)
forward(32.5)

left(90)
forward(65)

right(90)

forward(29)
right(90)

forward(30)

right(90)
forward(64)


exitonclick()