import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [0, 1, 2]
pictures = [rock, paper, scissors]
#0 = Rock
#1 = Paper
#2 = Scissors

computer_choice = choices[random.choice(choices)]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if not 0 <= player_choice <= 2:
    exit()

if computer_choice == player_choice:
    print(f"{pictures[player_choice]}\nComputer chose:\n{pictures[player_choice]}\nIt's a draw.")
elif player_choice == 0 and computer_choice == 2 or player_choice == 1 and computer_choice == 0 or\
    player_choice == 2 and computer_choice == 1:
        print(f"{pictures[player_choice]}\nComputer chose:\n{pictures[computer_choice]}\nYou win!")
else:
    print(f"{pictures[player_choice]}\nComputer chose:\n{pictures[computer_choice]}\nYou lose :(")

