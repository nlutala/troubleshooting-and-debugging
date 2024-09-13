"""
solutions/troubleshoot_16.py

Troubleshoot the issue 16: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""


def factorial(n):
    if n < 0:
        raise ValueError(
            f"Negative number {n} was given. Only positive numbers are accepted."
        )

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    # factorial needs a positive integer
    print(factorial(-5))
