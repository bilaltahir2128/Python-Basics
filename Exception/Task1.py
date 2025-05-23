class Adult_Exception(Exception):
    def print_exp(self):
        print("The person is an adult.")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_minor_age(self):
        if int(self.age) > 18:
            raise Adult_Exception()
        else:
            return f"Age of person is: {self.age}"

    def display(self):
        try:
            print(self.get_minor_age())
        except Adult_Exception as e:
            e.print_exp()
        finally:
            print(f"Name of person is: {self.name}")

p1 = Person("Hafsa",18 )
p1.display()