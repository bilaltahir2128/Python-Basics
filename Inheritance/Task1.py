class Animal:
    def __init__(self, habitat="Unknown"):
        self.habitat = habitat

    def print_habitat(self):
        print(f"Habitat: {self.habitat}")
    
    def sound(self):
        print("Some animals make sounds.")

class Dog(Animal):
    def __init__(self, habitat="Backyard", sound="Woof woof!"):
        super().__init__(habitat)
        self.sound_effect = sound

    def sound(self):
        print(self.sound_effect)


x = Dog(habitat="Park", sound="Bark bark!")
x.print_habitat()
x.sound()