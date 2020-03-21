import random


# function for choosing random word from a list
def choose_random_word():
    long_list = ["python", "java", "kotlin", "javascript"]
    return random.choice(long_list)


# function to validate the input from the user
def is_valid(s, used_letters):
    if len(s) != 1:
        print("You should print a single letter")
        return False
    elif not s.islower():
        print("It is not an ASCII lowercase letter")
        return False
    elif s in used_letters:
        print("You already typed this letter")
        return False
    else:
        used_letters.add(s)  # to add the new letter entered by the user in the used_word set
        return True


# function for the main body of the game
def play():
    random_word = choose_random_word()
    set_of_word = set(random_word)

    temp_word = list("-" * len(random_word))  # word to display the completed word by user

    life = 8  # set available life = 8
    used_letters = set()  # set track the used words

    while life:
        print("\n")
        print("".join(temp_word))
        str_ = input("Input a letter: > ")

        if is_valid(str_, used_letters):
            if str_ not in set_of_word:
                print("No such letter in the word")
                life -= 1
            else:
                # to find the position of the str_ in the main string
                for i in range(len(random_word)):
                    if random_word[i] == str_:
                        temp_word[i] = str_
                # To match whether the user has guessed the word or not
                if "".join(temp_word) == random_word:
                    break

    if life:
        print()
        print("You guessed the word {}!".format("".join(temp_word)))
        print("You survived!")
    else:
        print("You are hanged!")

    print("\n")


print("H A N G M A N")

while True:
    option = input("Type \"play\" to play the game, \"exit\" to quit: > ")
    if option == "exit":
        break
    elif option == "play":
        play()
