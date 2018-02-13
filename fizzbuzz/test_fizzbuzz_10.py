"""
- [x] 3で割り切れる数の場合は「Fizz」と返す
- [x] 5で割り切れる数の場合は「Buzz」と返す
- [x] 3と5で割り切れる数の場合は「FizzBuzz」と返す
- [x] 3でも5でも割り切れない数の場合は、その数をそのまま返す
- [x] リファクタリング

- [x] 7で割り切れる数の場合は「Hoge」と返す
- [x] 3と7で割り切れる数の場合は「FizzHoge」と返す
- [x] 5と7で割り切れる数の場合は「BuzzHoge」と返す
- [x] 3と5と7で割り切れる数の場合は「FizzBuzzHoge」と返す
- [x] 3でも5でも7でも割り切れない数の場合は、その数をそのまま返す
"""


def fizz_buzz(num):
    res = ""
    if num % 3 == 0:
        res += "Fizz"
    if num % 5 == 0:
        res += "Buzz"
    if num % 7 == 0:
        res += "Hoge"
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


# 3でも5でも7でも割り切れない数の場合は、その数をそのまま返すか確認
def test_not_fizz_buzz():
    check_fizz_buzz(2, "2")
    check_fizz_buzz(13, "13")

# 7で割り切れる数の場合は「Hoge」と返すか確認
def test_hoge():
    check_fizz_buzz(7, "Hoge")
    check_fizz_buzz(14, "Hoge")


# 3と7で割り切れる数の場合は「FizzHoge」と返すか確認
def test_fizz_hoge():
    check_fizz_buzz(21, "FizzHoge")
    check_fizz_buzz(42, "FizzHoge")


# 5と7で割り切れる数の場合は「Buzz」と返すか確認
def test_buzz_hoge():
    check_fizz_buzz(35, "BuzzHoge")
    check_fizz_buzz(70, "BuzzHoge")


# 3と5と7で割り切れる数の場合は「FizzBuzzHoge」と返すか確認
def test_fizz_buzz_hoge():
    check_fizz_buzz(105, "FizzBuzzHoge")
    check_fizz_buzz(210, "FizzBuzzHoge")
