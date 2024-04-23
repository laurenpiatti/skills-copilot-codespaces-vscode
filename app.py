# Ask if the user wants to play a game of rock paper scissors
print("Do you want to play a game of rock paper scissors?")

# Get the user's input
user_input = input()

user_score = 0
computer_score = 0
tie_score = 0

while user_input in ['yes', 'y', 'Yes', 'Y']:
    print("Let's play!")

    # Print options the user can choose from
    print("Choose rock, paper, or scissors. On your input, I will choose one of the three as well.")

    # randomly choose rock, paper, or scissors
    import random
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    # get the user's input
    user_input = input()

    # print out the computers choice and the users choice
    print("I picked:", computer_choice, "You picked:", user_input)

    # Determine the winner of the game and print the result
    # Rock beats scissors, scissors beats paper, paper beats rock
    # Add a point to the winner's score

    if computer_choice == user_input:
        print("It's a tie!")
        tie_score += 1
    elif computer_choice == "rock" and user_input == "scissors":
        print("I win! Rock beats scissors.")
        computer_score += 1
    elif computer_choice == "scissors" and user_input == "paper":
        print("I win! Scissors beats paper.")
        computer_score += 1
    elif computer_choice == "paper" and user_input == "rock":
        print("I win! Paper beats rock.")
        computer_score += 1
    elif computer_choice == "scissors" and user_input == "rock":
        print("You win! Rock beats scissors.")
        user_score += 1
    elif computer_choice == "paper" and user_input == "scissors":
        print("You win! Scissors beats paper.")
        user_score += 1
    elif computer_choice == "rock" and user_input == "paper":
        print("You win! Paper beats rock.")
        user_score += 1
    else:
        print("I'm sorry, I didn't understand that.")

    # ask the user if they want to play again
    print("Do you want to play again?")

    # get the user's input
    user_input = input()

# if the user says no, n, No, or N, then print the score and say goodbye
if user_input in ['no', 'n', 'No', 'N']:
    if(computer_score > user_score):
        winner = "I win!"
    elif(user_score > computer_score):
        winner = "You win!"
    else:
        winner = "It's a tie!"

    print(winner + " The final score is: Computer:", computer_score, "User:", user_score, "Ties:", tie_score,". Goodbye!")
# if the user input is invalid, notify them
else:
    print("I'm sorry, I didn't understand that. Goodbye!")
        




