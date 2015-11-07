
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


def flip_map(m):
    """
    :param m: a map
    :return: a map of values to list of keys
    """
    return reduce(lambda m, kv:
                  set_on(m, kv[1], append(m.get(kv[1], []), kv[0])),
                  m.iteritems(), {})


assert flip_map({'a': 1, 'b': 2, 'c': 1}) == {1: ['a', 'c'], 2: ['b']}
