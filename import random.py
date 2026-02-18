import random

# List to store game history
game_history = []

def game_mode(mode):
    if mode == "easy":
        print("Starting Easy Mode!")
        target = random.randint(1, 10)
        attempts = 5
    elif mode == "hard":
        print("Starting Hard Mode!")
        target = random.randint(1, 50)
        attempts = 3
    else:
        print("Unknown mode. Defaulting to Easy Mode.")
        target = random.randint(1, 10)
        attempts = 5

    print(f"You have {attempts} attempts to guess the number between 1 and {target if mode=='easy' else 50}.")

    guesses = []
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        guesses.append(guess)
        if guess == target:
            print("Congratulations! You guessed it right.")
            game_history.append({"mode": mode, "guessed_correctly": True, "guess": guess})
            break
        elif guess < target:
            print("Too low!")
        else:
            print("Too high!")
        attempts -= 1
    else:
        print(f"Sorry, you've run out of attempts. The number was {target}.")
        game_history.append({"mode": mode, "guessed_correctly": False, "guess": None})

    # Store guesses in the list
    print("Your guesses were:", guesses)

# Call the function with different arguments
game_mode("easy")
game_mode("hard")
game_mode("unknown")

# Use a for loop to display game history
print("\nGame History:")
for idx, record in enumerate(game_history):
    print(f"Game {idx + 1}: Mode={record['mode']}, Guessed Correctly={record['guessed_correctly']}, Guess={record['guess']}")