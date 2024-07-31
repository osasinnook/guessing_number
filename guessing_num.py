import random
import math

def number_guessing_game():
    upper_bound = int(input('Enter Your Upper Bound Range: '))
    lower_bound = int(input('Enter Your Lower Bound Range: '))
    
    if lower_bound > upper_bound:
        print("Error: Lower bound must be less than or equal to upper bound.")
        return
    
    # Special number to be guessed
    secret_number = random.randint(lower_bound, upper_bound)
    
    # Maximum number of guesses
    max_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))
    
    # Initializing the number of guesses
    number_of_guesses = 0
    
    print(f"I have selected a number between {lower_bound} and {upper_bound}. Can you guess what it is?")
    print(f"You should be able to guess it in a maximum of {max_guesses} guesses.")
   
    while True:
        guess = int(input('Enter the number: '))
        number_of_guesses += 1
        
        if guess < secret_number:
            print('Oops! Your guess is too small. Try again.')
        elif guess > secret_number:
            print('Oops! Your guess is too high. Try again.')
        else:
            print(f"Congratulations! You guessed the number in {number_of_guesses} guesses.")
            if number_of_guesses <= max_guesses:
                print(f"You guessed it within the maximum number of guesses ({max_guesses}). Well done!")
            break
        
        if number_of_guesses >= max_guesses:
            print("Sorry, you've reached the maximum number of guesses. Better luck next time!")
            break

# Run the game
number_guessing_game()
