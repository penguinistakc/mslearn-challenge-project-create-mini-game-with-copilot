# create a rock paper scissors game using python with github copilot

# import the random module
import random

# create a list of the possible choices
choices = ["rock", "paper", "scissors"]

#create the score and round played variables
score = 0
rounds_played = 0

# create the loop to play the game
while True:
    # get the user's choice
    user_choice = input("Enter your choice (rock, paper, scissors): ")

    # get the computer's choice
    computer_choice = random.choice(choices)

    # print the computer's choice
    print(f"Computer chose: {computer_choice}")

    # if player chose rock 
    if user_choice.lower() == "rock":
        if computer_choice == "rock":
            print("It's a tie!")
        elif computer_choice == "paper":
            print("Computer wins!")
        elif computer_choice == "scissors":
            print("You win!")
            score += 1
        # increment the rounds played
        rounds_played += 1

    # if player chose paper
    elif user_choice.lower() == "paper":
        if computer_choice == "rock":
            print("You win!")
            score += 1
        elif computer_choice == "paper":
            print("It's a tie!")
        elif computer_choice == "scissors":
            print("Computer wins!")
        # increment the rounds played
        rounds_played += 1
       
    # if player chose scissors
    elif user_choice.lower() == "scissors":
        if computer_choice == "rock":
            print("Computer wins!")
        elif computer_choice == "paper":
            print("You win!")
            score += 1
        elif computer_choice == "scissors":
            print("It's a tie!")
        # increment the rounds played
        rounds_played += 1
    
    # if the user's choice is not valid
    else:
        print("Invalid choice. Please enter rock, paper, or scissors.")
      
    # print the score and rounds played
    print(f"Score: {score}")
    print(f"Rounds played: {rounds_played}")

    # ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n): ")

    # if the user doesn't want to play again, break out of the loop
    if play_again.lower() != "y":
        break