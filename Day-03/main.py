print(r'''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
                                                                 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choice1 = input("You are on a crossroad. Where do you want to go? Left or Right?\n").lower()

if choice1 == "left":
    choice2 = input("You have arrived at a lake with an island on it's center.\n\
                    Do you want to WAIT for a boat or SWIM across?\n").lower().strip()

    if choice2 == "wait":
        choice3 = input("You arrived on the island unharmed.\nThere is a house with 3 doors:\
                         one red, one yellow, and one blue. Which color do you choose?\n").lower().strip()

        if choice3 == "red":
            print("The room is burning.\nGame Over!")
        elif choice3 == "blue":
            print("You were devoured by hungry beasts.\nGame over!")
        elif choice3 == "yellow":
            print("You found the treasure!\n You Win!")
        else:
            print("Invalid Option!")

    elif choice2 == "swim":
         print("You have been attacked by furious trouts.\nGame Over!")
    else:
        print("Invalid Option!")
        
elif choice1 == "right":
    print("You have fallen into a deep hole.\nGame Over!")
else:
    print("Invalid Option!")