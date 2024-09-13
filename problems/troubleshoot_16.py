"""
problems/troubleshoot_16.py

Troubleshoot the issue 16: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(-5))
