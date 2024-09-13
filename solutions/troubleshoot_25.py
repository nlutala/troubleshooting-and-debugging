"""
solutions/troubleshoot_25.py

Troubleshoot the issue 25: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""


def calculate_average(numbers):
    if len(numbers) == 0:
        raise AttributeError("No numbers were given.")

    total = sum(numbers)
    count = len(numbers)
    return total / count


if __name__ == "__main__":
    # Returns ZeroDivisionError because no numbers were given
    print(calculate_average([]))
