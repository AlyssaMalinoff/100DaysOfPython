from art import logo
import random

def NumberGame():
    print(logo)
    print("Welcome to the guessing game! Guess the number I'm thinking of. You'll have 10 chances to get it right, but if you want to try Hard Mode...You'll only have 5 ;) ")

    #Initializing some variables for later
    Number = random.randint(1, 100)
    guesses = 0
    
    #Setting the amount of guesses based on user input and validating 
    difficulty = input("Please select a difficulty: Easy or Hard. Please type 'E' or 'H': ")
    if difficulty.lower() == "e":
        guesses = 10
    elif difficulty.lower() == "h":
        guesses = 5
    else:
        difficulty = input("Looks like you didn't enter a valid difficulty. Please try again, but only enter 'E' or 'H' for Easy or Hard mode: ")
        if difficulty.lower() != "e" or "h":
            print("Could not set difficulty.")
            return
    
    #Setting the users guess and handling conditions based on the number generated and the users guess 
    userGuess = int(input("Please guess a number between 1-100: "))

    while guesses > 0:
        if userGuess == Number:
            print(f"Hey, you win! The number was {Number}, good job")
            return  
        elif userGuess > Number:
            print("Too high")
        elif userGuess < Number:
            print("Too low")
        elif abs(userGuess - Number) <= 10:
            print("You're close!")
        elif abs(userGuess - Number) <= 5:
            print("You're superrrr close!")
        elif userGuess > 100 or userGuess <1:
            userGuess =input("You didn't use a proper number, please guess between 1 and 100.")
            guesses = guesses + 1
        elif guesses == 0:
            return
        else:
            print(f"Sorry, you've used all your gusses. The correct number was: {Number}, better luck next time!")

        #decrementing the amount of guesses and letting the user know their current total
        guesses -= 1
        print(f"You have {guesses} guesses left.")
        userGuess = int(input("Please guess again: "))

    print(f"Sorry, you've used all your guesses. The correct number was: {Number}, better luck next time!")

# Don't forget to run the function
NumberGame()


    



    


