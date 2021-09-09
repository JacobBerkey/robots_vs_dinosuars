from robot import robot

class fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_one = robot("Chappie")
        robot_two = robot("Bender")
        robot_three = robot("WALL-E")

        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)