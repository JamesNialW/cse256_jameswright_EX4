# James Wright
# CIS256 Spring 2025
# EX 4

# Import the functions to be tested.
from guess_the_word import *

# Initialize global random_word.
random_word = get_random_word()

def test_random_word():
    # Test that the random word is not empty.
    assert random_word != ''

    # Test that the random word is in the word list.
    assert random_word in word_list

def test_correct_input():
    revealed_word = ['_'] * len(random_word)

    # Test that the correct input reveals the letter in the word.
    correct_input(random_word[0], random_word, revealed_word)
    assert revealed_word[0] == random_word[0]

def test_incorrect_input():
    revealed_word = ['_'] * len(random_word)

    # Test that the incorrect input does not reveal any letters in the word.
    original_revealed_word = revealed_word.copy()
    incorrect_input('z', revealed_word)
    assert revealed_word == original_revealed_word

def test_assess_guess():
    revealed_word = ['_'] * len(random_word)
    original_revealed_word = revealed_word.copy()

    # Test that correct input is correctly processed.
    # guess_count_holder_variable is used to capture the return value of assess_guess.
    guess_count_holder_variable = assess_guess(random_word[0], random_word, revealed_word, 0, [])
    assert revealed_word != original_revealed_word

    # Test that incorrect input is correctly processed.
    revealed_word = ['_'] * len(random_word)
    original_revealed_word = revealed_word.copy()

    test_word = 'bunny'
    # guess_count_holder_variable is used to capture the return value of assess_guess.
    guess_count_holder_variable = assess_guess('a', test_word, revealed_word, 0, [])
    assert revealed_word == original_revealed_word

test_random_word()
test_correct_input()
test_incorrect_input()
test_assess_guess()