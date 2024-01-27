import random

def get_top_of_range():
    """Prompt the user to input the top limit for the random number."""
    top_of_range = input("Type a positive integer as the maximum value: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print('Please type a number larger than 0 next time.')
            quit()
    else:
        print('Please type a number next time.')
        quit()

    return top_of_range

def play_guessing_game(top_of_range):
    """Play the guessing game with the specified range."""
    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print('Please type a number next time.')
            continue

        if user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("You guessed above the number!")
        else:
            print("You guessed below the number!")

    print("You got it in", guesses, "guesses")

def main():
    """Main function to orchestrate the game."""
    print("Welcome to the Number Guessing Game!")
    top_of_range = get_top_of_range()
    play_guessing_game(top_of_range)

if __name__ == "__main__":
    main()
