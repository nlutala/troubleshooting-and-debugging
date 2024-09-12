"""
troubleshoot_5.py

Troubleshoot the issue 5: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""

def get_element_at_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]
    print(get_element_at_index(my_list, 5))
    # my_list only has indicies in the range of 0-4.
    # We need to handle this exception, preferably in the get_element_at_index function
    # (we could return None)?
