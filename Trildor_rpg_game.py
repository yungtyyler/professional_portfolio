import random

print ("Adventures of Trildor")
print("++++++++++++++++++++++")

startGame = input("Start adventure? ").lower()
classList = ["warrior", "mage", "ranger", "assassin"]
weaponList = {
    "Sword": "warrior",
    "Staff": "mage",
    "Bow": "archer",
    "Knife": "assassin"
}
mainVillain = "\033[1m" + "Goran" + "\033[0m"

warriorAttackList = [("punch", 100), ("sword slash", 75), ("ultimate attack: Swordnado", 20)]
mageAttackList = [("punch", 100), ("mana blast", 75), ("ultimate attack: Fireball", 20)]
rangerAttackList = [("punch", 100), ("arrow shot", 75), ("ultimate attack: Arrow Storm", 20)]
assassinAttackList = [("punch", 100), ("throwing knife", 75), ("ultimate attack: Backstab", 20)]

if startGame == "yes" or startGame == "y":
    print("Wonderful!\n")

else:
    print("Too bad... see you next time!")
    quit()

print("Welcome to Trildor, my friend.")
print("I know I am a little old, so as you could imagine I'm rather hard of seeing... and hearing, so SPEAK UP!")

playerName = input("Tell me kid, what do they call you? ")
print(f"What a name! {playerName}... it's got a ring to it.")

playerClass = ""

while playerClass != weaponList.keys():

    weapons = ", ".join(str(key) for key in weaponList.keys())
    playerClass = input(f"\n Now remember, I am also slightly blind. What weapon is it that you carry with you? \n {weapons} \n").lower()

    if playerClass == "sword":
        print(f"\n A fellow warrior! Hmmmm... this could get interesting.\n")
        playerClass = classList[0]
        break

    elif playerClass == "staff":
        print("\n A fellow mage! Hmmmm... this could get interesting.\n")
        playerClass = classList[1]
        break

    elif playerClass == "bow":
        print("\n A fellow archer! Hmmmm... this could get interesting.\n")
        playerClass = classList[2]
        break

    elif playerClass == "knife":
        print("\n A fellow assassin! Hmmmm... this could get interesting.\n")
        playerClass = classList[3]
        break

    else:
        print("\n Hmmm... I'm not familiar with that weapon. Are you sure?")
    

print(f"Well, it's nice to meet you {playerName}.\n Back in my hay-day, I was the greatest {playerClass} Trildor had ever seen!\n That all changed, however, when... {mainVillain} rose to power.\n")

#Insert story here

print("Now, enough of that! We have some trouble on our hands. \n")

def fightSequence1():

    print("A couple of goblins just walked into this tavern, and I don't think they're here for a couple swigs of brew.\n")
    continue1 = False

    while not continue1:

        continueGame1 = input("If things go south in here, can I count on you to help me take these guys out? \n")

        if continueGame1 == "yes" or continueGame1 == "y":
            print("I knew I could count on you! Alright, let's listen...\n")
            continue1 = True
        else:
            print("Are you sure? This could be the opportunity of a lifetime for you kid, trust me.")

    print("Goblin 1: 'Hey, bartender! Why don't you give me and my friends here a couple of ales on the house.\n I promise you... you don't want to tell me no right now. \n Things can get really messy 'round here, real quick.\n")
    fighting = False

    while not fighting:

        fight1 = input(f"\nOld Man: This sounds likes it's about to get out of hand, {playerName}. There's three of these guys to take down. I can handle the one on the left and you focus on the one on the middle and the right. Are you ready to show me what a true {playerClass} can do? ")

        if fight1 == "y" or fight1 == "yes":
            print("Alrighty then, let's kick some ass!")
            fighting = True
        else:
            print("\nCome on! Grow some acorns and help me save this bar!")

    def battle():
        
        #Stats Display
        playerHealth = 150
        enemies = [("Middle Goblin", 100), ("Right Goblin", 200)]
        target = random.choice(enemies)
        targetName = target[0]
        targetHealth = target[1]
        print(f"\nCurrent Target: {targetName}, Health: {targetHealth} \n{playerName}, Health: {playerHealth} \n")
        attackList = []

        if playerClass == "warrior":
            for item in range(len(warriorAttackList)):
                attackList.append(warriorAttackList[item])
        if playerClass == "mage":
            for item in range(len(mageAttackList)):
                attackList.append(mageAttackList[item])
        if playerClass == "ranger":
            for item in range(len(rangerAttackList)):
                attackList.append(rangerAttackList[item])
        if playerClass == "assassin":
            for item in range(len(assassinAttackList)):
                attackList.append(assassinAttackList[item])
        
    battle()

fightSequence1()