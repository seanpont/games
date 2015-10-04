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

    >>> count_occurrences('noodle', 'o')
    2
    >>> count_occurrences('alabama', 'a')
    4
    >>> count_occurrences([1, 2, 3, 4, 3, 2, 1], 3)
    2
    """
    pass


def find_most_common_item(items):
    """
    Return the most common item among a set of items. For example:
    In the event of a tie, return whichever occurs first in the list.

    >>> find_most_common_item('alabama')
    'a'
    >>> find_most_common_item([1, 2, 3, 1, 2, 1])
    '1'
    >>> find_most_common_item('abcab')
    'a'
    """
    pass


def find_first_item_that_occurs_once(items):
    """
    Return the item that only occurrs once.
    If there is none, return None

    >>> find_first_item_that_occurs_once('aabbc')
    'c'
    >>> find_first_item_that_occurs_once([1, 2, 3, 4, 3, 2, 1, 5])
    4
    >>> find_first_item_that_occurs_once('abracadabra')
    'c'
    """
    pass


def is_anagram(word1, word2):
    """
    Return true if word1 is an anagram of word2.
    An anagram is a word or phrase that uses all of the letters of another word or phrase
    in a different order.
    For example: 'silent' and 'listen' or 'able' and 'bale'

    >>> is_anagram('silent', 'listen')
    True
    >>> is_anagram('foobar', 'foofoo')
    False
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

    >>> word_with_only_letters('apple', '')
    '_____'
    >>> word_with_only_letters('apple', 'pl')
    '_ppl_'
    >>> word_with_only_letters('apple', 'aelp')
    'apple'
    """
    pass


def all_letters_in_word(word, letters):
    """
    Return true if all the letters in word are in 'letters'.
    For example, all_letters_in_word('apple', 'aelp') == True

    >>> all_letters_in_word('apple', 'aelp')
    True
    >>> all_letters_in_word('apple', 'elpj')
    False
    """
    pass


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
    print "Sorry, the word was %s" % word


# if __name__ == '__main__':
#     play_hangman(15)


"""
RECURSION

Definition:
The repeated application of a recursive procedure or definition.
See: Recursion

Key idea: divide and conquer
Recursion is:
    Way of defining a problem
    Way of solving a problem
    Example:
        Definition of US Citizen
Two parts:
    Base Case
    Inductive case
Examples!
Build exponentiation, ie x^n
    b^n = b^(n-1) * b if n > 0, if n==0 1
"""


def simple_exp(b, n):
    if n == 0:
        return 1
    return b * simple_exp(b, n - 1) * b


"""
Towers of Hanoi
Three rods and a bunch of disks of decreasing size.
Can move one disk at a time. Can never cover a smaller disk
Goal: move all disks from one rod to the other.
"""


def hanoi(n, from_stack, to_stack, spare_stack):
    if n == 1:
        print 'move from', from_stack, 'to', to_stack
    else:
        hanoi(n - 1, from_stack, spare_stack, to_stack)
        hanoi(1, from_stack, to_stack, spare_stack)
        hanoi(n - 1, spare_stack, to_stack, from_stack)


# hanoi(3, 'f', 't', 's')


"""
A palindrome may be defined recursively as well.
Add print statements to watch it in action!
"""


def is_palindrome(s):
    s = filter(lambda x: x in string.lowercase, s.lower())
    return _is_palindrome(s)


def _is_palindrome(s):
    if len(s) <= 1:  # Note: two base cases!
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])


def fib(n):
    """
    The Fibonacci sequence is the most famous recursively-defined
    number sequence.
    fib(n) = fib(n-1) + fib(n-2)
    Base case: fib(0) == fib(1) == 1
    What happens as n grows?
    How can we make it faster

    >>> fib(0)
    1
    >>> fib(1)
    1
    >>> fib(2)
    2
    >>> fib(5)
    8
    >>> fib(10)
    89

    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
