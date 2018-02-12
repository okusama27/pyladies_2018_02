"""
- [x] 3で割り切れる数の場合は「Fizz」と返す
- [x] 5で割り切れる数の場合は「Buzz」と返す
- [ ] 3と5で割り切れる数の場合は「FizzBuzz」と返す
- [ ] 3でも5でも割り切れない数の場合は、その数をそのまま返す
"""


class FizzBuzz:
    def call(self, num):
        if num % 3 == 0:
            return "Fizz"
        if num % 5 == 0:
            return "Buzz"


def test_call_fizz():
    fizzbuzz = FizzBuzz()
    result_3 = fizzbuzz.call(3)
    assert "Fizz" == result_3
    result_6 = fizzbuzz.call(6)
    assert "Fizz" == result_6


def test_call_buzz():
    fizzbuzz = FizzBuzz()
    result_5 = fizzbuzz.call(5)
    assert "Buzz" == result_5
    result_10 = fizzbuzz.call(10)
    assert "Buzz" == result_10
