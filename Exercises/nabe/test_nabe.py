"""世界のナベアツ
- [ ] 数字を渡すと、渡した数字を文字列で返す
ただし、
- [ ] 3の倍数のときは阿呆になるので、「さぁ〜ん」と文字列を返す
- [ ] 渡した数字に3が含まれるときは阿呆になるので、「さぁ〜ん」と文字列を返す
"""


def nabe(num):
    if num % 3 == 0:
        return "さぁ〜ん"
    if "3" in str(num):
        return "さぁ〜ん"
    return str(num)

for i in range(1, 101):
    print(nabe(i))


# 1のときは数字
def test_nabe_1():
    assert "1" == nabe(1)


# 3の倍数ときは「さぁ〜ん」
def test_nabe_3():
    assert "さぁ〜ん" == nabe(3)


# 3が含まれるときは「さぁ〜ん」
def test_nabe_13():
    assert "さぁ〜ん" == nabe(13)


