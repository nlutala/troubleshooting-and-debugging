"""
problems/troubleshoot_3.py

Troubleshoot the issue 3: (Advanced - created by Generative AI)

Author: Nathan Lutala (nlutala)
"""

def divide(a, b):
    return a / b


if __name__ == "__main__":
    try:
        result = divide(10, 0)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
