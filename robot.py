from weapon import weapon


class robot:
    def __init__(self, name):
        self.name = name
        self.health = 500
        self.weapon = [weapon("Blade Storm", 60), weapon("Phantom", 40), weapon("Operator", 80)]



    def attack(self, dinosaur):
        pass