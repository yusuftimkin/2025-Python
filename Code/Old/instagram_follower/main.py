import art

from game_data import data

import random

def info_format(account):

    account_name = account['name']
    account_description = account['description']
    account_country = account['country']

    return f"{account_name}, {account_description}, from {account_country}"

def answer_check(instagram_a, instagram_b, guess):
    if instagram_a > instagram_b:
        guess == "a"
        return True
    else:
        return False

print(art.logo)

instagram_b = random.choice(data)

print(f"Compare A: {info_format(instagram_b)}")

is_game_over = False

while not is_game_over:

    print(art.vs)

    score =0

    account_b = random.choice(data)
    account_a = account_b
    print(f"Compare B: {info_format(instagram_b)}")










