# WARM-UP

# TODO: Write a function that takes a list of ints and returns only the odd ones
# Example: odd_filter([1,2,3,4,5]) == [1,3,5]
# Remember: a number n is odd if n % 2 == 1


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


# INTRODUCTION TO CLASSES


class Person(object):
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.skills = {}

    def name(self):
        return self.first_name + ' ' + self.last_name

    def greeting(self):
        return 'Hi, my name is ', self.name(), "and I'm", self.age, 'years old.'

    def age_by(self, years):
        self.age += years

    def practice(self, skill, hours):
        self.skills[skill] = self.skills.get(skill, 0) + hours

    def __str__(self):
        return self.name

    def best_skill(self):
        return max(self.skills.iteritems(), key=lambda x: x[1])


sean = Person("Sean", "Pont", 30)
cedric = Person("Cedric", "Oltramare", 14)
alexia = Person("Alexia", "Oltramare", 10)

print sean.greeting()
print cedric.greeting()

sean.age_by(1)
print sean.greeting()

sean.practice('running', 2)
sean.practice('programming', 8)
sean.practice('running', 1)
sean.practice('programming', 8)
sean.practice('basket weaving', 1)
print "Sean's best skill:", sean.best_skill()


# TODO: create a store class.
# The store will have an inventory of items.
# Items have prices.
# Create functions that allow us to stock items, set prices, and buy items.
# Explore inheritance by creating different types of stores
# Explore composition by splitting the store up into an inventory, storefront...


