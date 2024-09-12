"""
solutions/troubleshoot_6.py

Troubleshoot the issue 6: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""

class Person:
    # def __init__(self, name, age):
    def __init__(self, name, age, address=None):
        self.name = name
        self.age = age
        # Added address attribute
        self.address = None

def print_person_info(person):
    # We don't have an an address attribute... Maybe we can add a default address in the
    # person class?
    print(f"Name: {person.name}, Age: {person.age}, Address: {person.address}")

if __name__ == "__main__":
    p = Person("Alice", 30)
    print_person_info(p)
