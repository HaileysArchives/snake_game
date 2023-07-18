# super()를 호출하는 것을 추천하지만 필수는 아닙니다. 

class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woorf!")

class Labrador(Dog):
    def __init__(self):
        self.temperament = "friendly"
