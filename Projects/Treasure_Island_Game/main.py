print("\n"
      "*******************************************************************************\n"
      "          |                   |                  |                     |\n"
      " _________|________________.=\"\"_;=.______________|_____________________|_______\n"
      "|                   |  ,-\"_,=\"\"     `\"=.|                  |\n"
      "|___________________|__\"=._o`\"-._        `\"=.______________|___________________\n"
      "          |                `\"=._o`\"=._      _`\"=._                     |\n"
      " _________|_____________________:=._o \"=._.\"_.-=\"'\"=.__________________|_______\n"
      "|                   |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |\n"
      "|___________________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|___________________\n"
      "          |           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |\n"
      " _________|___________| ;`-.o`\"=._; .\" ` '`.\"\` . \"-._ /_______________|_______\n"
      "|                   | |o;    `\"-.o`\"=._``  '` \" ,__.--o;   |\n"
      "|___________________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|___________________\n"
      "____/______/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/____\n"
      "/______/______/______/_\"=._o--._        ; | ;        ; ;/______/______/______/_\n"
      "____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____\n"
      "/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_\n"
      "____/______/______/______/______/_____\"=.o|o_.--\"\"___/______/______/______/____\n"
      "/______/______/______/______/______/______/______/______/______/______/_____ /\n"
      "*******************************************************************************\n")

print("Welcome to Treasure Island.")
print("You mission is to find the treasure.")
way = input("You're at a cross road.Where do you want to go?left or right?\n").lower()
if way == "left":
    go_through = input(
        "You come to a lake. There is an island in the middle of the lake.\nType wait to wait for a boat OR swim to swim across?\n").lower()
    if go_through == "wait":
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if door == "red":
            print("Burned By Fire.\nGame Over")
        elif door == "yellow":
            print("\n\t\tYou found the treasure!\n\n\t\t\t\t\tYou Win")
        elif door == "blue":
            print("\n\t\tEaten By Beasts.\n\n\t\t\t\t\tGame Over")
        else:
            print("\n\t\tYou chose a door that doesn't exist.\n\n\t\t\t\t\tGame Over")
    else:
        print("\n\t\tAttack by trout.\n\n\t\t\t\t\tGame Over")
else:
    print("\n\t\tFall into a hole.\n\n\t\t\t\t\tGame Over")
