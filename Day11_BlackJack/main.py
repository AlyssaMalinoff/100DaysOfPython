import random
from art import logo


def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
#Checking for a win condition (blackjack)
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #If we pull an Ace (11) and our score would be over 21 as a result, use the Ace as a 1 instead.
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare (user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose :'( "
  elif user_score == computer_score:
    return "Draw!"
  elif computer_score == 0:
    return "Lose, House has Blackjack :("
  elif user_score == 0:
    return "You Win! Blackjack :)"
  elif user_score > 21:
    return "You went over. You lose :/"
  elif computer_score > 21:
    return "House went over, you win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose :("
  
def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards are: { yuser_cards}, current score: { user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"Your final cards: {user_cards}, final score: {user_score}")
  print(f"Computer's cards {computer_cards}, final score: {computer_score}")
  print (compare(user_score, computer_score))

while input("Do you want to play a game? Type 'y' or 'n':") == "y":
    play_game()

        