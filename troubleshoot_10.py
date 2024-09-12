"""
troubleshoot_10.py

Troubleshoot the issue 10: (created by Generative AI)

Author: Nathan Lutala (nlutala)
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

if __name__ == "__main__":
    dog = Dog("Buddy", "Golden Retriever")
    print(dog.speak()) # Dog doesn't implement speak yet. Let's change that.
