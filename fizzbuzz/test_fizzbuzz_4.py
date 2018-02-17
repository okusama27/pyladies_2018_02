"""
FizzBuzz.

- [x] 3で割り切れる数の場合は「Fizz」と返す
- [x] 5で割り切れる数の場合は「Buzz」と返す
- [x] 3と5で割り切れる数の場合は「FizzBuzz」と返す
- [x] 3でも5でも割り切れない数の場合は、その数の文字列を返す
"""


def fizz_buzz(num):
    """FizzBuzz."""
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return str(num)


def test_fizz():
    """3で割り切れる数の場合は「Fizz」と返すか確認するテスト."""
    result_3 = fizz_buzz(3)
    assert "Fizz" == result_3
    result_6 = fizz_buzz(6)
    assert "Fizz" == result_6


def test_buzz():
    """5で割り切れる数の場合は「Buzz」と返すか確認するテスト."""
    result_5 = fizz_buzz(5)
    assert "Buzz" == result_5
    result_10 = fizz_buzz(10)
    assert "Buzz" == result_10


def test_fizz_buzz():
    """3と5で割り切れる数の場合は「FizzBuzz」と返すか確認するテスト."""
    result_15 = fizz_buzz(15)
    assert "FizzBuzz" == result_15
    result_30 = fizz_buzz(30)
    assert "FizzBuzz" == result_30


def test_not_fizz_buzz():
    """3でも5でも割り切れない数の場合は、その数をそのまま返すか確認するテスト."""
    result_2 = fizz_buzz(2)
    assert "2" == result_2
    result_14 = fizz_buzz(14)
    assert "14" == result_14
