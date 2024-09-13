"""
problems/troubleshoot_23.py

Troubleshoot the issue 23: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


if __name__ == "__main__":
    print(read_file("non_existent_file.txt"))
