import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to run the game
def play_game():
    print("\nWelcome to Rock, Paper, Scissors!")
    
    while True:
        # Ask the user for their choice
        user_choice = input("\nEnter 'rock', 'paper', or 'scissors' (or 'exit' to quit): ").lower()
        
        if user_choice == 'exit':
            print("Thanks for playing! Goodbye!\n\n")
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input: Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Get computer's choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        # Determine and print the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

# Start the game
play_game()