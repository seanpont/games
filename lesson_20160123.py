from test_utils import assert_equal
from collections import namedtuple

# THE KNAPSACK PROBLEM


class Item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = float(value)
        self.weight = float(weight)

    def __str__(self):
        return '%s: $%s %s oz' % (self.name, self.value, self.weight)

    def __repr__(self):
        return str(self)


some_items = [
    Item('book', 15, 2),
    Item('vase', 20, 4),
    Item('watch', 40, 1),
    Item('glasses', 30, 3),
    Item('computer', 100, 10),
    Item('bottle', 1, 1),
    Item('shoes', 12, 2)
]

print some_items






