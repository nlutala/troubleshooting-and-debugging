"""
solutions/troubleshoot_3.py

Troubleshoot the issue 3: (Advanced - created by Generative AI)

Author: Nathan Lutala (nlutala)
"""

def divide(a, b):
    return a / b


if __name__ == "__main__":
    try:
        result = divide(10, 0)
        print("Result:", result)
    # It might be making the exception more specific?
    # except Exception as e:
    except ZeroDivisionError as e:
        print("Error:", e)
