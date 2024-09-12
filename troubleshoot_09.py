"""
troubleshoot_9.py

Troubleshoot the issue 9: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""

def calculate_area(radius):
    if radius < 0:
        raise ValueError("Negative radius given.")
    pi = 3.14
    area = pi * radius ** 2
    return area

if __name__ == "__main__":
    print("Area of circle:", calculate_area(5))
    print("Area of circle:", calculate_area(-3))
    # The error here is that we're not handling a negative radius which shouldn't be
    # allowed.
