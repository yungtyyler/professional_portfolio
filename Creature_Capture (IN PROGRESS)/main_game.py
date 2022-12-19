'''
Creature Capture Main Game
by Tyler Varzeas
11/26/2022
'''

import random
from time import sleep
from final_project_pkg import creature_index
from final_project_pkg import team_storage


# Important variables

starter_emburn = creature_index.Emburn("emburn", 5)
starter_shorey = creature_index.Shorey("shorey", 5)
starter_seedoff = creature_index.Seedoff("seedoff", 5)
starter_list = [starter_emburn, starter_shorey, starter_seedoff]

player_team = team_storage.Player_team(6)
player_creature_storage = team_storage.Player_creature_sanctuary(100)
player_inventory_storage = team_storage.Player_inventory(100)


# Game functions


def wait_time(n):
    '''
    Delays the printing in the terminal by n seconds
    '''
    sleep(n)


def turn_action():
    '''
    This will display and perform the actions available during a creature encounter
    '''

    # print("-" * 20)
    # print()
    # while creature_hp > 0 or turn_over:
    #     turn_action = input(
    #         "What would you like to do?:\n1)   Attack\n2)   Catch\n3)   Run\n").lower()

    #     if turn_action == "1" or turn_action == "Attack":
    #         pass

    #     elif turn_action == "2" or turn_action == "catch":
    #         while True:
    #             catch_chance = random.randrange(1, 11)
    #             print(f"{player_name} throws an ion ring at {creature}!")

    #             for i in range(1, 4):
    #                 print(i)
    #                 time.sleep(1)

    #             if catch_chance > 5:
    #                 print(f"Nice! You caught {creature}!\n")
    #                 return
    #             else:
    #                 print(f"Shoot! {creature} got out!\n")
    #                 break

    #     elif turn_action == "3" or turn_action == "run":
    #         while True:
    #             run_success = random.randint(1, 6)
    #             if run_success < 2:
    #                 print("Oh no! The creature is blocking your path...\n")
    #                 break
    #             else:
    #                 print("You got away successfully\n")
    #                 return

    #     else:
    #         print("I'm sorry, I do not recognize that action. Try again\n")


def get_player_creature():
    '''
    Allows player to choose their creature at the start of the battle
    '''
    print(f"Who will {player_name} choose to battle?")

    while True:
        counter = 1
        for creature in player_team.team:
            print(f"{counter}:  {creature.species.upper()}")
            counter += 1

        player_creature = input("\n").lower()

        for creature in player_team.team:
            if player_creature == creature.species:
                player_creature = creature
                print(
                    f"{player_name} has selected {player_creature.species.upper()} to battle!")
                print(
                    f"Level: {player_creature.level}\nHP: {player_creature.hp}\n")
                return player_creature

            else:
                print("I don't think you have that creature... \n")


def check_type_advantage(player, opponent):

    if (player == "fire" and opponent == "grass") or (player == "water" and opponent == "fire") or (player == "grass" and opponent == "water"):
        return True
    elif (player == "fire" and opponent == "water") or (player == "water" and opponent == "grass") or (player == "grass" and opponent == "fire"):
        return False


# Introduction
print("-" * 17)
print("Creature Capture!")
print("-" * 17)
print("by Tyler Varzeas")
print("-" * 17)
print("Welcome Traveler! \nDon't be alarmed, I'm simply a hermit looking for young talent to \ntake my place as the creature capturer of this town. \n")
player_name = input("Tell me traveler, what's your name:    ")
print("")
print(f"{player_name}! That's a good name, not one that I've ever heard at least.\n")

# Tutorial
while True:
    do_tutorial = input(
        f"So, {player_name}, are you familiar with Creatures? Y/N:  \n").lower()
    if do_tutorial == "no" or do_tutorial == "n":
        print("Great! Let me give you the breakdown then.\n")
        wait_time(2)
        print(
            "Creatures are little things, some call them animals, some call them monsters.")
        print("I prefer their accepted term of creatures and nothing else.\n")
        wait_time(5)
        print("A 'Capturer' like myself is one that is determined to index the characteristics, abilities, and demeanor of all creatures.")
        wait_time(3)
        print("It is also important that Creature Capturers are always on the lookout for new Creatures to discover!")
        wait_time(3)
        print("When a Capturer encounters a wild Creature, they're number one goal is capture that creature!")
        wait_time(3)
        print("Some prefer to weaken the Creature through battle of their own Creatures they have captured in the past.")
        print(
            "And some prefer to try and capture the Creature through more delicate means.\n")
        wait_time(2)
        break
    elif do_tutorial == "y" or do_tutorial == "yes":
        print("Good to know!")
        break
    else:
        print("Sorry youngster, I didn't quite catch that...")

print("Let's get on with things then shall we!\n")

while True:
    start_game = input(
        f"Okay {player_name}, time to choose. Are you ready to embark on this \njourney and become a Creature Capturer?: Y/N   \n").lower()
    if start_game == "y":
        print("Great! Let's get started. Time to get out there and capture your \nfirst Creature!\n")
        break
    else:
        print("Are you sure? It's the opportunity of a lifetime!\n")

print(f"The hermit and {player_name} leave town and venture into the nearby forest in search of {player_name}'s first Creature to capture.\n")


# Player Starter Pick
print("Now that we are out in the wilderness, before we get ambushed, I would like for you to select a creature of your choice from my special collection!\n")

while True:

    print("Each of these three creatures are a rare breed, so choose wisely!\n")

    for choice in starter_list:
        wait_time(0.5)
        print(choice.species.upper())

    starter_choice = input("\n").lower()

    if starter_choice == "emburn":
        final_choice = input(
            f"You want {starter_choice.upper()}, are you sure? Y/N:    \n").lower()
        if final_choice == "y" or final_choice == "yes":
            print("Alright! That would have been my choice too.\n")
            player_team.add_creature(starter_emburn)
            break

    elif starter_choice == "shorey":
        final_choice = input(
            f"You want {starter_choice.upper()}, are you sure? Y/N:    \n").lower()
        if final_choice == "y" or final_choice == "yes":
            print("Alright! That would have been my choice too.\n")
            player_team.add_creature(starter_shorey)
            break

    elif starter_choice == "seedoff":
        final_choice = input(
            f"You want {starter_choice.upper()}, are you sure? Y/N:    \n").lower()
        if final_choice == "y" or final_choice == "yes":
            print("Alright! That would have been my choice too.\n")
            player_team.add_creature(starter_seedoff)
            break


# More Story
wait_time(2)
print("As they begin to traverse deeper into the woods, they hear rustling in the nearby bushes.\n")
wait_time(2)
print("Then suddenly...\n")
wait_time(3)

# Hermit Battle
while True:

    print("-" * 20)
    print(f"Alright {player_name}, time to teach you how to battle!\n")

    if starter_emburn in player_team.team:
        hermit_creature = creature_index.Seedoff("seedoff", 5)
    elif starter_shorey in player_team.team:
        hermit_creature = creature_index.Emburn("emburn", 5)
    elif starter_seedoff in player_team.team:
        hermit_creature = creature_index.Shorey("shorey", 5)

    wait_time(2)
    print(f"{hermit_creature.species.upper()} has appeared!")

    print(f"Level: {hermit_creature.level}\nHP: {hermit_creature.hp}\n")

    player_creature = get_player_creature()

    print(f"Okay {player_name}, here's how a battle works...\nFirst, you will choose a Creature to battle, as you already have.\nThen, you will be given a few options during the turn phase: Attack, Catch, and Run.\nAttack will allow you to cause damage to the opposing Creature. This can have its uses in either defeating your opponent, or weakening a creature to catch it.\nFor this battle, we will only focus on attacking!\n")

    def first_battle_sequence():
        '''
        This is the first turn action function for the initial battle with the hermit
        '''

        player_type_advantage = check_type_advantage(
            player_creature.type, hermit_creature.type)
        if player_type_advantage:
            player_creature.attack += 2
        elif not player_type_advantage:
            hermit_creature.attack += 2

        while True:

            print("-" * 20)
            print()
            turn_action = input(
                "What would you like to do?:\n1)   Attack\n2)   Catch\n3)   Run\n").lower()

            if turn_action == "1" or turn_action == "attack":

                while hermit_creature.hp > 0 or player_creature.hp > 0:
                    goes_first = random.choice(
                        [player_name, hermit_creature.species])
                    if goes_first == player_name:
                        print(f"{player_name} will go first!\n")
                    else:
                        print(
                            f"Hermit's {hermit_creature.species.upper()} will go first!\n")
                    wait_time(2)

                    if goes_first == player_name:
                        hermit_creature.hp -= player_creature.attack
                        print(
                            f"{player_name}'s {player_creature.species.upper()} attacked Hermit's {hermit_creature.species.upper()} and caused {player_creature.attack} damage!")
                        if hermit_creature.hp <= 0:
                            break

                        player_creature.hp -= hermit_creature.attack
                        print(
                            f"Hermit's {hermit_creature.species.upper()} attacked {player_name}'s {player_creature.species.upper()} and caused {hermit_creature.attack} damage!")
                        if player_creature.hp <= 0:
                            break

                        print(
                            f"Hermit's {hermit_creature.species.upper()} HP: {hermit_creature.hp}\n{player_name}'s {player_creature.species.upper()} HP: {player_creature.hp}")
                        wait_time(2)
                        break

                    else:
                        player_creature.hp -= hermit_creature.attack
                        print(
                            f"Hermit's {hermit_creature.species.upper()} attacked {player_name}'s {player_creature.species.upper()} and caused {hermit_creature.attack} damage!")
                        if player_creature.hp <= 0:
                            break

                        hermit_creature.hp -= player_creature.attack
                        print(
                            f"{player_name}'s {player_creature.species.upper()} attacked Hermit's {hermit_creature.species.upper()} and caused {player_creature.attack} damage!")
                        if hermit_creature.hp <= 0:
                            break

                        print(
                            f"Hermit's {hermit_creature.species.upper()} HP: {hermit_creature.hp}\n{player_name}'s {player_creature.species.upper()} HP: {player_creature.hp}")
                        wait_time(2)
                        break

            if hermit_creature.hp <= 0:
                print("Great Gatsby! You defeated me! You really are special...")
                print(f"{player_name} wins the battle!\n")
                print(
                    f"{player_name}'s {player_creature.species.upper()} gained 100 XP")
                player_creature.xp += 100
                player_creature.check_level_up(player_creature)
                wait_time(3)
                break
            if player_creature.hp <= 0:
                print("Tisk, Tisk... better luck next time!")
                print(f"{player_name} has lost the battle!\n")
                break

            elif turn_action == "2" or turn_action == "catch":
                print("Oh no! You don't have any ion rings to capture this creature.\n")
                wait_time(1)

            elif turn_action == "3" or turn_action == "run":
                print("This is what we came for! No turning back now. \n")
                wait_time(1)

    first_battle_sequence()
    break
print(
    f"\nThat's what I'm talking about {player_name}! That's only half the battle though... get it?? HA!\n We still need to teach you how to capture a feral creature.")
print("When traversing through this world, you will occasionally run into these feral creatures, and if it appeals to you, you will have an attempt at capturing it.")
print("Let's go look for one now, I think I can see one just ahead!\n")

# Capturing creatures tutorial

while True:

    print("-" * 20)
    print(
        f"Alright {player_name}, time to capture your first feral Creature!\n")

    feral_creature = creature_index.Chirpsy("chirpsy", 5)

    wait_time(2)
    print(f"{feral_creature.species.upper()} has appeared!")
    print(f"Level: {feral_creature.level}\nHP: {feral_creature.hp}\n")

    player_creature = get_player_creature()

    print(f"Okay {player_name}, I'm going to give you some 'Ion Rings'!\nThese are the instruments necessary for capturing and taming feral creatures.\nNow give it a go! See how it works for yourself.\n")
    player_inventory_storage.add_item("Ion Ring", 5)

    def first_capture_sequence():
        '''
        This is the capture sequence function for the initial feral creature encounter.
        '''

        while True:

            captured = False

            print("-" * 20)
            print()
            turn_action = input(
                "What would you like to do?:\n1)   Attack\n2)   Catch\n3)   Run\n").lower()

            if turn_action == "1" or turn_action == "Attack":

                print(
                    "We already learned how to battle! Time to capture your first Creature on your own!")
                wait_time(1)

            elif turn_action == "2" or turn_action == "catch":

                if "Ion Ring" in player_inventory_storage.inventory:
                    while True:
                        catch_chance = random.randrange(1, 11)
                        print(
                            f"{player_name} throws an Ion Ring at {feral_creature.species.upper()}!")

                        for i in range(1, 4):
                            print(i)
                            wait_time(1)

                        if catch_chance > 5:
                            print(
                                f"Nice! You caught {feral_creature.species.upper()}!\n")
                            print(
                                f"Nice! You caught {feral_creature.species.upper()} was added to your starter team!\n")

                            print("Starter Team:")
                            for creature in player_team.team:
                                print(creature.species.upper())

                            player_team.add_creature(feral_creature)
                            captured = True
                            return captured
                        else:
                            print(
                                f"Shoot! {feral_creature.species.upper()} got out!\n")
                            break
                else:
                    print(
                        "It looks like you don't have any Ion Rings to capture this creature!\n")

            elif turn_action == "3" or turn_action == "run":
                print("This is what we came for! No turning back now. \n")
                wait_time(1)

            elif captured == True:
                break

    first_capture_sequence()
    break

# End of Tutorial Message
print(f"Wow {player_name}... you have learned how to battle with and capture creatures.\nNow it is time for you to start your own adventure!\nAll I ask is when you become the champion at the annual tournament,\nYou don't forget who taught you how to capture your first creature!\n")
wait_time(2)
print(
    f"I wish you the best {player_name} and maybe one day, our paths will cross again.\nBut until then, onward!")
wait_time(2)
print("YOU HAVE COMPLETED THE TUTORIAL FOR 'Creature Capture'!\n")
wait_time(2)
print("Thanks for playing!")
wait_time(2)
print("END")
quit()
