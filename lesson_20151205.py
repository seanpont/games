# coding=utf-8
from test_utils import assert_equal


# RECURSION

# TODO: write a function that returns the nth fibonacci number
def fib(n):
    pass

# Tests for fib(n)
assert_equal(fib(0), 1)
assert_equal(fib(1), 1)
assert_equal(fib(2), 2)
assert_equal(fib(3), 3)
assert_equal(fib(4), 5)
assert_equal(fib(5), 8)

exit()


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

# Examples of List Comprehensions in Python

print "Example 1: Make a list of letters in a string"
print [letter for letter in "Hello, World!"]

print "\nExample 2: Add an exclamation point to every letter"
print [letter + "!" for letter in "Hello, World!"]

print "\nExample 3: A multiplication table for the 9's"
print [9 * num for num in range(13)]

print "\nExample 4: Make a list of letters in a string if they're not 'o'"
print [letter for letter in "Hello, World!" if letter != 'o']


# TODO: write a function that returns the intersection of two lists
# (all the elements that are common in both groups)


exit()


# Write a list comprehension which solves the equation y = x**2 + 1
# Your solution should print out a list of [x, y]


# TODO: physics engine! write a function that determines if two balls have
# collided. Represent the balls as a tuple of (x, y, r)


# DICTIONARIES

# D = {key1:value1, ...} creates a non-empty dictionary
# D[key] returns the value thats mapped to by key.
# (What if there's no such key?)
# D[key] = newvalue maps newvalue to key. Overwrites any previous value.
# Remember - newvalue can be any valid Python data structure.
# del D[key] deletes the mapping with that key from D.
# len(D) returns the number of entries (mappings) in D.
# x in D, x not in D checks whether the key x is in the dictionary D.
# D.keys() - returns a list of all the keys in the dictionary.
# D.values() - returns a list of all the values in the dictionary


# TODO: write a function that combines these two lists to form a dictionary
NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank', 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]


exit()


# TODO: organize the dog breeds by group. Find the group with the most breeds


exit()


# TODO: use a map to make our fib function super fast


exit()
