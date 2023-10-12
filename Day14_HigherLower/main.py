from art import logo, vs
from game_data import data
import random


def HigherLower():
    print(logo)
    print(
        "Welcome to the Higher or Lower game! Here you will be presented with 2 options and you have to guess which one has a higher follower count from Instagram. Good luck :)"
    )
    # Select two unique entries from the game_data list and assign them to variables for comparison
    random_values = random.sample(data, 2)
    optionOne = random_values[0]
    optionTwo = random_values[1]


# Display the name, description and country of the entry selected
# Ask user to select which option they think has a higher follower count (A = optionOne, B = optionTwo)
# Compare the follower_count value for both entries
# If user guessed correctly, give them a point, assign the correctly guessed choice to optionOne, and select a new random entry for optionTwo
# If user was not correct, end the game


HigherLower()
