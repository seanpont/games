#!/usr/bin/python
# -*- coding: utf-8 -*-


from test_utils import assert_equal

# Let's do some review!

# Examples of if statements
if 9 > 5:
    print "Yes, 9 greater than 5"

if 9 != 5:
    print "Yes, 9 not equal to 5"

if not 9 == 5:
    print "9 is not equal to 5"


# An example of an if/else statement
if 9 < 5:
    print "Yes, 9 less than 5"
else:
    print "No, 9 is not less than 5"


# Try writing an if/else statement that tests whether 779775 is divisible by 3
# Remember that the remainder operator is %
if 779775 % 3 == 0:
    print "%d is divisible by 3" % 779775
else:
    print "Nope"


# An example using "not" and "and" keywords
if not (10 == 4) and 9 > 5:
    print "Yay, basic math competency achieved!"
else:
    print ":("

# Traffic light example
# light_color = raw_input("What color is the traffic light? ")
# light_color = light_color.lower()
# print light_color
# if light_color == "red":
#     print "You should stop"
# elif light_color == "yellow":
#     print "Slow down!"
# elif light_color == "green":
#     print "Go ahead!"
# else:
#     print "What country are you in??"


# speed = raw_input("how fast do you run? ")
# speed = speed.lower()
# if speed == 'fast':
#     print 'As fast as YiOu?'
# elif speed == 'meh':
#     print 'YiOu will probably beat you'
# elif speed == 'slow':
#     print 'You will lose to YiOu, but go have fun anyway'


# exit()

def is_vowel(letter):
    return letter.lower() in 'aeiouy'

print "U is a vowel?", is_vowel('u')


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

# A while loop example

# Initialize a counter
count = 1
print "Count is initially", count
# Want to keep looping until the counter is bigger than 100
while count < 100:
    count *= 9
    print "Now count is", count

# When we get here, the while loop is done - so count must be > 100
print "the counter is", count


# A while loop where we count dice rolls
from random import randint
dice_count = 0
while randint(1, 6) != 6:
    dice_count += 1

print "it took %d rolls to get a 6"


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
