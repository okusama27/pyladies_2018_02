"""
FizzBuzz.

- [x] 数字を文字列で返す
  - [x] 1を渡したら文字列"1"を返す
  - [x] 2を渡したら文字列"2"を返す
ただし、
- [X] 3で割り切れる数の場合は「Fizz」と返す
- [x] 5で割り切れる数の場合は「Buzz」と返す
- [x] 3と5で割り切れる数の場合は「FizzBuzz」と返す

- [x] リファクタリング
"""
import pytest


def fizz_buzz(num):
    """FizzBuzz."""
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return str(num)


@pytest.mark.parametrize(['test_input', 'expected'], [
    (1, "1"), (2, "2"),
    (3, "Fizz"), (6, "Fizz"),
    (5, "Buzz"), (10, "Buzz"),
    (15, "FizzBuzz"), (30, "FizzBuzz")
])
def test_fizzbuzz(test_input, expected):
    assert fizz_buzz(test_input) == expected


# 参照
# http://note.crohaco.net/2016/python-pytest/#pytest-marker-parametrize

# def test_fizzbuzz_1():
#     """1を渡したら文字列1を返すテスト."""
#     assert "1" == fizz_buzz(1)
#
#
# def test_fizzbuzz_2():
#     """2を渡したら2を返すのを確認するテスト."""
#     assert "2" == fizz_buzz(2)
#
#
# def test_fizzbuzz_3():
#     """3を渡したらFizzを返すのを確認するテスト."""
#     assert "Fizz" == fizz_buzz(3)
#
#
# def test_fizzbuzz_6():
#     """6を渡したらFizzを返すのを確認するテスト."""
#     assert "Fizz" == fizz_buzz(6)
#
#
# def test_fizzbuzz_5():
#     """5を渡したらBuzzを返すのを確認するテスト."""
#     assert "Buzz" == fizz_buzz(5)
#
#
# def test_fizzbuzz_10():
#     """5を渡したらBuzzを返すのを確認するテスト."""
#     assert "Buzz" == fizz_buzz(10)
#
#
# def test_fizzbuzz_15():
#     """15を渡したらFizzBuzzを返すのを確認するテスト."""
#     assert "FizzBuzz" == fizz_buzz(15)
#
#
# def test_fizzbuzz_30():
#     """30を渡したらFizzBuzzを返すのを確認するテスト."""
#     assert "FizzBuzz" == fizz_buzz(30)
