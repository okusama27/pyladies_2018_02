"""
- [x] 3で割り切れる数の場合は「Fizz」と返す
- [ ] 5で割り切れる数の場合は「Buzz」と返す
- [ ] 3と5で割り切れる数の場合は「fizz_buzz」と返す
- [ ] 3でも5でも割り切れない数の場合は、その数をそのまま返す
"""


def fizz_buzz(num):
    return "Fizz"


# 3で割り切れる数の場合は「Fizz」と返すか確認
def test_fizz():
    result_3 = fizz_buzz(3)
    assert "Fizz" == result_3
    result_6 = fizz_buzz(6)
    assert "Fizz" == result_6
