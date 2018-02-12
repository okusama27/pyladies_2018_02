"""
- [x] 3で割り切れる数の場合は「Fizz」と返す
- [ ] 5で割り切れる数の場合は「Buzz」と返す
- [ ] 3と5で割り切れる数の場合は「FizzBuzz」と返す
- [ ] 3でも5でも割り切れない数の場合は、その数をそのまま返す
"""

class FizzBuzz:
    def call(self, num):
        return "Fizz"


def test_call_fizz():
    fizzbuzz = FizzBuzz()
    result_3 = fizzbuzz.call(3)
    assert "Fizz" == result_3
    result_6 = fizzbuzz.call(6)
    assert "Fizz" == result_6
