
dice = {
    1: (
        "┌───────┐\n"
        "│       │\n"
        "│   ●   │\n"
        "│       │\n"
        "└───────┘"
    ),
    2: (
        "┌───────┐\n"
        "│ ●     │\n"
        "│       │\n"
        "│     ● │\n"
        "└───────┘"
    ),
    3: (
        "┌───────┐\n"
        "│ ●     │\n"
        "│   ●   │\n"
        "│     ● │\n"
        "└───────┘"
    ),
    4: (
        "┌───────┐\n"
        "│ ●   ● │\n"
        "│       │\n"
        "│ ●   ● │\n"
        "└───────┘"
    ),
    5: (
        "┌───────┐\n"
        "│ ●   ● │\n"
        "│   ●   │\n"
        "│ ●   ● │\n"
        "└───────┘"
    ),
    6: (
        "┌───────┐\n"
        "│ ●   ● │\n"
        "│ ●   ● │\n"
        "│ ●   ● │\n"
        "└───────┘"
    ),
}


#import random
import random

#define Roll dice number
def Roll_Dice():
    return random.randint(1,6)

#Prompts User to select Y/N
Roll_Dice1
Response = input("Roll the dice? (y/n): ").lower()

#With "Y" response and roll dice, output corresponding ASCII art
if Response == "y":
    Roll_Dice()
    result = Roll_Dice()
    if result == 1:
        print(dice[1])
    elif result == 2:
        print(dice[2])
    elif result == 3:
        print(dice[3])
    elif result == 4:
        print(dice[4])
    elif result == 5:
        print(dice[5])
    else:
        print(dice[6])
elif Response == "n":
=======


