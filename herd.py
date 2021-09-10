from dinosaur import dinosaur

class herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dinosaur_one = dinosaur("Littlefoot", attack_power=50)
        dinosaur_two = dinosaur("Ducky", attack_power=80)
        dinosaur_three = dinosaur("Sharp Tooth", attack_power=70)

        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)