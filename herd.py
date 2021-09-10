from dinosaur import dinosaur

class herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dinosaur_one = dinosaur("Littlefoot")
        dinosaur_two = dinosaur("Ducky")
        dinosaur_three = dinosaur("Sharp Tooth")

        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)