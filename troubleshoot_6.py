class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def print_person_info(person):
    print(f"Name: {person.name}, Age: {person.age}, Address: {person.address}")

if __name__ == "__main__":
    p = Person("Alice", 30)
    print_person_info(p)
