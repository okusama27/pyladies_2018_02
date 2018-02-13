"""
- [x] 3で割り切れる数の場合は「Fizz」と返す
- [x] 5で割り切れる数の場合は「Buzz」と返す
- [ ] 3と5で割り切れる数の場合は「FizzBuzz」と返す
- [ ] 3でも5でも割り切れない数の場合は、その数をそのまま返す
"""


def fizz_buzz(num):
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"


# 3で割り切れる数の場合は「Fizz」と返すか確認
def test_fizz():
    result_3 = fizz_buzz(3)
    assert "Fizz" == result_3
    result_6 = fizz_buzz(6)
    assert "Fizz" == result_6


# 5で割り切れる数の場合は「Buzz」と返すか確認
def test_buzz():
    result_5 = fizz_buzz(5)
    assert "Buzz" == result_5
    result_10 = fizz_buzz(10)
    assert "Buzz" == result_10
