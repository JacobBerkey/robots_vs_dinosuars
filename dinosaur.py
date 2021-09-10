from fleet import fleet
from herd import herd


class dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 500

    def attack(self, robot):
        self.robots = fleet()
        for robot in self.robots.robots:
            print(f"{robot.health}")

        self.dinosaurs = herd()
        for dinosaur in self.dinosaurs.dinosaurs:
                print("Name:"f"{dinosaur.name}")
                print("Attack Power:"f"{dinosaur.attack_power}")

        
        self.input = input("Type 'attack' to damage opponent")
        if self.input == "attack":
            print("You attacked:" f"{robot.name}" "for" f"{dinosaur.attack_power}""Damage!")
            print(f"{robot.health}" - f"{dinosaur.attack_power}")


        
        


