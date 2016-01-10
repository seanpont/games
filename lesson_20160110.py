from test_utils import assert_equal

# WARM-UP

# TODO: Write a function that takes a list of ints and returns only the odd ones
# Example: odd_filter([1,2,3,4,5]) == [1,3,5]
# Remember: a number n is odd if n % 2 == 1


def odd_filter(xs):
    return [x for x in xs if x % 2 == 1]


assert_equal(odd_filter(range(1, 6)), [1, 3, 5])


# TODO: Write a function that can read roman numerals
# https://en.wikipedia.org/wiki/Roman_numerals
# Example: roman_numerals_to_int('XIV') == 14
# Important string methods: count, replace

NUMERALS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}
SPECIAL_NUMERALS = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900}


def roman_numerals_to_int(numerals):
    """
    :type numerals: str
    """
    res = sum((SPECIAL_NUMERALS[sn] * numerals.count(sn)
               for sn in SPECIAL_NUMERALS))
    numerals = reduce(lambda a, b: a.replace(b, ''), SPECIAL_NUMERALS.keys(), numerals)
    return res + sum((NUMERALS[n] * numerals.count(n) for n in NUMERALS))


assert_equal(14, roman_numerals_to_int('XIV'))


# INTRODUCTION TO CLASSES


class Person(object):
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def name(self):
        return self.first_name + ' ' + self.last_name

    def say_hello(self):
        print 'Hi, my name is ', self.name(), "and I'm", self.age, 'years old.'

    def age_by(self, years):
        self.age += years

    def __str__(self):
        return self.name


sean = Person("Sean", "Pont", 30)
cedric = Person("Cedric", "Oltramare", 14)
alexia = Person("Alexia", "Oltramare", 10)

sean.say_hello()
cedric.say_hello()

sean.age_by(1)
sean.say_hello()


# TODO: create a store class.
# The store will have an inventory of items.
# Items have prices.
# Create functions that allow us to stock items, set prices, and buy items.
# Explore inheritance by creating different types of stores
# Explore composition by splitting the store up into an inventory, storefront...





