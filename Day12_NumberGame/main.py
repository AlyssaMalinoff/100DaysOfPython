from art import logo
import random

#generate a random number between 1-100
#let the user select a difficult level (easy-10 guesses, hard-5 guesses)

#Setting game variables



def NumberGame():
    Number = random.randint(1, 100)
    guesses = 0
    

    print(logo/n"Welcome to the number guessing game!")
    Difficulty = input("Please select a difficulty: Easy or Hard /n Please type "E" or "H":")
    userGuess = int(input("Please guess a number between 1-100: "))

    #Checking for valid user input for variables
    if Difficulty == "E":
        guesses = 10
    elif Difficulty == "H":
         guesses = 5
    elif userGuess > 100 or userGuess < 1:
        userGuess =input("You didn't use a proper number, please guess between 1 and 100.")
    else:
        Difficulty = input("Looks like you didn't enter a valid difficulty, ops! Please try again, but only enter "E" or "H" for Easy or Hard mode: ")
        
    for attempt in range(guesses):
        while guesses > 0:
            if userGuess == Number:
                print(f"Hey, you win! The number was {Number}, good job")
            elif userGuess > Number:
                print("Too high")
                guesses -= 1
            elif userGuess < Number:
                print ("Too low")
                guesses -= 1

    



    


