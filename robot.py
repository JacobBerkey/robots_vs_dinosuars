from weapon import weapon


class robot:
    def __init__(self, name):
        self.name = name
        self.health = 500
        self.weapon = [weapon("Blade Storm", attack_power= 60), weapon("Phantom", attack_power=40), weapon("Operator", attack_power=80)]



    def attack(self, dinosaur):
        pass