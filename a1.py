import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(500, 500)
turtle.Screen().title("turtle")
polygon= turtle.Turtle()
side=6
len=100 
angle=360/side
for i in range(side):
    polygon.forward(len)
    polygon.right(angle)

turtle.done()