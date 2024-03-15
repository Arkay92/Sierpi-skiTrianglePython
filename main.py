import turtle

# Function to draw a Sierpiński triangle
def draw_sierpinski(length, depth):
    if depth == 0:
        # Draw an equilateral triangle
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        # Recursively draw three smaller Sierpiński triangles
        draw_sierpinski(length/2, depth-1)
        turtle.forward(length/2)
        draw_sierpinski(length/2, depth-1)
        turtle.backward(length/2)
        turtle.left(60)
        turtle.forward(length/2)
        turtle.right(60)
        draw_sierpinski(length/2, depth-1)
        turtle.left(60)
        turtle.backward(length/2)
        turtle.right(60)

# Setup turtle environment
turtle.speed(0)
turtle.up()
turtle.goto(-200, -150)
turtle.down()

# Set the depth of the recursion
depth = 4  # You can change this to make the triangle more or less detailed

# Start drawing
draw_sierpinski(400, depth)

# Hide the turtle and display the drawing
turtle.hideturtle()
turtle.done()
