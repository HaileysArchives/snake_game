# Inheritance, slicing and finising the snake game.

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swin()
nemo.breathe()
print(nemo.num_eyes)

