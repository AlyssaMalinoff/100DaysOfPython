from art import logo, vs
from game_data import data
import random

"""
TODO:
create a game that compares the amount of followers a certain celebrity has and asks the user to guess which is higher. If the user gets it right, they get 1 point and are asked to compare 
the winning choice to a new celebrity. this goes on until the user gets it wrong, which means the game ends.

"""


# ask the user which one they think is higher
# compare the two follower counts of the selected celebrities
# if user is correct, give them 1 point
# if user is wrong, end the game.
# if the user is correct, select another entry from the game_data to compare the winning option to


def HigherLower():
    # print(logo)
    # print('Welcome to the Higher or Lower game! Here you will be presented with 2 options and you have to guess which one has a higher follower count from Instagram. Good luck :)')

    # Select two unique entries from the game_data list and assign them to variables for comparison
    random_values = random.sample(data, 2)
    optionOne = random_values[0]
    optionTwo = random_values[1]


HigherLower()
