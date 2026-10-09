import turtle

screen = turtle.Screen()

width = screen.window_width()
height = screen.window_height()

print("Width:", width)
print("Height:", height)

print("Min X:", -width / 2)
print("Max X:", width / 2)
print("Min Y:", -height / 2)
print("Max Y:", height / 2)

turtle.done()