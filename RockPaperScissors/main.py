import random

# Initialize variables to track wins for the user and the computer
user_wins = 0
computer_wins = 0

# Define the options available for the game
options = ["rock", "paper", "scissors"]

# Define winning combinations using a dictionary for clarity and ease of use
winning_combinations = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

# Start the main game loop
while True:
    # Get user input, convert it to lowercase for consistency
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    
    # Check if the user wants to quit the game
    if user_input == "q":
        break
    
    # Check if the user's input is valid
    if user_input not in options:
        print("Invalid input. Please enter Rock, Paper, or Scissors.")
        continue
    
    # Generate a random choice for the computer
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    
    # Display the computer's choice to the user
    print("Computer picked", computer_pick + ".")
    
    # Determine the outcome of the game and update the win counts accordingly
    if computer_pick == user_input:
        print("It's a tie!")
    elif winning_combinations[user_input] == computer_pick:
        print("You Win!")
        user_wins += 1
    else:
        print("Computer Wins!")
        computer_wins += 1

# Display the final results of the game
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")

# Say goodbye to the player
print("Goodbye!")
