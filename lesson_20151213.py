# TODO: write a function that returns the intersection of two lists
# (all the elements that are common in both groups)
def intersect(l1, l2):
    print l1
    print l2


intersect([1,2,3], [2,3,4])

# TODO: Write some tests for the intersect function


# TODO: Rewrite the intersection function using list comprehension

def intersect2(l1, l2):
    return [x for x in l1 if x in l2]


# TODO: Write a function that takes an integer n and uses List Comprehension to
# return a list of all the divisors of n


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
NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank', 'Gary', 'Helen',
         'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

names_ages = {name: age for name, age in zip(NAMES, AGES)}

print names_ages
print "Kelly is %s years old" % names_ages['Kelly']



# TODO: write a function that will increment everyone's age by 1.


# INTRODUCTION TO CLASSES


# TODO: create a store. The store will have an inventory of items. Items have
# prices. Create functions that allow us to stock items, set prices, and
# buy items.
# Explore inheritance by creating different types of stores
# Explore composition by splitting the store up into an inventory, storefront...

a = {1: 1, 2: 4}
print a.get(1)
print a.get(2)

inventory = {}
prices = {}

inventory['shoes'] = 12
print inventory
prices['shoes'] = '$100'
print prices





