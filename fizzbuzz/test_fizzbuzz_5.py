"""
- [x] 3で割り切れる数の場合は「Fizz」と返す
- [x] 5で割り切れる数の場合は「Buzz」と返す
- [x] 3と5で割り切れる数の場合は「FizzBuzz」と返す
- [x] 3でも5でも割り切れない数の場合は、その数をそのまま返す
- [x] リファクタリング
"""
import pytest


class FizzBuzz:

    def call(self, num):
        res = ""
        if num % 3 == 0:
            res += "Fizz"
        if num % 5 == 0:
            res += "Buzz"
        if not res:
            res = str(num)
        return res


@pytest.mark.skip(reason="This test is a parent test of all tests")
def test_call(num, expected):
    fizzbuzz = FizzBuzz()
    actual = fizzbuzz.call(num)
    assert expected == actual


def test_call_fizz():
    test_call(3, "Fizz")
    test_call(6, "Fizz")


def test_call_buzz():
    test_call(5, "Buzz")
    test_call(10, "Buzz")


def test_call_fizz_buzz():
    test_call(15, "FizzBuzz")
    test_call(30, "FizzBuzz")


def test_call_not_fizz_buzz():
    test_call(2, "2")
    test_call(14, "14")
