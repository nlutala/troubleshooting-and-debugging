"""
solutions/troubleshoot_24.py

Troubleshoot the issue 24: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""


def fibonacci(n):
    if n < 0:
        raise ValueError(
            f"Negative number {n} was given. Only positive numbers are accepted."
        )

    # if n <= 0: - needs to be explicitly 0.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(10))
