import random

print("Welcome to rock, paper, scissors game!")

shapes = [
'''
         _...._
       .`      `.
      / ***      \         
     : **         :         
     :            :        
      \          /       
       `-.,,,,.-'  
         ''', 
'''
    ,-----------.
   (_\            ]
      |           |
      |           |
      |           |
      |           |
     _|           |
    (_/_____(*)___/
            ''', 
'''    
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
''']

player_choice = int(input("Please choose: 1 for rock, 2 for paper or 3 for scissors.\n"))

computer_choice = random.randint(1, 3)

game = ["rock", "paper", "scissors"]

if 0 < player_choice <4:
    print(f"\nYou choose {game[player_choice - 1]}!\n")
    print(shapes[player_choice - 1])
else:
    print("Invalid choice!")

print(f"Computer chooses {game[computer_choice -1]}!\n")
print(shapes[computer_choice - 1])

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
