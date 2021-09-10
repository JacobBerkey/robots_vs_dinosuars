from weapon import weapon
from herd import herd
from fleet import fleet


class robot:
    def __init__(self, name):
        self.name = name
        self.health = 500
        self.weapon = weapon("Blade Storm", attack_power= 60)



    def attack(self, dinosaur):
        self.dinosaurs = herd()
        for dinosaur in self.dinosaurs.dinosaurs:
            print(f"{dinosaur.name}")
            print(f"{dinosaur.attack_power}")

        self.robots = fleet()
        for robot in self.robots.robots:
            print("Name:"f"{robot.name}")
            print("Weapon Name:"f"{robot.weapon.name}")
            print("Weapon Power:"f"{robot.weapon.attack_power}")

            print("You attacked:" f"{dinosaur.name}" "for" f"{robot.weapon.attack_power}""Damage!")
            self.input = input("Type 'attack' to damage opponent")
        if self.input == "attack":
            print("You attacked:" f"{dinosaur.name}" "for" f"{robot.weapon.attack_power}""Damage!")
            print(f"{dinosaur.health}" - f"{robot.weapon.attack_power}")
