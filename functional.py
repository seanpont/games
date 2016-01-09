def append(xs, x):
    """
    :param xs: a list of items
    :param x: the item that should be appended
    :return: the list with the item appended
    """
    xs.append(x)
    return xs


def set_on(m, key, value):
    """
    :param m: a map
    :param key: the key to add
    :param value: the value to add
    :return: the map with the key set to the value
    """
    m[key] = value
    return m


def add(s, val):
    """
    :param s: a set of items
    :param val: the item to add
    :return: the set
    """
    s.add(val)
    return s

def flip_map(m):
    """
    :param m: a map
    :return: a map of values to list of keys
    """
    return reduce(lambda m, kv:
                  set_on(m, kv[1], append(m.get(kv[1], []), kv[0])),
                  m.iteritems(), {})


assert flip_map({'a': 1, 'b': 2, 'c': 1}) == {1: ['a', 'c'], 2: ['b']}


def memoize(fn):
    """Annotation for single-argument methods that memoizes results
    :param fn: The single-argument function to memoize
    """
    memo = {}

    def memoized(x):
        if x in memo:
            return memo[x]
        memo[x] = y = fn(x)
        return y

    return memoized


def group_by(xs, key_fn, val_fn = lambda val: val):
    """Return a map where the keys are fn(x) and value is a list of x

    >>> group_by([(1, 2), (1, 3), (2, 3), (1, 4)], lambda x: x[0])
    {1: [(1, 2), (1, 3), (1, 4)], 2: [(2, 3)]}

    >>> group_by([(1, 2), (1, 3), (2, 3), (1, 4)], lambda x: x[0], lambda y: y[1])
    {1: [2, 3, 4], 2: [3]}

    """
    def group(m, x):
        key = key_fn(x)
        return set_on(m, key, append(m.get(key, []), val_fn(x)))

    return reduce(group, xs, {})


if __name__ == '__main__':
    import doctest
    doctest.testmod()


def count(target, xs):
    """
    :param target: item to count instanes of
    :param xs: items
    :return: number of instances of target in xs
    >>> count(1, [1,2,1,3,1])
    3
    >>> count(1, range(4, 6))
    0
    """
    return reduce(lambda c, x: c + 1 if x == target else c, xs, 0)


def if_none(x, fn):
    """
    return x if x is not None, else return value returned by function fn
    :param x: the value, or None
    :param fn: a function to call if x is None
    :return: x or fn()
    >>> if_none(5, list)
    5
    >>> if_none(None, list)
    []
    """
    return x if x is not None else fn()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
