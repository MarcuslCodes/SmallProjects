from titlework import logo
import random

secret_number = random.randint(1, 100)
game_over = False

def play_game():
    while not game_over:

        if difficulty == 'easy':
            guesses_left = 10
            print(f"You have {guesses_left} attempts remaining to guess the number.")
        elif difficulty == 'hard':
            guesses_left = 5
            print(f"You have {guesses_left} attempts remaining to guess the number.")
    
            while guesses_left > 0:
                guess = int(input("Make a guess: "))

                if guess == secret_number:
                    print(f"You got it! The answer was {secret_number}")
                    break #game_over = True
                else:
                    if guess > secret_number:
                        guesses_left -= 1
                        print(f"You have {guesses_left} attempts remaining to guess the number.\n"
                              f"Too high.\n"
                              f"Guess again!")
                    elif guess < secret_number:
                        guesses_left -= 1
                        print(f"You have {guesses_left} attempts remaining to guess the number.\n"
                              f"Too Low.\n"
                              f"Guess again!")
            if guesses_left == 0:
                print("You've run out of guesses. Refresh the page to run again.")
                break

print(logo)
print("Welcome to the Number Guessing Game!\n"
    "I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
play_game()
