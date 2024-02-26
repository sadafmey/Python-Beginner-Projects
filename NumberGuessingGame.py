import random

def number_guessing_game():
    """A whimsical journey into the world of number guessing! Can you outsmart the computer and guess the secret number?"""
    print("Welcome to the Number Guessing Game!")  
    print("I'm thinking of a number between 1 and 100. Can you guess it within 10 attempts?") 
    secret_number = random.randint(1, 100)  # Generating a random secret number for the player to guess.
    attempts = 0  # Initializing the number of attempts the player has made.
    max_attempts = 10  # Setting the maximum number of attempts allowed.

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))  # Prompting the player to enter their guess.
        attempts += 1  # Incrementing the number of attempts made by the player.

        if guess < secret_number:
            print("Too low! Aim higher, my friend!")  
        elif guess > secret_number:
            print("Too high! Bring it down a notch, tiger!")  
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts! You're a true number ninja!")  
            break
    else:
        print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}. Better luck next time!")  

if __name__ == "__main__":
    number_guessing_game()
