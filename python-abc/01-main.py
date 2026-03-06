#!/usr/bin/python3
""" Main file for duck typing demonstration """

from task_01_duck_typing import Circle, Rectangle, shape_info


if __name__ == "__main__":
    # Create a circle with radius 5
    circle = Circle(5)
    print("Circle with radius 5:")
    shape_info(circle)
    print()

    # Create a rectangle with width 4 and height 6
    rectangle = Rectangle(4, 6)
    print("Rectangle with width 4 and height 6:")
    shape_info(rectangle)
