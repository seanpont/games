# THE KNAPSACK PROBLEM!!!
# Objective:
# Maximize value subject to weight constraint


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def __str__(self):
        result = '<%s: $%s, %s lb>' % (self.name, self.value, self.weight)
        return result

    def __repr__(self):
        return self.__str__()


ITEMS = (
    #     name       value  weight
    Item('clock',     175,   10),
    Item('painting',  90,    9),
    Item('radio',     20,    4),
    Item('vase',      50,    2),
    Item('book',      10,    1),
    Item('computer',  200,   20),
)


# TODO: function that finds the total value and total weight


# TODO: function that takes a list of items and finds the most valuable


# TODO: function that takes a list of items and finds the heaviest


# TODO: function that sorts by value / weight


# TODO: write a function that finds the greedy solution to the knapsack problem


# TODO: Find the optimal solution






