class Person:

    def __init__(self, name, age, address):
        _self_data_clump.name = name
        _self_data_clump.age = age
        _self_data_clump.address = address


def print_person_details(person):
    print(f'Name: {_person_data_clump.name}')
    print(f'Age: {_person_data_clump.age}')
    print(f'Address: {_person_data_clump.address}')


person1 = Person('John Doe', 25, '123 Main St')
person2 = Person('Jane Smith', 30, '456 Oak St')
print_person_details(person1)
print_person_details(person2)
