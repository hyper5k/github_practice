import random


def get_user_choice():
  """Gets the user's choice and validates it."""
  while True:
    choice = input("Choose rock, paper, or scissors: ").lower()
    if choice in ["rock", "paper", "scissors"]:
      return choice
    else:
      print("Invalid choice. Please enter rock, paper, or scissors.")
def get_computer_choice():
  """Gets the computer's random choice."""
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)
def determine_winner(user_choice, computer_choice):
  """Determines the winner of the round."""
  if user_choice == computer_choice:
    return "Tie!"
  elif (
      (user_choice == "rock" and computer_choice == "scissors")
      or (user_choice == "paper" and computer_choice == "rock")
      or (user_choice == "scissors" and computer_choice == "paper")
  ):
    return "You win!"
  else:
    return "Computer wins!"
def playGame():
  """Plays a single round of rock, paper, scissors with a twist!"""
  user_choice = get_user_choice()
  computer_choice = get_computer_choice()
  print(f"You chose {user_choice}.")
  print(f"Computer chose {computer_choice}.")
  result = determine_winner(user_choice, computer_choice)
  print(result)
  return result
# Extra Credit: Best of 3
play_best_of_three = input("Do you want to play best of 3? (yes/no): ").lower()
if play_best_of_three == "yes":
  user_wins = 0
  computer_wins = 0
  while user_wins < 2 and computer_wins < 2:
    game_result = playGame()
    if game_result == "You win!":
      user_wins += 1
      print(f"User score: {user_wins}")
    elif game_result == "Computer wins!":
      computer_wins += 1
      print(f"Computer score: {computer_wins}")
    else:
      print("It's a tie!")
  if user_wins == 2:
    print("You won the best-of-three game!")
  else:
    print("The computer won the best-of-three game!")
else:
  game_result = playGame()
  if game_result == "You win!":
    print("Congratulations! You won the game!")
  elif game_result == "Computer wins!":
    print("Better luck next time! The computer won.")
  else:
    print("It was a tie!")