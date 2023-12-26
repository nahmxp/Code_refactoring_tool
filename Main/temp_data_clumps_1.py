class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

def print_person_details(person):
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
    print(f"Address: {person.address}")

# Usage
person1 = Person("John Doe", 25, "123 Main St")
person2 = Person("Jane Smith", 30, "456 Oak St")

print_person_details(person1)
print_person_details(person2)
