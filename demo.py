class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_hello(self):
        print(self.name + " says hello !")

    def old(self):
        print(self.name + " is " + str(self.age) + " years old.")
