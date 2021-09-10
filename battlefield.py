from herd import herd
from fleet import fleet
from robot import robot
from dinosaur import dinosaur



class battlefield:
    def __init__(self):
        self.run_game()
        self.battle()
        self.dino_turn()
        self.robot_turn()
        self.display_winners()
        


    def run_game(self):
        self.input = input("Please Type 'on' to start game")
        if self.input != 'on':
            self.input
        if self.input == 'on':
            self.display_welcome()
    
    def display_welcome(self):
        print("Welcome to Robots Vs. Dinosaurs!!")
        self.battle()

    def battle(self):
        self.dinosaurs = herd()
        self.robots = fleet()
        self.input = input("Choose 'Dinosaurs' or 'Robots'")
        if self.input == "Dinosaurs":
            herd()
            for dinosaur in self.dinosaurs.dinosaurs:
                print("Name:"f"{dinosaur.name}")
                print("Attack Power:"f"{dinosaur.attack_power}")
                print("Health:"f"{dinosaur.health}")
                self.show_dino_opponent_option()

        if self.input != "Dinosaurs":
            fleet()
            for robot in self.robots.robots:
                print("Name:"f"{robot.name}")
                print("Weapon Name:"f"{robot.weapon.name}")
                print("Weapon Damage:"f"{robot.weapon.attack_power}")
                print("Health:"f"{robot.health}")
                self.show_robo_opponent_option()


    def dino_turn(self, Dinosaur):
       Dinosaur = Dinosaur
       dinosaur()

    def robot_turn(self, Robot):
        Robot = Robot
        robot()

    def show_dino_opponent_option(self):
        for robot in self.robots.robots:
            print("Name:"f"{robot.name}")
            print("Weapon Name:"f"{robot.weapon.name}")
            print("Weapon Damage:"f"{robot.weapon.attack_power}")
            print("Health:"f"{robot.health}")
        
    def show_robo_opponent_option(self):
        for dinosaur in self.dinosaurs.dinosaurs:
            print("Name:"f"{dinosaur.name}")
            print("Attack Power:"f"{dinosaur.attack_power}")
            print("Health:"f"{dinosaur.health}")


    def display_winners(self):
        for dinosaur in self.dinosaurs.dinosaurs:
            if dinosaur.health == 0:
                print("Robots Win!!!")

        for robot in self.robots.robots:
            if robot.health == 0:
                print("Dinosaurs Win")

