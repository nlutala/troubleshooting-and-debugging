"""
problems/troubleshoot_21.py

Troubleshoot the issue 21: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""


def find_max(numbers):
    max_num = None

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num


if __name__ == "__main__":
    print(find_max([3, 5, 7, 2, 8]))
