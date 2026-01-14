import art
import random

def ace_user():
    for index in range (0, len(user_hand)):
        if cards[index] == 11:
            if sum(user_hand) > 21:
                cards[index] = 1

def ace_dealer():
    for index in range (0, len(dealer_hand)):
        if cards[index] == 11:
            if sum(dealer_hand) > 21:
                cards[index] = 1


print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to the Blackjack!")

user_hand = []
dealer_hand = []
dealer_hit = True
user_hit = True
user_chance_win = True

for i in range(2):
    user_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))

sum_user_hand = sum(user_hand)
sum_dealer_hand = sum(dealer_hand)

print(f"Your hand: {user_hand}.")
print(f"Sum of your hand: {sum_user_hand}.")
print(f"Dealer hand: [{dealer_hand[0]}].")

while user_hit:

    ask_to_hit = input("Do you want to be hit or stay?").lower()

    if ask_to_hit == "hit":
        user_hand.append(random.choice(cards))
        ace_user()
        sum_user_hand = sum(user_hand)
        print(f"Your hand: {user_hand}.")
        print(f"Sum of your hand: {sum_user_hand}.")
        if sum_user_hand > 21:
            print("You lost!")
            user_hit = False
    elif ask_to_hit == "stay":
        user_hit = False
    else:
        print("Please enter a valid input.")

if sum_user_hand > 21:
    dealer_hit = False

while dealer_hit:
    if sum_dealer_hand < 17:
        print("Dealer hit")
        dealer_hand.append(random.choice(cards))
        ace_dealer()
        sum_dealer_hand = sum(dealer_hand)
        if sum_dealer_hand > 21:
            print("You win!")
            dealer_hit = False
    else:
        print("Dealer stay")
        sum_dealer_hand = sum(dealer_hand)
        dealer_hit = False
print(f"Dealer hand: {dealer_hand}.")
print(f"Sum of dealer hand: {sum_dealer_hand}.")

if sum_dealer_hand > sum_dealer_hand:
    print("You lost!")
elif sum_dealer_hand < sum_dealer_hand:
    print("You win!")
elif sum_dealer_hand == sum_user_hand:
    print("Draw!")
