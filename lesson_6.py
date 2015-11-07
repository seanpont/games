#!/usr/bin/python
# -*- coding: utf-8 -*-


from test_utils import assert_equal
import string


# Let's do some review!

# Examples of if statements
if 9 > 5:
    print "Yes, 9 greater than 5"

if 9 != 5:
    print "Yes, 9 not equal to 5"


# An example of an if/else statement
if 9 < 5:
    print "Yes, 9 less than 5"
else:
    print "No, 9 is not less than 5"


# Try writing an if/else statement that tests whether 779775 is divisible by 3
# Remember that the remainder operator is %
# TODO: is 779775 divisible by 3? print the answer


# When we're done here, delete this exit() and comment stuff out above
exit()

# An example using "not" and "and" keywords
if not (10 == 4) and 9 > 5:
    print "Yay, basic math competency achieved!"
else:
    print ":("

# Traffic light example
light_color = raw_input("What color is the traffic light? ")
light_color = light_color.lower()
print light_color
if light_color == "red":
    print "You should stop"
elif light_color == "yellow":
    print "Slow down!"
elif light_color == "green":
    print "Go ahead!"
else:
    print "What country are you in??"


# TODO: build another helper that takes an input and instructs the user


exit()

# for loops let us iterate over collections of things, like strings
a_string = "Hello World"
letter_count = 0

# Go through all the letters in a string
for letter in a_string:
    # Print out the position of each letter
    print "Letter number", letter_count, "is", letter
    # And increment the counter
    letter_count += 1

# Finally print how many letters were in the string
print "There were", letter_count, "letters in the string", a_string


# For loop examples using range:

# Range with 1 argument goes from 0 through n-1
for num in range(10):
    print num

# Range with 2 arguments goes from the first number through the last-1
for num in range(7, 15):
    print num

# Range with 3 arguments goes from the first number through the
#  second-1, in increments determined by the third number
for num in range(2, 12, 2):
    print num

# TODO: What happens if the 3rd number is negative?


exit()

# A while loop example

# Initialize a counter
count = 1
print "Count is initially", count
# Want to keep looping until the counter is bigger than 100
while count < 100:
    count = count * 9
    print "Now count is", count

# When we get here, the while loop is done - so count must be > 100
print "the counter is", count


# FUNCTIONS

# def starts a function definition
# names of functions follow variable naming conventions
# functions can take zero or more parameters
def party():
    print "This is a party!"


def is_a_party(apples, pizzas):
    # Returns True if you have enough apples and pizzas to make a party happen
    if apples > 10 and pizzas > 10:
        return True
    else:
        return False


# Testing the functions
print is_a_party(20, 20)
print is_a_party(5, 15)
print is_a_party(5, 2)
print is_a_party(14, 8)

# We can test our functions using other functions!
assert_equal(True, is_a_party(11, 11))
assert_equal(False, is_a_party(11, 9))
assert_equal(False, is_a_party(9, 11))
assert_equal(False, is_a_party(9, 9))
# TODO: Why did I test these four conditions?


def is_a_vowel(c):
    # TODO: write the implementation
    pass

# Testing is_a_vowel
assert_equal(True, is_a_vowel("u"))
assert_equal(True, is_a_vowel("E"))
assert_equal(False, is_a_vowel("x"))


exit()

def only_vowels(phrase):
    # Takes a phrase, and returns a string of all the vowels
    # Initalize an empty string to hold all of the vowels
    vowel_string = ''
    for letter in phrase:
        # check if each letter is a vowel
        if is_a_vowel(letter):
            # If it's a vowel, we append the letter to the vowel string
            vowel_string = vowel_string + letter
        # if not a vowel, we don't care about it- so do nothing!
    return vowel_string

# Testing the functions
print only_vowels("Cedric and Alexia")
print only_vowels("HeLlO wOrLd!!")
print only_vowels("klxn")  # Expect no vowels from this one!


# TODO: write a function that counts how many vowels are in a string


exit()

# STRINGS
new_string = "Hi Class!"
# iteration
for letter in new_string:
    print letter

# We can concatenate two strings together
s1 = "Hi"
s2 = "Class"
print s1 + s2

# gluing together with a comma adds an extra space
print s1, s2

# and with a comma you can glue together different data types
print s1, 6.189, s2

# We can index the string
print "new_string[0] is", new_string[0]
print "new_string[-1] is", new_string[-1]
# And slice it
print "new_string[0:3] is", new_string[0:3]

# We can get the length of our string using the len function
print "len(new_string) is:", len(new_string)

# And use various string methods on it
print "new_string.upper()", new_string.upper()
print "new_string.lower()", new_string.lower()


# LISTS

# Lists are defined by brackets
new_list = [3, 4, 5, 6]
print "new_list is:", new_list

# Just like strings, we can index & slice them
print "new_list[2] is:", new_list[2]
print "new_list[0:2] is:", new_list[0:2]

# And iterate through them:
for item in new_list:
    print item

# Lists, however, are mutable! So, if we want we can change the
# value of one element

new_list[2] = 100
print "new_list is:", new_list

# Or, add on a new element with append:
new_list.append(87)
print "new_list is:", new_list

# Or insert
new_list.insert(0, 200)  # insert at position 0 the element 200
print "new_list is:", new_list

# Or even delete an element using remove
new_list.remove(100)  # Write in the item that you want to remove from the list
print "new_list is:", new_list

# Lists are possibly the most useful data structure in Python!

# Examples of List Comprehensions in Python

print "Example 1: Make a list of letters in a string"
print [letter for letter in "Hello, World!"]

print "\nExample 2: Add an exclamation point to every letter"
print [letter+"!" for letter in "Hello, World!"]

print "\nExample 3: A multiplication table for the 9's"
print [9*num for num in range(13)]

print "\nExample 4: Make a list of letters in a string if they're not 'o'"
print [letter for letter in "Hello, World!" if letter != 'o']


# TODO(optional): ROCK PAPER SCISSORS
# Write the game rock paper scissors
# Should ask for two inputs, validate them, then say who won


exit()

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


# A palindrome may be defined recursively as well.
# Add print statements to watch it in action!


def is_palindrome(s):
    s = filter(lambda x: x in string.lowercase, s.lower())
    return _is_palindrome(s)


def _is_palindrome(s):
    if len(s) < 2:
        return True
    return s[0] == s[-1] and _is_palindrome(s[1:-1])

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


# TODO: Write a function that takes in two numbers and recursively multiplies
# them together.


exit()

# TODO: write fibonacci's sequence

def fib(n):
    """
    The Fibonacci sequence is the most famous recursively-defined
    number sequence.
    fib(n) = fib(n-1) + fib(n-2)
    Base case: fib(0) == fib(1) == 1
    What happens as n grows?
    How can we make it faster?
    """
    # TODO
    pass

assert_equal(1, fib(0))
assert_equal(1, fib(1))
assert_equal(2, fib(2))
assert_equal(8, fib(5))
assert_equal(89, fib(10))


# TODO: Write a function using recursion to check if a number n is prime
# (you have to check whether n is divisible by any number below n).









