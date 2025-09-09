import random

def get_computer_choice():
    choices = ["snake", "water", "gun"]
    return random.choice(choices)

def get_user_choice():
    return input("Enter your choice (snake, water, gun): ").lower()

def determine_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "Match is a draw"
    elif (computer_choice == "snake" and user_choice == "water") or \
         (computer_choice == "water" and user_choice == "gun") or \
         (computer_choice == "gun" and user_choice == "snake"):
        return "You lose"
    else:
        return "You win"
