import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(500, 500)
turtle.Screen().title("Turtle")
polygon= turtle.Turtle()
side=0
while True:
    for i in range(6):
        polygon.forward(side+1)
        polygon.left(60)
        side=side-5
    side=side+1



