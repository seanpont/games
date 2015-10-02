#!/usr/bin/python

"""
Review:
    Objects literals (int, str, float)
    Conditionals and Looping Constructs (if, while, for)
    Functions (def)
    Tuples (), lists [], and dictionaries {}
    Mutability and immutability
Today:
    Use tuples, lists, and dicts to solve complex problems
    Discuss mutability and its perils
    (stretch goal) Introduce recursion

To practice with lists, conditionals, and loops, we'll build the game Hangman
"""

import random
import string

def get_random_word():
    """Returns a random word from the built-in dictionary"""
    with open('/usr/share/dict/words') as word_file:
        return random.choice([word.strip() for word in word_file if word.islower()])

print get_random_word()

def word_with_only_letters(word, letters):
    return ''.join(map(lambda letter: letter if letter in letters else '_', word))

print word_with_only_letters('apple', 'pl')

def play_hangman(max_num_guesses):
    print 'Welcome! Guess the word in %d guesses to win' % max_num_guesses
    word = get_random_word()
    print "I am thinking of a word %d letters long" % len(word)
    possible_letters = string.ascii_lowercase
    letters = ''
    num_guesses = 0
    while num_guesses < max_num_guesses:
        print '\n-----------------------'
        print 'You have %d guesses left' % (max_num_guesses - num_guesses)
        print 'Available letters: %s' % possible_letters
        letter = raw_input("Please guess a letter: ")
        if not letter or len(letter) != 1:
            print 'Invalid guess'
            continue
        if letter in letters:
            print 'You already guessed that'
            continue
        letters += letter
        possible_letters = possible_letters.replace(letter, '')
        if letter in word:
            print 'Good guess! %s' % word_with_only_letters(word, letters)
        else:
            print 'Nope, guess again. %s' % word_with_only_letters(word, letters)
        num_guesses += 1
        if all(map(lambda x: x in letters, word)):
            print "You won!"
            return
    print "Sorry, the word was %s" % word

play_hangman(15)















