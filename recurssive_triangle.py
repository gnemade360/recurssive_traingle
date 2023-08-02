import turtle

def draw_triangle(side_length, depth):
    if depth == 0:
        for _ in range(3):
            turtle.forward(side_length)
            turtle.left(120)
    else:
        draw_triangle(side_length / 2, depth - 1)
        turtle.forward(side_length / 2)
        draw_triangle(side_length / 2, depth - 1)
        turtle.backward(side_length / 2)
        turtle.left(60)
        turtle.forward(side_length / 2)
        turtle.right(60)
        draw_triangle(side_length / 2, depth - 1)
        turtle.left(60)
        turtle.backward(side_length / 2)
        turtle.right(60)

def main():
    turtle.speed(0)  # Set the drawing speed (0 is the fastest)
    side_length = 300
    depth = 4
    draw_triangle(side_length, depth)
    turtle.done()

if __name__ == "__main__":
    main()
