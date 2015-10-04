#!/usr/bin/python

"""
Review:
    Objects literals (int, str, float)
    Conditionals and Looping Constructs (if, while, for)
    Functions (def)
    Tuples (), lists [], and dictionaries {}
    Mutability and immutability
Today:
    Practice using strings, tuples, lists, and dicts to solve problems
    Introduce recursion

To practice with lists, conditionals, and loops, we'll build the game Hangman
"""

import random
import string


def count_occurrences(items, target):
    """
    Return how many instances of target are in the list of items.
    items may be any iterable
    a list of numbers like [1,2,3] or a string like 'abc'
    """
    pass


def find_most_common_item(items):
    """
    Return the most common item among a set of items. For example:
    In the event of a tie, return whichever occurs first in the list.
    """
    pass


def find_first_item_that_occurs_once(items):
    """
    Return the item that only occurrs once.
    If there is none, return None
    """
    pass


def is_anagram(word1, word2):
    """
    Return true if word1 is an anagram of word2.
    An anagram is a word or phrase that uses all of the letters of another word or phrase
    in a different order.
    For example: 'silent' and 'listen' or 'able' and 'bale'
    """
    pass


"""
Below, I've written a quick implementation of the game Hangman.
It will only work correctly if we implement the following functions correctly!
"""


def get_random_word():
    """Returns a random word from the built-in dictionary"""
    with open('/usr/share/dict/words') as word_file:
        return random.choice(
            [word.strip() for word in word_file if word.islower()])


def word_with_only_letters(word, letters):
    """
    Return the word, but replace all the letters that are not 
    in 'letters' with an underscore '_'
    For example, word_with_only_letters('apple', 'pl') == '_ppl_'
    """
    pass


def all_letters_in_word(word, letters):
    """
    Return true if all the letters in word are in 'letters'.
    For example, all_letters_in_word('apple', 'aelp') == True
    """
    pass


def play_hangman(num_guesses):
    print 'Welcome! Guess the word in %d guesses to win' % num_guesses
    word = get_random_word()
    print "I am thinking of a word %d letters long" % len(word)
    possible_letters = string.ascii_lowercase
    letters = ''
    while num_guesses > 0:
        print '\n', word_with_only_letters(word, letters)
        print 'You have %d guesses left' % num_guesses
        print 'Available letters: %s' % possible_letters
        letter = raw_input("Please guess a letter: ")
        if not letter or len(letter) != 1:
            print 'Invalid guess'
            continue
        if letter in letters:
            print 'You already guessed that!'
            continue
        letters += letter
        possible_letters = possible_letters.replace(letter, '')
        if letter in word:
            print 'Good guess!'
        else:
            print 'Sorry, guess again.'
        num_guesses -= 1
        if all_letters_in_word(word, letters):
            print "You won!"
            return
    print "Sorry, the word was %s" % word


if __name__ == '__main__':
    play_hangman(15)


"""
RECURSION

Definition:
The repeated application of a recursive procedure or definition.
See: Recursion


"""






