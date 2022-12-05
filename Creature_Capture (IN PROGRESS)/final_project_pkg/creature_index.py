'''
Index of Creatures
by Tyler Varzeas
11/26/2022
'''

class Creature:
    def __init__(self, species, level):
        self.species = species
        self.level = level

    def get_species(self):
        return self.species

    def get_level(self):
        return self.level


class Emburn(Creature):
    def __init__(self, species, level):
        super().__init__(species, level)
        self.type = "fire"
        self.hp = 4 * level
        self.attack = int(6 * (0.2 * level))


class Shorey(Creature):
    def __init__(self, species, level):
        super().__init__(species, level)
        self.type = "water"
        self.hp = 4.4 * level
        self.attack = int(5 * (0.2 * level))


class Seedoff(Creature):
    def __init__(self, species, level):
        super().__init__(species, level)
        self.type = "grass"
        self.hp = 5 * level
        self.attack = int(4 * (0.2 * level))


class Chirpsy(Creature):
    def __init__(self, species, level):
        super().__init__(species, level)
        self.type = "flying"
        self.hp = 4 * level
        self.attack = int(3 * (0.2 * level))