# Exercise 6: Draw 36 overlapping squares, or choose another count and colour.
import turtle
count = -1
while count <= 0:
    count = int(input('Enter a positive number of squares: '))
colour = input('Enter a colour name (e.g. black, blue, red): ').strip() or 'black'
turtle.speed(0)
turtle.pencolor(colour)
angle = 360 / count
for square in range(count):
    for side in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.left(angle)
turtle.done()
