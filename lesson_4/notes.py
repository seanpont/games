"""
Review: Objects (literals), Expressions, Conditionals, and Loops
New: Data structures! Tuples, lists, and maps
Project: Improve Dog Breed picker app
"""


def is_divisible(number, divisor):
    """
    Review: Objects (literals) and conditionals

    If number is divisible by divisor, print <number> is divisible by <divisor>
    Otherwise, print <number> is not divisible by <divisor>
    This function will use an if statement and the mod function (%)
    To concat (put together) strings, use the + function
    You will need to turn the ints into strings by using the str() function

    hint:
    if ...:
        print str(number) + " is divisible by " + str(divisor)
    else:
        ...
    """
    if number % divisor == 0:
        print str(number) + " is divisible by " + str(divisor)
    else:
        print str(number) + " is not divisible by " + str(divisor)


# print 'Testing is_divisible:'
# is_divisible(8, 2)
# is_divisible(8, 3)
# is_divisible(121, 11)
# is_divisible(571326516, 548298)


def number_of_divisors(number):
    """
    Review: Looping constructs

    Returns the number of divisors of number
    :param number: a number greater than 0
    :return: the number of divisors

    We will need to use a loop to iterate through all the numbers less than n
    We can use the range(n) function to enumerate all the numbers less than n
    We will use the special 'return' keyword to return the answer to the caller
    hint:
    num_divisors = 0
    for divisor in range(number):
        ...
    return num_divisors
    """
    num_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            num_divisors += 1
    return num_divisors


# print 'Testing number_of_divisors:'
# print '%s has %s divisors' % (8, number_of_divisors(8))
# print '%s has %s divisors' % (49, number_of_divisors(49))
# print '%s has %s divisors' % (112, number_of_divisors(112))


def sign_of_number(number):
    pass



def starts_with(word):
    print word + ' starts with ' + word[0]
    print word + ' ends with ' + word[len(word)-1]


"""
Data Structures: Tuples, Lists, and Maps

Tuples
    Ordered List of items
    Can contain anything
    Can get items by index using []
    Slices
"""
# t = (1, 2, 3, 4, 5)
# print t[0]
# print t[1]
#
# x = 100
# divisors = ()
# for i in range(1,x):
#     if x%i == 0:
#         divisors = divisors + (i,)
# print divisors

"""
Lists
    More useful than tuples, but more complicated
    First mutable object we've looked at
    append() is a method
        like having a function that uses the list as the first argument
    append mutates the list -- different than creating a copy



"""
# dogs = ['Retriever', 'Pointer', 'Hound']
# print dogs
# dogs.append('Terrier')
# print dogs
# print dogs[1]
# for dog in dogs[:2]:
#     print dog

"""
We can concatenate lists using the + operator.
We can remove items using the
"""
# cats = ["Furry", "Hairless"]
# dogs_and_cats = dogs + cats
# print dogs_and_cats
# dogs_and_cats.remove('Pointer')
# print dogs_and_cats

"""
The assignment operator "=" modifies items in the list
"""
# dogs[0] = "Sheep Dog"
# print dogs

"""
We can sort the items using the sort() function
This too has the side-effect of changing the list
"""
# dogs_and_cats.sort()
# print dogs_and_cats

"""
Having mutable objects is useful, but it can also be DANGEROUS!
If you have multiple pointers to the same list, mutating one will cause the
other to change
"""

# L1 = [2]
# L2 = [L1, L1]
# print 'L2 =', L2
# L1[0] = 3
# print 'L2 =', L2
# L2[0] = 'a'
# print 'L2 =', L2
#
# L1 = [2]
# print 'L2 =', L2
# L2 = L1
# L2[0] = 'a'
# print 'L1 =', L1
# print 'L2 =', L2
#
# L1 = [2]
# L2 = L1[:]
# L2[0] = 'a'
# print 'L1 =', L1
#
# def copy_list(source, dest):
#     for e in source:
#         dest.append(e)
#         print 'LDest =', dest
#
# L1 = []
# L2 = [1,2,3]
# copy_list(L2,L1)
# print L1
# print L2
## copy_list(L1, L1)
## print L1


"""
Maps
    Unordered
    Set of key-value pairs
    The keys need not be integers!
    They can be any immutable type
        ie it can be a string or a tuple, but not a list or a map
    The values can be anything (mutable or immutable)
"""

# EtoF = {'bread': 'du pain',
#         'wine': 'du vin',
#         'eats': 'mange',
#         'drinks': 'bois',
#         'likes': 'aime',
#         1: 'un',
#         '6.00': '6.00'}
# print EtoF
# print EtoF.keys()
# print EtoF.keys
# del EtoF[1]
# print EtoF

"""
We can modify the map by using the assignment operator '='
Delete items using the del keyword
Because maps are mutable, you need to be careful when you have two references
to the same map!
"""
# D = {1: 'one', 'deux': 'two', 'pi': 3.14159}
# D1 = D
# print D1
# D[1] = 'uno'
# del D1['deux']
# print D1
# for k in D1.keys():
#     print k, '=', D1[k]
#
#
# def translate_word(word, dictionary):
#     if word in dictionary:
#         return dictionary[word]
#     else:
#         return word
#
#
# def translate(sentence):
#     translation = ''
#     word = ''
#     for c in sentence:
#         if c != ' ':
#             word = word + c
#         else:
#             translation = translation + ' '\
#                           + translate_word(word, EtoF)
#             word = ''
#     return translation[1:] + ' ' + translate_word(word, EtoF)
#
# print translate('John eats bread')
# print translate('Steve drinks wine')
# print translate('John likes 6.00')

