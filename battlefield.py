from herd import herd
from fleet import fleet
from robot import robot
from dinosaur import dinosaur



class battlefield:
    def __init__(self):
        self.run_game()
        self.show_dino_opponent_option()
        self.dinosaurs = herd()



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
        pass

    def dino_turn(self, dinosaur):
        pass

    def robot_turn(self, robot):
        pass

    def show_dino_opponent_option(self):
        for dinosaur in self.dinosaurs.dinosaurs:
            print(f"{dinosaur.health}")

    def show_robo_opponent_option(self):
        for robot in self.robot.robot:
            print(f"{robot.weapons}")

    def display_winners(self):
        pass

