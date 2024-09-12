"""
problems/troubleshoot_4.py

Troubleshoot the issue 4: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""

def concatenate_strings(str_list):
    result = ""
    for item in str_list:
        result += item
    return result

if __name__ == "__main__":
    strings = ["Hello", " ", "World", 123]
    print(concatenate_strings(strings))
