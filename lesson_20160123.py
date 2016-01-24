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


def value_of(item):
    return item.value


def weight_of(item):
    return item.weight


# TODO: function that finds the total value and total weight

def get_total_value(items):
    total_value = 0
    for item in items:
        total_value += item.value
    return total_value

print 'total value:', get_total_value(ITEMS)


def get_total_weight(items):
    total_weight = 0
    for item in items:
        total_weight += item.weight
    return total_weight


print 'total weight:', get_total_weight(ITEMS)


# TODO: function that takes a list of items and finds the most valuable

def most_valuable(items):
    most_valuable_item = None
    highest_value = 0
    for item in items:
        if item.value > highest_value:
            most_valuable_item = item
            highest_value = item.value
    return most_valuable_item


def most_valuable2(items):
    return max(items, key=value_of)


print 'most valuable:', most_valuable(ITEMS)
print 'most valuable:', most_valuable2(ITEMS)

# TODO: function that takes a list of items and finds the heaviest


def heaviest(items):
    heaviest_item = None
    heaviest_item_weight = 0
    for item in items:
        if item.weight > heaviest_item_weight:
            heaviest_item = item
            heaviest_item_weight = item.weight
    return heaviest_item


def heaviest2(items):
    return max(items, key=weight_of)


print 'heaviest:', heaviest(ITEMS)
print 'heaviest2:', heaviest2(ITEMS)


# TODO: Sort the items by value and weight

print 'Sorted by value:', sorted(ITEMS, key=value_of)

print 'Sorted by weight:', sorted(ITEMS, key=weight_of)

print 'Sorted by value, descending:', sorted(ITEMS, key=value_of, reverse=True)


# TODO: write a function that finds the greedy solution to the knapsack problem


def greedy_solution(items, max_weight):
    items = sorted(items, key=value_of, reverse=True)
    total_weight = 0
    selected_items = []
    for item in items:
        if total_weight + item.weight <= max_weight:
            total_weight += item.weight
            selected_items.append(item)
    return selected_items


print 'greedy solution, 20:', greedy_solution(ITEMS, 20)
print 'greedy solution, 19:', greedy_solution(ITEMS, 19)
print 'greedy solution, 18:', greedy_solution(ITEMS, 18)
print 'greedy solution, 15:', greedy_solution(ITEMS, 15)
print 'greedy solution, 12:', greedy_solution(ITEMS, 12)
print 'greedy solution, 2:', greedy_solution(ITEMS, 2)


# TODO: Find the optimal solution






