import random
import rps_module

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

pc_choice = random.randint(0, 2)

if player_choice == 0:
    print(f"{rps_module.rock}\n\nComputer choose:")
    if pc_choice == 0:
        print(f"{rps_module.rock}\n\nDRAW")
    elif pc_choice == 1:
        print(f"{rps_module.paper}\n\nYou Lose")
    else:
        print(f"{rps_module.scissors}\n\nYou Win")

elif player_choice == 1:
    print(f"{rps_module.paper}\n\nComputer choose:")
    if pc_choice == 1:
        print(f"{rps_module.paper}\n\nDRAW")
    elif pc_choice == 2:
        print(f"{rps_module.scissors}\n\nYou Lose")
    else:
        print(f"{rps_module.rock}\n\nYou Win")

elif player_choice == 2:
    print(f"{rps_module.scissors}\n\nComputer choose:")
    if pc_choice == 2:
        print(f"{rps_module.scissors}\n\nDRAW")
    elif pc_choice == 0:
        print(f"{rps_module.rock}\n\nYou Lose")
    else:
        print(f"{rps_module.paper}\n\nYou Win")
else:
    print("You typed an invalid number.")
    

