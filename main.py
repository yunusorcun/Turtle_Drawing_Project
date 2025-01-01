import turtle
#Examples of using the turtle package
drawing_board= turtle.Screen()
drawing_board.bgcolor("cyan3") #bgcolor arka plan rengini seçtiriyor
drawing_board.title("Python Turtle") #ekranın üstünde yazacak yazı.

'''
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance_2=turtle.Turtle()
turtle_instance_2.left(90)
turtle_instance_2.forward(100)
turtle_instance_2.right(90)
turtle_instance_2.forward(100)
'''
# it's second option and better than before .
'''
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)
   note: İf you want draw a star you need 5 sides and 145 angle.
'''

# Get number of sides from user
print("Please enter the number of sides: ")
num_sides = int(input("n="))

# Print number of sides
print(num_sides)

# Calculate angle and side length
angle = 360.0 / num_sides
side_length = 100

# Start Turtle module
turtle_instance = turtle.Turtle()

for i in range(num_sides):
    turtle_instance.left(angle)
    turtle_instance.forward(side_length)

# finish drawing
turtle.done()

