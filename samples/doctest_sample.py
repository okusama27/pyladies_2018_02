"""
値を1増加させる関数です
>>> add_one(1)
2
"""


def add_one(x):
    """
    値が1増加します
    >>> [add_one(x) for x in range(5)]
    [1, 2, 3, 4, 5]
    """
    return x + 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
