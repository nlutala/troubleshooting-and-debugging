"""
problems/troubleshoot_22.py

Troubleshoot the issue 22: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.area)
