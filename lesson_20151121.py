#!/usr/bin/python
# -*- coding: utf-8 -*-


from test_utils import assert_equal


# FUNCTIONS

def is_a_vowel(letter):
    return letter.lower() in 'aeiouy'

# Testing is_a_vowel
assert_equal(True, is_a_vowel("u"))
assert_equal(True, is_a_vowel("E"))
assert_equal(False, is_a_vowel("x"))

# FUNCTIONS THAT USE FUNCTIONS
# TODO: write a function that removes all the vowels from a string


# TODO: write some tests for said function


# exit()

"""
RECURSION: Functions that call themselves

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
"""


def hanoi(n, from_stack, to_stack, spare_stack):
    """
    Towers of Hanoi
    Three rods and a bunch of disks of decreasing size.
    Can move one disk at a time. Can never cover a smaller disk
    Goal: move all disks from one rod to the other.
    :param from_stack: name of from_stack
    :param to_stack: name of to_stack
    :param spare_stack: name of spare stack
    """
    if n == 1:
        print 'move from', from_stack, 'to', to_stack
    else:
        hanoi(n - 1, from_stack, spare_stack, to_stack)
        hanoi(1, from_stack, to_stack, spare_stack)
        hanoi(n - 1, spare_stack, to_stack, from_stack)


print "moving 5:"
hanoi(4, 1, 2, 3)


exit()


# A palindrome may be defined recursively as well.
# Add print statements to watch it in action!

# TODO: write a function, is_palindrome, that tests if a string is a palindrome
def is_palindrome(s):
    raise Exception("Unimplemented!")


assert_equal(True, is_palindrome(""))
assert_equal(True, is_palindrome("a"))
assert_equal(True, is_palindrome("aa"))
assert_equal(False, is_palindrome("ab"))
assert_equal(True, is_palindrome("abcba"))
assert_equal(False, is_palindrome("abccba"))
assert_equal(True, is_palindrome("Eva, can I stab bats in a cave?"))
assert_equal(True, is_palindrome("A nut for a jar of tuna"))
assert_equal(True, is_palindrome("Go hang a salami, I'm a lasagna hog"))
assert_equal(False, is_palindrome("Definitely not a Palindrome"))


exit()


# TODO: write a function that returns the nth fibonacci number


exit()


# TODO: use maps to make the recursive fibonacci function faster.


exit()


# TODO: use maps to answer questions about different dog breeds


