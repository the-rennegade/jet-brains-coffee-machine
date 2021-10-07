class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, name):
        print(f'Hello, I am {name}!')

name_input = input()

person = Person(name_input)

person.greet(name_input)
