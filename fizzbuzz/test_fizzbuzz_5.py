"""
- [x] 3で割り切れる数の場合は「Fizz」と返す
- [x] 5で割り切れる数の場合は「Buzz」と返す
- [x] 3と5で割り切れる数の場合は「FizzBuzz」と返す
- [x] 3でも5でも割り切れない数の場合は、その数をそのまま返す
- [x] リファクタリング
"""


def fizz_buzz(num):
    res = ""
    if num % 3 == 0:
        res += "Fizz"
    if num % 5 == 0:
        res += "Buzz"
    if not res:
        res = str(num)
    return res


# テストを実施
def check_fizz_buzz(num, expected):
    actual = fizz_buzz(num)
    assert expected == actual


# 3で割り切れる数の場合は「Fizz」と返すか確認
def test_fizz():
    check_fizz_buzz(3, "Fizz")
    check_fizz_buzz(6, "Fizz")


# 5で割り切れる数の場合は「Buzz」と返すか確認
def test_buzz():
    check_fizz_buzz(5, "Buzz")
    check_fizz_buzz(10, "Buzz")


# 3と5で割り切れる数の場合は「FizzBuzz」と返すか確認
def test_fizz_buzz():
    check_fizz_buzz(15, "FizzBuzz")
    check_fizz_buzz(30, "FizzBuzz")


# 3でも5でも割り切れない数の場合は、その数をそのまま返すか確認
def test_not_fizz_buzz():
    check_fizz_buzz(2, "2")
    check_fizz_buzz(14, "14")
