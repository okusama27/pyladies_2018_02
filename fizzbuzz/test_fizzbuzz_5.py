"""
FizzBuzz.

- [x] 3で割り切れる数の場合は「Fizz」と返す
- [x] 5で割り切れる数の場合は「Buzz」と返す
- [x] 3と5で割り切れる数の場合は「FizzBuzz」と返す
- [x] 3でも5でも割り切れない数の場合は、その数をそのまま返す
- [x] リファクタリング
"""


def fizz_buzz(num):
    """FizzBuzz."""
    res = ""
    if num % 3 == 0:
        res += "Fizz"
    if num % 5 == 0:
        res += "Buzz"
    if not res:
        res = str(num)
    return res


def check_fizz_buzz(num, expected):
    """テストを実施する関数."""
    actual = fizz_buzz(num)
    assert expected == actual


def test_fizz():
    """3で割り切れる数の場合は「Fizz」と返すか確認するテスト."""
    check_fizz_buzz(3, "Fizz")
    check_fizz_buzz(6, "Fizz")


def test_buzz():
    """5で割り切れる数の場合は「Buzz」と返すか確認するテスト."""
    check_fizz_buzz(5, "Buzz")
    check_fizz_buzz(10, "Buzz")


def test_fizz_buzz():
    """3と5で割り切れる数の場合は「FizzBuzz」と返すか確認するテスト."""
    check_fizz_buzz(15, "FizzBuzz")
    check_fizz_buzz(30, "FizzBuzz")


def test_not_fizz_buzz():
    """3でも5でも割り切れない数の場合は、その数をそのまま返すか確認するテスト."""
    check_fizz_buzz(2, "2")
    check_fizz_buzz(14, "14")
