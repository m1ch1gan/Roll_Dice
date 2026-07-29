#import random
import random
#Prompts User to select Y/N
RollDice = input("Roll the dice? (y/n): ")
UserResponse = RollDice.upper
#Logic for when user responds 
if UserResponse == str("Y").upper:
    RollDiceNumber1 =random.randint(0, 100)
    RollDiceNumber2 =random.randint(0,100)
    print(f"(",str(RollDiceNumber1) + ", " + str(RollDiceNumber2),f")")
elif UserResponse == str("N").upper:
    pass
    print("Thanks for playing!")
else:
    print("Invalid Choice!")


