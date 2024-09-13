"""
solutions/troubleshoot_20.py

Troubleshoot the issue 20: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says woof!")


if __name__ == "__main__":
    dog = Dog("Buddy")
    # dog.bark - bark is a method, not an attribute
    dog.bark()
