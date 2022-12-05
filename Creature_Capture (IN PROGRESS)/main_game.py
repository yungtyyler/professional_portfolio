'''
Creature Capture Main Game
by Tyler Varzeas
11/26/2022
'''

import random
import time
from final_project_pkg import creature_index
from final_project_pkg import team_storage


# Important variables

starter_emburn = creature_index.Emburn("emburn", 5)
starter_shorey = creature_index.Shorey("shorey", 5)
starter_seedoff = creature_index.Seedoff("seedoff", 5)
starter_list = [starter_emburn, starter_shorey, starter_seedoff]

player_team = team_storage.Player_team(6)

player_storage = team_storage.Player_storage(30, 1)

# Game functions


def wait_time(n):
    '''
    Delays the printing in the terminal by n seconds
    '''
    time.sleep(n)


def turn_action():
    '''
    #This will display and perform the actions available during a creature encounter

    while creature_hp > 0 or turn_over:
        turn_action = input(
            "What would you like to do?:\n1)   Attack\n2)   Catch\n3)   Run\n").lower()

        if turn_action == "1" or turn_action == "Attack":
            pass

        elif turn_action == "2" or turn_action == "catch":
            while True:
                catch_chance = random.randrange(1, 11)
                print(f"{player_name} throws an ion ring at {creature}!")

                for i in range(1, 4):
                    print(i)
                    time.sleep(1)

                if catch_chance > 5:
                    print(f"Nice! You caught {creature}!\n")
                    return
                else:
                    print(f"Shoot! {creature} got out!\n")
                    break

        elif turn_action == "3" or turn_action == "run":
            while True:
                run_success = random.randint(1, 6)
                if run_success < 2:
                    print("Oh no! The creature is blocking your path...\n")
                    break
                else:
                    print("You got away successfully\n")
                    return

        else:
            print("I'm sorry, I do not recognize that action. Try again\n")
    '''


def get_player_creature():
    '''
    Allows player to choose their creature at the start of the battle
    '''
    print(f"Who will {player_name} choose to battle?")

    for creature in player_team.team:
        print(creature.species.upper())

    player_creature = input("\n").lower()

    for creature in player_team.team:
        if player_creature == creature.species:
            player_creature = creature

    print(f"{player_name} has selected {player_creature.species.upper()} to battle!")
    return player_creature


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
        print("Great! Let me give you the breakdown then.")
        print(
            "Creatures are little things, some call them animals, some call them monsters.")
        print("I prefer their accepted term of creatures and nothing else.")
        print("A 'Capturer' like myself is one that is determined to index the characteristics, abilities, and demeanor of all creatures.")
        print("It is also important that Creature Capturers are always on the lookout for new Creatures to discover!")
        print("When a Capturer encounters a wild Creature, they're number one goal is capture that creature!")
        print("Some prefer to weaken the Creature through battle of their own Creatures they have captured in the past.")
        print(
            "And some prefer to try and capture the Creature through more delicate means.")
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
            player_team.team.append(starter_emburn)
            break

    elif starter_choice == "shorey":
        final_choice = input(
            f"You want {starter_choice.upper()}, are you sure? Y/N:    \n").lower()
        if final_choice == "y" or final_choice == "yes":
            print("Alright! That would have been my choice too.\n")
            player_team.team.append(starter_shorey)
            break

    elif starter_choice == "seedoff":
        final_choice = input(
            f"You want {starter_choice.upper()}, are you sure? Y/N:    \n").lower()
        if final_choice == "y" or final_choice == "yes":
            print("Alright! That would have been my choice too.\n")
            player_team.team.append(starter_seedoff)
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

    hermit_creature = random.choice([creature_index.Emburn(
        "emburn", 5), creature_index.Shorey("shorey", 5), creature_index.Seedoff("seedoff", 5)])

    wait_time(2)
    print(f"{hermit_creature.species.upper()} has appeared!")

    print(f"Level: {hermit_creature.level}\nHP: {hermit_creature.hp}\n")

    player_creature = get_player_creature()

    print(f"Okay {player_name}, here's how a battle works...\nFirst, you will choose a Creature to battle, as you already have.\nThen, you will be given a few options during the turn phase: Attack, Catch, and Run.\nAttack will allow you to cause damage to the opposing Creature. This can have its uses in either defeating your opponent, or weakening a creature to catch it.\nFor this battle, we will only focus on attacking!\n")

    def first_turn_action():
        '''
        This is the first turn action function for the initial battle with the hermit
        '''

        if (player_creature.type == "fire" and hermit_creature.type == "grass") or (player_creature.type == "water" and hermit_creature.type == "fire") or (player_creature.type == "grass" and hermit_creature.type == "water"):
            player_creature.attack += 2
        elif (player_creature.type == "fire" and hermit_creature.type == "water") or (player_creature.type == "water" and hermit_creature.type == "grass") or (player_creature.type == "grass" and hermit_creature.type == "fire"):
            hermit_creature.attack += 2

        while True:

            turn_action = input(
                "What would you like to do?:\n1)   Attack\n2)   Catch\n3)   Run\n").lower()

            if turn_action == "1" or turn_action == "Attack":

                while hermit_creature.hp > 0 or player_creature.hp > 0:
                    goes_first = random.choice(
                        [player_name, hermit_creature.species])
                    if goes_first == player_name:
                        print(f"{player_name} will go first!")
                    else:
                        print(
                            f"Hermit's {hermit_creature.species} will go first!")
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
                print(f"{player_name} wins the battle!")
                break
            if player_creature.hp <= 0:
                print("Tisk, Tisk... better luck next time!")
                print(f"{player_name} has lost the battle!")
                break

            elif turn_action == "2" or turn_action == "catch":
                print("Oh no! You don't have any ion rings to capture this creature.\n")
                wait_time(1)

            elif turn_action == "3" or turn_action == "run":
                print("This is what we came for! No turning back now. \n")
                wait_time(1)

    first_turn_action()
    break
