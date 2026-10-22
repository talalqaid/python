# Exercise 7: draw a user-specified number of random squares
import random
import turtle

def square(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

def main():
    number = int(input('How many squares should be drawn?'))
    turtle.hideturtle()
    turtle.speed(0)
    colors = ('red', 'blue', 'green', 'yellow', 'purple', 'orange')
    for _ in range(max(0, number)):
        width = random.randint(20, 120)
        x = random.randint(-250, 250 - width)
        y = random.randint(-180, 180 - width)
        square(x, y, width, random.choice(colors))
    turtle.done()
main()
