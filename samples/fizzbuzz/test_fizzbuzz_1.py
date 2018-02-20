"""
FizzBuzz.

- [ ] 数字を文字列で返す
  - [x] 1を渡したら文字列"1"を返す
  - [ ] 2を渡したら文字列"2"を返す
ただし、
- [ ] 3で割り切れる数の場合は「Fizz」と返す
- [ ] 5で割り切れる数の場合は「Buzz」と返す
- [ ] 3と5で割り切れる数の場合は「FizzBuzz」と返す
"""


def fizz_buzz(num):
    """FizzBuzz."""
    return "1"


def test_fizzbuzz_1():
    """1を渡したら文字列1を返すテスト."""
    assert "1" == fizz_buzz(1)
