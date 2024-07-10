from os import system, name
from game_data import data
import random
from art import logo, vs


# Generate a random account from the game data.
def random_account():
    account = random.choice(data)
# Format account data into printable format.
def formated_account(account):
    name =  account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Ask user for a guess.


# Check if user is correct.
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
## Get follower count.
## If Statement

# Feedback.


# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.
