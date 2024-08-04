import turtle

def pythagoras_tree_recursion(turt:turtle.Turtle, level, branch_length=100, angle=45, width_factor=0.75):
    if level == 0:
        turt.fd(0)
    else:
        # Draw the main branch
        turt.forward(branch_length)
        turt.left(angle)

        # Recursive call for the right subtree
        pythagoras_tree_recursion(turt, level - 1, branch_length * width_factor, angle, width_factor)

        turt.right(2 * angle)

        # Recursive call for the left subtree
        pythagoras_tree_recursion(turt, level - 1, branch_length * width_factor, angle, width_factor)

        turt.left(angle)
        turt.backward(branch_length)

def init_pythagoras_tree(level=8):
    screen = turtle.Screen() # Create the screen.
    screen.setup(900, 800)   # Set Window size.
    turt = turtle.Turtle()
    turt.speed(0)
    # turt.bgcolor("white")
    turt.color("green")
    # turt.title("Pythagoras Tree Fractal")

    turt.left(90)
    turt.up()
    turt.backward(300)
    turt.down()

    pythagoras_tree_recursion(turt, level, 150, 45)

    turt.hideturtle()
    screen.exitonclick() # Exit scree

if __name__ == "__main__":
    init_pythagoras_tree()
