"""
solutions/troubleshoot_2.py

Troubleshoot the issue 2: (Intermediate - created by Generative AI)

Author: Nathan Lutala (nlutala)
"""

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        # The logic error lies here.
        # Num needs to be bigger than max_num for max_num to be updated to num
        # if num < max_num:
        if num > max_num:
            max_num = num
    return max_num

if __name__ == "__main__":
    numbers = [3, 5, 2, 8, 1]
    print("The maximum number is:", find_max(numbers))
