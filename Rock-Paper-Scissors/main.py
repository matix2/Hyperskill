# Write your code here
import random

winning_cases = {
    "water": ["scissors", "fire", "rock", "hun", "lightning", "devil", "dragon"],
    "dragon": ["snake", "scissors", "fire", "rock", "gun", "lightning", "devil"],
    "devil": ["tree", "human", "snake", "scissors", "fire", "rock", "gun"],
    "gun": ["wolf", "tree", "human", "snake", "scissors", "fire", "rock"],
    "rock": ["sponge", "wolf", "tree", "human", "snake", "scissors", "fire"],
    "fire": ["paper", "sponge", "wolf", "tree", "human", "snake", "scissors"],
    "scissors": ["air", "paper", "sponge", "wolf", "tree", "human", "snake"],
    "snake": ["water", "air", "paper", "sponge", "wolf", "tree", "human"],
    "human": ["dragon", "water", "air", "paper", "sponge", "wolf", "tree"],
    "tree": ["devil", "dragon", "water", "air", "paper", "sponge", "wolf"],
    "wolf": ["lightning", "devil", "dragon", "water", "air", "paper", "sponge"],
    "sponge": ["gun", "lightning", "devil", "dragon", "water", "air", "paper"],
    "paper": ["rock", "gun", "lightning", "devil", "dragon", "water", "air"],
    "air": ["fire", "rock", "gun", "lightning", "devil", "dragon", "water"],
    "lightning": ["tree", "human", "snake", "scissors", "fire", "rock", "gun"]
}


# Gets user's selected rules, uses the default rules if the user doesn't send anything
def get_rules(cases):
    if not cases:
        cases = "rock,paper,scissors"
    rules = {}
    cases = cases.split(",")
    for case in cases:
        rules[case] = winning_cases[case]
    return rules


# Checks the inputted name and return its score
def get_name_score(name):
    with open("rating.txt", "r") as f:
        content = [x.rstrip("\n") for x in f]

    score = 0
    for line in content:
        name_content, score_content = line.split(" ")
        if name == name_content:
            score = int(score_content)
    return score


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    user_score = get_name_score(user_name)
    print(f"Hello, {user_name}")
    user_cases = input()
    game_rules = get_rules(user_cases)
    print("Okay, let's start")

    while True:
        user_choice = input()  # Read users input
        computer_choice = random.choice(list(game_rules.keys()))  # Choose a random option
        if user_choice == "!exit":
            print("Bye!")
            break
        else:
            if user_choice == "!rating":
                print(f"Your rating: {user_score}")
            elif user_choice in game_rules.keys():
                # Compares the options, determines the winner and outputs a line depending on the result of the game
                if user_choice in game_rules[computer_choice]:
                    print(f"Sorry, but the computer chose {computer_choice}")
                elif computer_choice == user_choice:
                    print(f"There is a draw ({computer_choice})")
                    user_score += 50
                else:
                    print(f"Well done. The computer chose {computer_choice} and failed")
                    user_score += 100
            else:
                print("Invalid input")
