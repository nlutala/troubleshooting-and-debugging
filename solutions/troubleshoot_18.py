"""
solutions/troubleshoot_18.py

Troubleshoot the issue 18: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""

if __name__ == "__main__":
    my_dict = {"a": 1, "b": 2, "c": 3}
    # print(my_dict["d"]) - This is used for assigning a value to the key "d"
    print(my_dict.get("d", "No key-value was found for 'd'."))
