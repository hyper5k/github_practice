import random

def print_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def get_user_guess():
    while True:
        try:
            guess = int(input("Take a guess: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        guess = get_user_guess()
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
    
def main():
    print_welcome_message()
    play_game()
    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == 'yes':
            play_game()
        elif play_again == 'no':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Please answer 'yes' or 'no'.")

if __name__ == "__main__":
    main()
