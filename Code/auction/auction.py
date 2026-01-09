import art
print(art.logo)
print("\n")

print("Welcome to the secret auction program.")

auction = {}

auction_continue = True

def winner_of_auction():
    global winner
    winner = ""
    global highest_bid
    highest_bid = 0
    for person in auction:
        if auction[person] > highest_bid:
            highest_bid = auction[person]
            winner = person


while auction_continue:

    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))

    auction[name] = bid

    more_bidder = input("Any more bidders? (y/n)\n").lower()

    if more_bidder == "y":
        auction_continue = True
        print("\n" * 20)
    else:
        auction_continue = False

winner_of_auction()

print(f"{winner} is the winner of the auction by the amount of ${highest_bid}.")