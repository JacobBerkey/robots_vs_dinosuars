from herd import herd
from fleet import fleet
from robot import robot
from dino import dino



class battlefield:
    def __init__(self):
        self.game = self.run_game()


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
        self.selection = input("Choose your charater! Type 'dino' or 'robot'")
        if self.selection == "dino":
            dino_selection = input()



    def dino_turn(self, dinosaur):
        pass

    def robot_turn(self, robot):
        pass

    def show_dino_opponent_option(self):
        pass

    def show_robo_opponent_option(self):
        pass

    def display_winners(self):
        pass

