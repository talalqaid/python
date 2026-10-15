# Exercise 5: Draw a regular polygon with n sides.
import turtle
sides = int(input('Enter the number of sides (3 or more): '))
while sides < 3:
    sides = int(input('Please enter at least 3 sides: '))
length = 100
angle = 360 / sides
for side in range(sides):
    turtle.forward(length)
    turtle.left(angle)
turtle.done()
