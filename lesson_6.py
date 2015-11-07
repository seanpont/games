
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

import string
from test_utils import assert_equal


def simple_exp(b, n):
    if n == 0:
        return 1
    return b * simple_exp(b, n - 1) * b


def hanoi(n, from_stack, to_stack, spare_stack):
    """
    Towers of Hanoi
    Three rods and a bunch of disks of decreasing size.
    Can move one disk at a time. Can never cover a smaller disk
    Goal: move all disks from one rod to the other.
    """
    if n == 1:
        print 'move from', from_stack, 'to', to_stack
    else:
        hanoi(n - 1, from_stack, spare_stack, to_stack)
        hanoi(1, from_stack, to_stack, spare_stack)
        hanoi(n - 1, spare_stack, to_stack, from_stack)


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
    How can we make it faster?
    """
    pass

assert_equal(1, fib(0))
assert_equal(1, fib(1))
assert_equal(2, fib(2))
assert_equal(8, fib(5))
assert_equal(89, fib(10))

