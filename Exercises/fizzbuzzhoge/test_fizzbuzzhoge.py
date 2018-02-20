"""
FizzBuzz.

- [x] 数字を文字列で返す
  - [x] 1を渡したら文字列"1"を返す
  - [x] 2を渡したら文字列"2"を返す
ただし、
- [X] 3で割り切れる数の場合は「Fizz」と返す
- [x] 5で割り切れる数の場合は「Buzz」と返す
- [x] 3と5で割り切れる数の場合は「FizzBuzz」と返す

- [x] 7で割り切れる数の場合は「Hoge」と返す
- [x] 3と7で割り切れる数の場合は「FizzHoge」と返す
- [x] 5と7で割り切れる数の場合は「BuzzHoge」と返す
- [x] 3と5と7で割り切れる数の場合は「FizzBuzzHoge」と返す
"""


def fizz_buzz(num):
    """FizzBuzz."""
    if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
        return "FizzBuzzHoge"
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0 and num % 7 == 0:
        return "FizzHoge"
    if num % 5 == 0 and num % 7 == 0:
        return "BuzzHoge"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 7 == 0:
        return "Hoge"
    return str(num)


def test_fizzbuzz_1():
    """1を渡したら文字列1を返すテスト."""
    assert "1" == fizz_buzz(1)


def test_fizzbuzz_2():
    """2を渡したら2を返すのを確認するテスト."""
    assert "2" == fizz_buzz(2)


def test_fizzbuzz_3():
    """3を渡したらFizzを返すのを確認するテスト."""
    assert "Fizz" == fizz_buzz(3)


def test_fizzbuzz_6():
    """6を渡したらFizzを返すのを確認するテスト."""
    assert "Fizz" == fizz_buzz(6)


def test_fizzbuzz_5():
    """5を渡したらBuzzを返すのを確認するテスト."""
    assert "Buzz" == fizz_buzz(5)


def test_fizzbuzz_10():
    """5を渡したらBuzzを返すのを確認するテスト."""
    assert "Buzz" == fizz_buzz(10)


def test_fizzbuzz_15():
    """15を渡したらFizzBuzzを返すのを確認するテスト."""
    assert "FizzBuzz" == fizz_buzz(15)


def test_fizzbuzz_30():
    """30を渡したらFizzBuzzを返すのを確認するテスト."""
    assert "FizzBuzz" == fizz_buzz(30)


def test_fizzbuzz_7():
    """7を渡したらHogeを返すのを確認するテスト."""
    assert "Hoge" == fizz_buzz(7)


def test_fizzbuzz_14():
    """14を渡したらHogeを返すのを確認するテスト."""
    assert "Hoge" == fizz_buzz(14)


def test_fizzbuzz_21():
    """21を渡したらFizzHogeを返すのを確認するテスト."""
    assert "FizzHoge" == fizz_buzz(21)


def test_fizzbuzz_35():
    """35を渡したらBuzzHogeを返すのを確認するテスト."""
    assert "BuzzHoge" == fizz_buzz(35)


def test_fizzbuzz_105():
    """105を渡したらFizzBuzzHogeを返すのを確認するテスト."""
    assert "FizzBuzzHoge" == fizz_buzz(105)
