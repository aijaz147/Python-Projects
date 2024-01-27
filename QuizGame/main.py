# Welcome message and introduction to the quiz
print("Welcome To My Computer Quiz")

# Ask the user if they want to play the quiz
playing = input("Do You Want To Play? ").lower()
if playing != "yes":
    quit()

# Inform the user that the game is starting
print("Okay! Let's play :)")

# Initialize the score counter
score = 0

# Define the function to ask a question
def ask_question(question, correct_answer):
    answer = input(question)
    if answer.lower() == correct_answer.lower():
        print("Correct!")
        return 1
    else:
        print(f"Incorrect! The correct answer is '{correct_answer}'.")
        return 0

# Define the questions and answers
questions = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What does GPU stand for? ", "graphics processing unit"),
    ("What does RAM stand for? ", "random access memory"),
    ("What does PSU stand for? ", "power supply unit")
]

# Ask each question and update the score
for question, answer in questions:
    score += ask_question(question, answer)

# Display the final score to the user
print(f"You got {score} questions correct!")
