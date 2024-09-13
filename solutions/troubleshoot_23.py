"""
solutions/troubleshoot_23.py

Troubleshoot the issue 23: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""


def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except:
        return f"Something went wrong when trying to read {file_path}."


if __name__ == "__main__":
    # Doesn't handle errors that can occur trying to read the file
    print(read_file("non_existent_file.txt"))
