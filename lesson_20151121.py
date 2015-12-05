#!/usr/bin/python
# -*- coding: utf-8 -*-


from test_utils import assert_equal
import string


# FUNCTIONS

def adds_one(number):
    return number + 1


def subs_one(number):
    return number - 1


# print adds_one(3)
# print adds_one(subs_one(8))
# print adds_one(subs_one(adds_one(subs_one(8))))


def is_a_vowel(letter):
    return letter.lower() in 'aeiouy'

# Testing is_a_vowel
assert_equal(True, is_a_vowel("u"))
assert_equal(True, is_a_vowel("E"))
assert_equal(False, is_a_vowel("x"))


# FUNCTIONS THAT USE FUNCTIONS
def vowel_deleter(s):
    """Removes vowels from s"""
    return ''.join([letter for letter in s if not is_a_vowel(letter)])


assert_equal("F Br", vowel_deleter("Foo Bar"))


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
    :param n: The number of disks
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


def hanoi_count(n):
    if n == 1:
        return 1
    return hanoi_count(n-1) * 2 + 1


# A palindrome may be defined recursively as well.
# Add print statements to watch it in action!

def is_palindrome(s):
    s = filter(lambda c: c in string.lowercase, s.lower())
    return _is_palindrome(s)


def _is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and _is_palindrome(s[1:-1])


assert_equal(True, is_palindrome(""))
assert_equal(True, is_palindrome("a"))
assert_equal(True, is_palindrome("aa"))
assert_equal(False, is_palindrome("ab"))
assert_equal(True, is_palindrome("abcba"))
assert_equal(True, is_palindrome("abccba"))
assert_equal(True, is_palindrome("Eva, can I stab bats in a cave?"))
assert_equal(True, is_palindrome("A nut for a jar of tuna"))
assert_equal(True, is_palindrome("Go hang a salami, I'm a lasagna hog"))
assert_equal(False, is_palindrome("Definitely not a Palindrome"))


