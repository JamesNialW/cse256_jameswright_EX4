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

    if revealed_word == list(random_word):
        print(f'Correct! You have revealed the entire word: {random_word}')
    else:
        print(f'Correct! So far you have revealed: {revealed_word}')

def incorrect_input(user_input, revealed_word):
    print(f'Incorrect. {user_input} is not in the word. So far you have revealed: {revealed_word}')

def assess_guess(user_input, random_word, revealed_word, false_guesses, guessed_letters):
    if user_input in guessed_letters:
        print(f'You have already guessed {user_input}.')
    elif user_input in random_word:
        # Print confirmation message and update revealed_word.
        correct_input(user_input, random_word, revealed_word)

        guessed_letters.append(user_input)
    else:
        # Print incorrect message.
        incorrect_input(user_input, revealed_word)
    
        # Track number of attempts.
        false_guesses += 1
        print(f'You have made {false_guesses}/15 wrong guesses.')

        guessed_letters.append(user_input)

    return false_guesses

if __name__ == '__main__':
    while True:
        random_word = get_random_word()

        revealed_word = ['_'] * len(random_word)

        false_guesses = 0

        guessed_letters = []

        # Continuously prompt user to guess until word is complete.
        while True:
            if false_guesses == 15:
                print(f'You have reached the maximum number of attempts. The word was: {random_word}')
                break

            # Prompt user to guess.
            user_input = str(input("Guess a letter: ")).lower()

            false_guesses = assess_guess(user_input, random_word, revealed_word, false_guesses, guessed_letters)

            if revealed_word == list(random_word):
                # Congratulations message prints in correct_input function. Break out of loop.
                break