'''
Index of Creatures
by Tyler Varzeas
11/26/2022
'''

class Creature:
    def __init__(self, species, level):
        self.species = species
        self.level = int(level)
        self.xp = 0
        self.xp_to_next_level = (self.level * 20)

    def get_species(self):
        return self.species

    def get_level(self):
        return self.level

    def level_up(self):
        self.xp = 0
        self.xp_to_next_level = (self.level * 20)
        self.level += 1

    def check_level_up(self, creature):
        if self.xp >= self.xp_to_next_level:
            self.level_up()
            print(f"Your {creature.species.upper()} has reached level {self.level}!")
            print(f"Level: {self.level} -- HP: {self.hp} -- Attack: {self.attack}")


class Emburn(Creature):
    
    def __init__(self, species, level):
        super().__init__(species, level)
        self.type = "fire"
        self.hp = (self.level * 4)
        self.attack = round(6 * (0.2 * self.level))

    def level_up(self):
        super().level_up()
        self.xp_to_next_level = (self.level * 20)
        self.hp = (self.level * 4)
        self.attack = round(6 * (0.2 * self.level))
        self.xp_to_next_level = (self.level * 20)


class Shorey(Creature):
    def __init__(self, species, level):
        super().__init__(species, level)
        self.type = "water"
        self.hp = round(self.level * 4.4)
        self.attack = round(5 * (0.2 * self.level))
    
    def level_up(self):
        super().level_up()
        self.xp_to_next_level = (self.level * 20)
        self.hp = round(self.level * 4.4)
        self.attack = round(5 * (0.2 * self.level))
        self.xp_to_next_level = (self.level * 20)


class Seedoff(Creature):
    def __init__(self, species, level):
        super().__init__(species, level)
        self.type = "grass"
        self.hp = (self.level * 5)
        self.attack = round(4 * (0.2 * self.level))
    
    def level_up(self):
        super().level_up()
        self.xp_to_next_level = (self.level * 20)
        self.hp = (self.level * 5)
        self.attack = round(4 * (0.2 * self.level))
        self.xp_to_next_level = (self.level * 20)


class Chirpsy(Creature):
    def __init__(self, species, level):
        super().__init__(species, level)
        self.type = "flying"
        self.hp = (self.level * 4)
        self.attack = round(3 * (0.2 * self.level))
    
    def level_up(self):
        super().level_up()
        self.xp_to_next_level = (self.level * 20)
        self.hp = (self.level * 4)
        self.attack = round(6 * (0.2 * self.level))
        self.attack = round(3 * (0.2 * self.level))
