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

To practice with lists, conditionals, and loops, we'll build the game Hangman
"""

import random
import string
from test_utils import assert_equal
import functional as f


def map_count(xs):
    return reduce(lambda m, x: f.set_on(m, x, m.get(x, 0) + 1), xs, {})

assert_equal({'a': 2, 'b': 1}, map_count('aba'))


def count_occurrences(items, target):
    """
    Return how many instances of target are in the list of items.
    items may be any iterable
    a list of numbers like [1,2,3] or a string like 'abc'
    :param target: The item that we would like to count
    :param items: A collection of items
    """
    return map_count(items)[target]

# Tests for count_occurrences
assert_equal(2, count_occurrences('noodle', 'o'))
assert_equal(4, count_occurrences('alabama', 'a'))
assert_equal(2, count_occurrences([1, 2, 3, 4, 3, 2, 1], 3))


def find_keys_with_highest_value(a_map):
    """
    Takes a map and returns the keys with the highest values
    :param a_map: a map where the values are comparable
    :return a list of the keys with the highest values
    """
    return f.flip_map(a_map)[max(a_map.values())]

assert_equal(['b'], find_keys_with_highest_value({'a': 1, 'b': 4, 'c': 2}))
assert_equal(['a', 'c'], find_keys_with_highest_value({'a': 4, 'b': 2, 'c': 4}))


def find_most_common_item(items):
    """
    Return the most common item among a set of items. For example:
    In the event of a tie, return whichever occurs first in the list.
    :param items:
    """
    return find_keys_with_highest_value(map_count(items))

assert_equal(['a'], find_most_common_item('alabama'))
assert_equal([1], find_most_common_item([1, 2, 3, 1, 2, 1]))
assert_equal(['a', 'b'], find_most_common_item('abcab'))


def find_items_that_occur_once(xs):
    """
    Return the item that only occurs only once.
    If there is none, return None
    :param xs: A list of items
    :return: the items that occur once
    """
    return f.flip_map(map_count(xs)).get(1, [])

assert_equal(['c'], find_items_that_occur_once('aabbc'))
assert_equal([4, 5], find_items_that_occur_once([1, 2, 3, 4, 3, 2, 1, 5]))
assert_equal(['c', 'd'], find_items_that_occur_once('abracadabra'))
assert_equal([], find_items_that_occur_once('aabbcc'))


def is_anagram(word1, word2):
    """
    Return true if word1 is an anagram of word2.
    An anagram is a word or phrase that uses all of the letters of another word
    or phrase
    in a different order.
    For example: 'silent' and 'listen' or 'able' and 'bale'
    """
    return map_count(word1) == map_count(word2)

assert_equal(True, is_anagram('silent', 'listen'))
assert_equal(False, is_anagram('foobar', 'foofoo'))
assert_equal(True, is_anagram('alexia', 'exalia'))
assert_equal(True, is_anagram('cedric', 'criced'))


# ===== HANGMAN ================================================================

def get_random_word():
    """Returns a random word from the built-in dictionary"""
    with open('/usr/share/dict/words') as word_file:
        return random.choice(
            [word.strip() for word in word_file if word.islower()])


def char_if_in_letters(character, letters):
    return character if character in letters else '_'


def word_with_only_letters(word, letters):
    """
    Return the word, but replace all the letters that are not
    in 'letters' with an underscore '_'
    For example, word_with_only_letters('apple', 'pl') == '_ppl_'
    """
    result = ''
    for letter in word:
        result += char_if_in_letters(letter, letters)
    return result

assert_equal('_____', word_with_only_letters('apple', ''))
assert_equal('_ppl_', word_with_only_letters('apple', 'pl'))
assert_equal('apple', word_with_only_letters('apple', 'aelp'))


def all_letters_in_word(word, letters):
    """
    Return true if all the letters in word are in 'letters'.
    For example, all_letters_in_word('apple', 'aelp') == True
    """
    for letter in word:
        if letter not in letters:
            return False
    return True

assert_equal(True, all_letters_in_word('apple', 'aelp'))
assert_equal(True, all_letters_in_word('apple', 'aelpfjt'))
assert_equal(False, all_letters_in_word('apple', 'elp'))
assert_equal(False, all_letters_in_word('apple', 'qwerty'))


def play_hangman(num_guesses):
    print 'Welcome! Guess the word in %d guesses to win' % num_guesses
    word = get_random_word()
    print "I am thinking of a word %d letters long" % len(word)
    possible_letters = string.lowercase
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
    print "Sorry, the word was " + word

