# Exercise 8: random turtle walk
import random
import turtle

def main():
    steps = int(input('How many steps should the walker take? '))
    walker = turtle.Turtle()
    walker.speed(4)
    for _ in range(max(0, steps)):
        walker.setheading(random.randint(0, 359))
        walker.forward(random.randint(10, 20))
    turtle.done()
main()
