import random

hearts = 5
hearts_list = ["<3"] * hearts
my_list = ["ardwark", "baboon", "camel"]
counter = 0
chosen_word = my_list[random.randint(0, len(my_list) - 1)]
print(f"testing word: {chosen_word}")
board = ["_"] * len(chosen_word)

while hearts_list:
    if counter == len(chosen_word):
        print(f"You Won! The word was {chosen_word}")
        break
    print(str(board) + " - Lifes: " + str(hearts_list))

    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
        if letter == guess:
            board[chosen_word.index(letter)] = letter
            counter += 1

    if guess not in chosen_word:
        hearts_list.pop(0)
