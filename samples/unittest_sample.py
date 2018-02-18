from unittest import TestCase


def add_one(num):
    """引数に1足した値を返す関数."""
    return num + 2


class TestAddOne(TestCase):
    """関数add_oneのテスト."""

    def test_add_one(self):
        """数が1増加するか確認するテスト."""
        expected = 2  # 期待する結果
        actual = add_one(1)  # 実際の結果

        # 比較
        self.assertEquals(expected, actual)
