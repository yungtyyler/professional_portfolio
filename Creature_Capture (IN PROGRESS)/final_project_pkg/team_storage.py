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
            print(f"{creature.species.upper()} has been added to the team!\n")
            return True
        else:
            Player_creature_sanctuary.storage.append(creature)
            print(f"{creature.species.upper()} has been added to your sanctuary!\n")
            return True

    def get_creatures(self):
        for creature in self.team:
            print(f"{creature.species}, {creature.level}")

    def is_creature_present(self, creature):
        if creature in self.team:
            print(f"Creature: {creature.species}, Level: {creature.level}")
        else:
            print("Creature not on team")

class Player_creature_sanctuary(Player_team):
    def __init__(self, max_creatures):
        super().__init__(max_creatures)
        self.max_creatures = max_creatures
        self.storage = []

class Player_inventory:
    def __init__(self, max_items):
        self.max_items = max_items
        self.inventory = []

    def add_item(self, item, quantity):
        if len(self.inventory) < self.max_items:
            for i in range(1, quantity + 1):
                self.inventory.append(item)
            if quantity == 1:
                print(f"1 {item} has been added to your inventory!\n")
                return True
            else:
                print(f"{quantity} {item}s have been added to your inventory!\n")
                return True

