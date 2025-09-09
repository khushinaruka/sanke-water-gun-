from game_logic import get_computer_choice, get_user_choice, determine_winner

def play_game():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    print(f"Your choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    result = determine_winner(computer_choice, user_choice)
    print(result)

if __name__ == "__main__":
    play_game()
