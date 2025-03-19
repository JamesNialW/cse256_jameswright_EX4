# James Wright
# CIS256 Spring 2025
# EX 4

import random

# Dolch word list of frequently used English nouns with 'Santa Claus' removed (96 words).
word_list = ['apple',
             'baby', 'back', 'ball', 'bear', 'bed', 'bell', 'bird', 'birthday', 'boat', 'box', 'boy', 'bread', 'brother',
             'cake', 'car', 'cat', 'chair', 'chicken', 'children', 'Christmas', 'coat', 'corn', 'cow',
             'day', 'dog', 'doll', 'door', 'duck',
             'egg', 'eye',
             'farm', 'farmer', 'father', 'feet', 'fire', 'fish', 'floor', 'flower',
             'game', 'garden', 'girl', 'goat', 'grass', 'ground',
             'hand', 'head', 'hill', 'home', 'horse', 'house', 'kitty',
             'leg', 'letter',
             'man', 'men', 'milk', 'money', 'morning', 'mother',
             'name', 'nest', 'night',
             'paper', 'party', 'picture', 'pig',
             'rabbit', 'rain', 'ring', 'robin',
             'school', 'seed', 'sheep', 'shoe', 'sister', 'snow', 'song', 'squirrel', 'stick', 'street', 'sun',
             'table', 'thing', 'time', 'top', 'toy', 'tree',
             'watch', 'water', 'way', 'wind', 'window', 'woman', 'women', 'wood']

def get_random_word():
    random_word = random.choice(word_list)
    return random_word

def correct_input(user_input, random_word, revealed_word):
    for i in range(len(random_word)):
        if user_input == random_word[i]:
            revealed_word[i] = user_input

    print(f'Correct! So far you have revealed: {revealed_word}')

def incorrect_input(user_input, revealed_word):
    print(f'Incorrect. {user_input} is not in the word. So far you have revealed: {revealed_word}')

def assess_guess(user_input, random_word, revealed_word):
    if user_input in random_word:
        # Print confirmation message and update revealed_word.
        correct_input(user_input, random_word, revealed_word)
    else:
        # Print incorrect message.
        incorrect_input(user_input, revealed_word)

if __name__ == '__main__':
    while True:
        random_word = get_random_word()

        revealed_word = ['_'] * len(random_word)

        # Continuously prompt user to guess until word is complete.
        while True:
            # Prompt user to guess.
            user_input = str(input("Guess a letter: ")).lower()

            assess_guess(user_input, random_word, revealed_word)

            if revealed_word == list(random_word):
                # Print congratulations message and break out of loop.
                print(f'Congratulations! You guessed the word: {random_word}')
                break