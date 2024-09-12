"""
solutions/troubleshoot_4.py

Troubleshoot the issue 4: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""

def concatenate_strings(str_list):
    result = ""
    for item in str_list:
        # result += item
        result += str(item)
    return result

if __name__ == "__main__":
    strings = ["Hello", " ", "World", 123]

    # The last element of the strings list is not a string, and will lead to a type
    # error of sorts.
    # The way to handle this is to ensure evering in the list is casted to a string
    # before appending it to the result
    print(concatenate_strings(strings))
