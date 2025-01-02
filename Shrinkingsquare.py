import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("yellow")
turtle_screen.title("Turtle Python")
turtle_instance =turtle.Turtle()
turtle_instance.color("blue")

def shrinkingsquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.right(90)
        size = size-7

shrinkingsquare(150)
shrinkingsquare(125)
shrinkingsquare(100)
shrinkingsquare(75)
shrinkingsquare(50)
turtle.done()