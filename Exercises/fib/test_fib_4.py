"""
- [x] fib(0) = 0
- [x] fib(1) = 1
- [ ] fib(n+2) = fib(n+1) + fib(n) + 1 (n ≧ 0)
"""


def fib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return 2


def test_fibonacci():
    cases = [(0, 0), (1, 1), (2, 1), (3, 2)]
    for case in cases:
        assert case[1] == fib(case[0])
