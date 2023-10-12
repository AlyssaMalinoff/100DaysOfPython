from art import logo
from game_data import data
import random


# Modify the format_data() function to return the formatted data as a dictionary without printing
def format_data(entry):
    return {
        "name": entry["name"],
        "description": entry["description"],
        "country": entry["country"],
        "follower_count": entry["follower_count"],
    }


def HigherLower():
    gameContinue = True
    score = 0
    print(logo)
    print(
        "Welcome to the Higher or Lower game! Here you will be presented with 2 options and you have to guess which one has a higher follower count from Instagram. Good luck :)"
    )
    while gameContinue:
        # Select two unique entries from the game_data list and assign them to variables for comparison
        random_values = random.sample(data, 2)
        optionOne = format_data(random_values[0])
        optionTwo = format_data(random_values[1])

        # Print the options for the user
        print("Compare A:")
        print(
            f"{optionOne['name']}, a {optionOne['description']} from {optionOne['country']}."
        )
        print("VS")
        print("Compare B:")
        print(
            f"{optionTwo['name']}, a {optionTwo['description']} from {optionTwo['country']}."
        )

        # Collect the user's guess
        userChoice = input(
            "Which celebrity has more Instagram followers? Choose option A or B: "
        ).lower()

        # Compare the follower_count value for both entries
        if (
            optionOne["follower_count"] > optionTwo["follower_count"]
            and userChoice == "a"
        ) or (
            optionOne["follower_count"] < optionTwo["follower_count"]
            and userChoice == "b"
        ):
            print("You're right! 🎉")
            score += 1
            print(f"Your score is: {score}")
        else:
            print(
                f"Sorry, that's incorrect. Game Over! Your score was: {score}. Thank you for playing!"
            )
            break  # Exit the loop and end the game


# Run the game
HigherLower()
