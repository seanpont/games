from lesson_20160123 import Item, ITEMS, greedy_solution


# WARM UP
# TODO: Find the items with the highest and lowest value densities.
# TODO: Sort items by value density (value / weight). Density should be a float.

def density_of(item):
    return item.value / item.weight

chair = Item('chair', 20, 30)
print 'density of chair:', density_of(chair)


# Functions that return more than one value.
# TODO: Function that returns the sum and the product of two numbers

def sum_and_product(a, b, c):
    return a + b + c, a * b + c

foo, bar = sum_and_product(4, 7, 3)

# Recursion, Path Finding
# TODO: Find the optimal solution to the 0/1 Knapsack Problem


def recursive_solution(items, max_weight):
    if not items:
        return 0, ()
    first, rest = items[0], items[1:]
    value_with, items_with = 0, ()
    if first.weight <= max_weight:
        value_with, items_with = recursive_solution(rest, max_weight - first.weight)
        value_with += first.value
        items_with += (first,)
    value_without, items_without = recursive_solution(rest, max_weight)
    if value_with > value_without:
        return value_with, items_with
    else:
        return value_without, items_without


print 'recursive solution:', recursive_solution(ITEMS, 20)



