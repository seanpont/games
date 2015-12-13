# coding=utf-8
from test_utils import assert_equal


# RECURSION

# TODO: write a function that returns the nth fibonacci number
def fib(n):
    print "fib(%s)" % n
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# for n in range(40):
#     print n, fib(n)

# fib(6)

# Tests for fib(n)
# assert_equal(fib(0), 1)
# assert_equal(fib(1), 1)
# assert_equal(fib(2), 2)
# assert_equal(fib(3), 3)
# assert_equal(fib(4), 5)
# assert_equal(fib(5), 8)


memo = {0: 1, 1: 1}


def fastfib(n):
    # print "fib(%s)" % n
    if n in memo:
        return memo[n]
    result = fastfib(n-1) + fastfib(n-2)
    memo[n]= result
    return result


# print fastfib(10)

# exit()


# LISTS
# Lists are defined by brackets

new_list = [3, 4, 5, 6]
print "new_list is:", new_list

# Just like strings, we can index & slice them
print "new_list[2] is:", new_list[0]
print "new_list[0:2] is:", new_list[2:9]

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
new_list.append(34)
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
