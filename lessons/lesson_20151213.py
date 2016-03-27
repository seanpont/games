from test_utils import assert_equal


# TODO: write a function that returns the intersection of two lists
# (all the elements that are common in both groups)
def intersect(l1, l2):
    xs = []
    for x in l1:
        if x in l2:
            xs.append(x)
    return xs


# TODO: Write some tests for the intersect function
assert_equal([1, 2, 3], intersect([1, 2, 3, 4, 5, 6], [3, 2, 1]))


# TODO: Rewrite the intersection function using list comprehension

def intersect2(l1, l2):
    return [x for x in l1 if x in l2]


# TODO: Write a function that takes an integer n and uses List Comprehension to
# return a list of all the divisors of n

def divisors(n):
    return [x for x in range(1, n + 1) if n % x == 0]


assert_equal([1, 2, 3, 4, 6, 12], divisors(12))

# DICTIONARIES

# D = {key1:value1, ...} creates a non-empty dictionary
# D[key] returns the value thats mapped to by key.
# (What if there's no such key?)
# D[key] = value maps newvalue to key. Overwrites any previous value.
# Remember - newvalue can be any valid Python data structure.
# del D[key] deletes the mapping with that key from D.
# len(D) returns the number of entries (mappings) in D.
# x in D, x not in D checks whether the key x is in the dictionary D.
# D.keys() - returns a list of all the keys in the dictionary.
# D.values() - returns a list of all the values in the dictionary


# TODO: write a function that combines these two lists to form a dictionary
NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank', 'Gary', 'Helen',
         'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]


def combine_names_ages(names, ages):
    return {name: age for name, age in zip(names, ages)}


# TODO: write a function takes a map of names and ages and increments
# everyone's age by 1.

def increment_ages(names_ages):
    for name in names_ages:
        names_ages[name] += 1
    return names_ages


assert_equal({'bob': 20, 'sue': 32}, increment_ages({'bob': 19, 'sue': 31}))


