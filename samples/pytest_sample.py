def add_one(num):
    """引数に1足した値を返す関数."""
    return num + 2


def test_add_one():
    """数が1増加するか確認するテスト."""
    expected = 2  # 期待する結果
    actual = add_one(1)  # 実際の結果

    # 比較
    assert expected == actual
