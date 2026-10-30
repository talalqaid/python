# Exercise 6: Adaptation of the supplied koch.py.
# k changes recursion depth; size changes side length.
import turtle as t

k = 4
size = 400

t.hideturtle()
t.penup()
t.goto(-size / 2, size / 3)
t.pendown()
t.pensize(1)
t.speed(0)
t.tracer(0, 0)

def koch(prefractal, size):
    if prefractal == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(prefractal - 1, size / 3)
            t.left(angle)

# Three rotated copies form the Koch snowflake.
for side in range(3):
    koch(k, size)
    t.right(120)

t.update()
t.done()
