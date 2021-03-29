class Animal:
    def __init__(self):
        self.no_of_eyes = 2

    def breathe(self):
        print('Inhale , exhale')


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swin(self):
        print("Moving in  water")

    def breathe(self):
        super().breathe()
        print('We are doing this under water')


nemo = Fish()

nemo.swin()
nemo.breathe()
print(nemo.no_of_eyes)
