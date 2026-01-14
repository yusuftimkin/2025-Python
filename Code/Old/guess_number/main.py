import art2

import random

def lives_check(lives):
    if lives == 0:
        print("You have lost. Try again.")
        return True



def play_game():

    print(art2.logo)

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    lives = 0

    wanna_play_again = True

    game_difficulty = " "

    game_difficulty= input("Choose a difficulty level: easy, hard\n").lower()

    if game_difficulty == "easy":
        lives = 10
    elif game_difficulty == "hard":
        lives = 5

    computer_select_number = random.randint(1,100)

    is_game_over = False

    while not is_game_over:

        guess_num = int(input("Make a guess: "))

        if computer_select_number == guess_num:
            print("You guessed the number!")
            is_game_over = True
        elif computer_select_number > guess_num:
            print("Too low. Try again.")
            lives -= 1
            print(f"You have {lives} lives remaining.")
            is_game_over = lives_check(lives)

        elif computer_select_number < guess_num:
            print("Too high. Try again.")
            lives -= 1
            print(f"You have {lives} lives remaining.")
            is_game_over = lives_check(lives)

    print(f"Chosen number: {computer_select_number}")

    while wanna_play_again:
        again = input("Do you want to play again? (y/n)\n").lower()
        if again == "y":
            print("\n" * 20)
            play_game()
        else:
            print("Thank you for playing!")
            wanna_play_again = False

play_game()