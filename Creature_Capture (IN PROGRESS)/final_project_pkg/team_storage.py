'''
Player Creature Storage and Starter Teams
by Tyler Varzeas
11/26/2022
'''


class Player_team:
    def __init__(self, max_creatures):
        self.max_creatures = max_creatures
        self.team = []

    def add_creature(self, creature):
        if len(self.team) < self.max_creatures:
            self.team.append(creature)
            return True
        return False

    def get_creatures(self, team):
        for creature in team:
            print(f"{creature.species}, {creature.level}")

    def is_creature_present(self, creature):
        if creature in self.team:
            print(f"Creature: {creature.species}, Level: {creature.level}")
        else:
            print("Creature not on team")

class Player_storage(Player_team):
    def __init__(self, max_creatures, box_number):
        super().__init__(max_creatures)
        self.max_creatures = max_creatures
        self.box_number = box_number
        self.storage = []