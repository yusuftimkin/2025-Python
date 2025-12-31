print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."/" . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      
''')

print("Welcome to the Tressure Island!")

print("Your goal is find the tressure.")

turn = input("You are in a cross road. Will you turn right or left?\n").lower()

if turn == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    action = input("Will you swim or wait for the boat?\n").lower()

    if action == "wait":
        print("You've come to the island and there is a house with three doors.")
        door = input("Which door will you pass through? Red, Yellow or Blue?\n").capitalize()

        if door == "Red":
            print("Burned by fire. Game over.")
        elif door == "Blue":
            print("Eaten by beasts. Game over.")
        elif door == "Yellow":
            print("You win!")
        else:
            print("Game over.")
    
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. Game over.")