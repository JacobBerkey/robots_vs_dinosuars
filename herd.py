from dino import dino

class herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dinosaur_one = dino("Littlefoot")
        dinosaur_two = dino("Ducky")
        dinosaur_three = dino("Sharp Tooth")

        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)