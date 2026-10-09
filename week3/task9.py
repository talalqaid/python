
# Exercise 9 - Hexagon Challenge

import turtle

side = float(input("Enter the side length: "))
thickness = int(input("Enter the pen thickness: "))
speed = int(input("Enter the animation speed (0-10): "))
colour = input("Enter the pen colour: ")

turtle.pensize(thickness)
turtle.speed(speed)
turtle.pencolor(colour)

for i in range(6):
    turtle.forward(side)
    turtle.left(60)

turtle.done()
