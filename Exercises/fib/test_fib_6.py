"""
- [x] fib(0) = 0
- [x] fib(1) = 1
- [x] fib(n+2) = fib(n+1) + fib(n) + 1 (n ≧ 0)

- [x] リファクタリング
"""
import pytest


def fib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


@pytest.mark.parametrize(['test_input', 'expected'], [
    (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5)
])
def test_fibonacci(test_input, expected):
    assert expected == fib(test_input)
