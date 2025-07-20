import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid input. Please type 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    if (user == "rock" and computer == "scissors") or \
       (user == "scissors" and computer == "paper") or \
       (user == "paper" and computer == "rock"):
        return "win"
    return "lose"

def play_game():
    print("=== Rock-Paper-Scissors Game ===")
    user_score = 0
    computer_score = 0
    round_num = 1

    while True:
        print(f"\n--- Round {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "win":
            print("You win this round!")
            user_score += 1
        elif result == "lose":
            print("You lose this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Score => You: {user_score} | Computer: {computer_score}")
        play_again = input("Do you want to play another round? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break
        round_num += 1

if __name__ == "__main__":
    play_game()
