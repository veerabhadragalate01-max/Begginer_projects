import random

def guess_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 50: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_game()
