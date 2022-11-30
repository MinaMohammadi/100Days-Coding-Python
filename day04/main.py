import random

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors.\n"))
# Rock
Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_mode = [Rock, Paper, Scissors]
# computer_chose = len(game_mode)
# print(computer_chose)
# cpu_turn = random.randint(0 , computer_chose-1)

computer_choice = random.randint(0, 2)
print("You:\n", game_mode[player])
print("computer_choice:\n" , game_mode[computer_choice])

if player < 3:
    if player - computer_choice >= 1:
        print("You win!")
    elif player - computer_choice < 1:
        print("It's a draw.")
else:
    print("Invalid number, You lose!")
