import turtle
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("white")
turtle_screen.title("Turtle python")

turtle_instance=turtle.Turtle()
turtle_instance.color("black")
turtle.speed(5)
turtle_colors=["red", "black", "blue", "grey", "purple"]
for i in range(10):
    turtle_instance.color(turtle_colors[i%5])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(i)

turtle.done()
