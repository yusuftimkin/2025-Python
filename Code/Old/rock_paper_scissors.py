import random

print("Welcome to the rock, paper, scissors game!")

player_choice = int(input("Please choose: 1 for rock, 2 for paper or 3 for scissors.\n"))

computer_choice = random.randint(1, 3)

game = ["rock", "paper", "scissors"]

if 0 < player_choice <4:
    print(f"\nYou choose {game[player_choice - 1]}!\n")
else:
    print("Invalid choice!")

print(f"Computer chooses {game[computer_choice -1]}!\n")

if player_choice == 1 and computer_choice == 1:
    print("Draw!")
elif player_choice == 2 and computer_choice == 2:
    print("Draw!")
elif player_choice == 3 and computer_choice == 3:
    print("Draw!")

if player_choice == 1 and computer_choice == 2:
    print("Computer win!")
elif player_choice == 1 and computer_choice == 3:
    print("You win!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
elif player_choice == 2 and computer_choice == 3:
    print("Computer win!")
elif player_choice == 3 and computer_choice == 1:
    print("Computer win!")
elif player_choice == 3 and computer_choice == 2:
    print("You win!")

print("\n")