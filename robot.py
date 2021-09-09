from weapon import weapon


class robot:
    def __init__(self, name):
        self.name = name
        self.health = 500
        self.weapon = weapon

    def attack(self, dinosaur):
        pass   