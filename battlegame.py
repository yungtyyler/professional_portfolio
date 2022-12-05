wizard_dictionary = {"name": "Wizard", "hp": 70, "damage": 150}
elf_dictionary = {"name": "Elf", "hp": 100, "damage": 100}
human_dictionary = {"name": "Human", "hp": 150, "damage": 20}
orc_dictionary = {"name": "Orc", "hp": 200, "damage": 75}
dragon_dictionary = {"name": "Dragon", "hp": 300, "damage": 50}
secret_dictionary = {"name": "Dragon Slayer", "hp": 20000, "damage": 300}

player = ""
playGame = True


def end_game():
    print("Thanks for Playing!")
    exit()


counter = 1

while playGame:

    while True:
        if counter == 1:
            print("Dragon Battle Game")
            print("-" * 20)
            print("(1)  " + wizard_dictionary["name"])
            print("(2)  " + elf_dictionary["name"])
            print("(3)  " + human_dictionary["name"])
            print("(4)  " + orc_dictionary["name"])
            print("(5)  Exit Game")
            print("-" * 20)
        elif counter > 1:
            print("Dragon Battle Game")
            print("-" * 20)
            print("(1)  " + wizard_dictionary["name"])
            print("(2)  " + elf_dictionary["name"])
            print("(3)  " + human_dictionary["name"])
            print("(4)  " + orc_dictionary["name"])
            print("(5)  Exit Game")
            print("(6)  Secret option??")
            print("-" * 20)

        character = input("Choose your Champion: ").lower()
        print("")

        if character == "1" or character == "wizard":
            player = wizard_dictionary["name"]
            my_hp = wizard_dictionary["hp"]
            my_damage = wizard_dictionary["damage"]
            break
        elif character == "2" or character == "elf":
            player = elf_dictionary["name"]
            my_hp = elf_dictionary["hp"]
            my_damage = elf_dictionary["damage"]
            break
        elif character == "3" or character == "human":
            player = human_dictionary["name"]
            my_hp = human_dictionary["hp"]
            my_damage = human_dictionary["damage"]
            break
        elif character == "4" or character == "orc":
            player = orc_dictionary["name"]
            my_hp = orc_dictionary["hp"]
            my_damage = orc_dictionary["damage"]
            break
        elif character == "5" or character == "exit game":
            end_game()
            break
        elif character == "6" or character == "secret option":
            player = secret_dictionary["name"]
            my_hp = secret_dictionary["hp"]
            my_damage = secret_dictionary["damage"]
            break
        else:
            print("Unknown Character, try again \n")

    print(f"Champion Selected: {player}")
    print(f"HP: {my_hp}")
    print(f"Damage: {my_damage}\n")

    while True:
        dragon_dictionary["hp"] -= my_damage
        print(f"The {player} damaged the Dragon!")
        print("Dragon HP: " + str(dragon_dictionary["hp"]) + "\n")

        if dragon_dictionary["hp"] <= 0:
            print("The Dragon has fallen!")
            print(f"The {player} wins the battle!")
            break

        my_hp -= dragon_dictionary["damage"]
        print(f"The Dragon has attacked the {player}!")
        print(f"{player} HP: {my_hp} \n")

        if my_hp <= 0:
            print(f"The {player} has fallen!")
            print("The Dragon has won the battle!")
            break

    replay = input("Would you like to play again?: ").lower()

    if replay == "y" or replay == "yes":
        dragon_dictionary["hp"] = 300
        counter += 1
        continue
    else:
        end_game()
