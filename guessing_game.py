"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    [x] 1. Display an intro/welcome message to the player.
    [x] 2. Store a random number as the answer/solution.
    [x] 3. Continuously prompt the player for a guess.
      [x] a. If the guess greater than the solution, display to the player "It's lower".
      [x] b. If the guess is less than the solution, display to the player "It's higher".
    
    [x] 4. Once the guess is correct, stop looping, inform the user they "Got it"
        [x] and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("--------------------------------------------------")
    print(" Hello and Welcome to the Number Guessing Game!!! ")
    print("--------------------------------------------------")

    number_to_guess = random.randint(1,10)
    print(number_to_guess)
    guess_count = 1
    playing = True
    while playing:
      user_guess = input("Please choose between 1 and 10: ")
      user_guess = int(user_guess)
      if user_guess < 1 or user_guess > 10:
        print("Your number is out of scope. Please choose between 1 and 10.")
      elif user_guess > number_to_guess:
        print("It is higher!")
        guess_count += 1
      elif user_guess < number_to_guess:
        print("It is lower!")
        guess_count += 1
      elif user_guess == number_to_guess:
        print(f"You got it! It took you {guess_count} tries.")
      # continue_game = input("Would you like to play again? Y/N ")
      # continue_game = continue_game.lower()
      # if continue_game == "yes" or continue_game == "y":
# Kick off the program by calling the start_game function.
start_game()