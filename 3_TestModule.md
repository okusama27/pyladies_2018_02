# Pythonの単体試験用モジュール

Pythonにはテストを行うためのツールがあります。

## doctest

標準ライブラリ。コメントやドキュメント中の実行例でテストを書く。

サンプル

[doctest_sample.py](./samples/doctest_sample.py)


実行

```bash
$ python doctest_sample.py -v
```

オプションvをつけると詳細を表示する。

参照
- [doctestを触ってみた](http://kamekokamekame.net/python/2017/12/10/article.html)


## unittest

標準ライブラリ。xUnit系。

サンプル

[unittest_sample.py](./samples/unittest_sample.py)

実行

```bash
$ python -m unittest unittest_sample.py
```

参考サイト: 
[26.4. unittest — ユニットテストフレームワーク](https://docs.python.org/ja/3/library/unittest.html)


## pytest

サードパーティー製のテストランナー。詳細なエラーレポートを表示するのが特徴。

インストール

```bash
$ pip install pytest
```

実行

```bash
$ python -m pytest pytest_sample.py
```

または、 `py.test` でも動きます。

```bash
$ py.test pytest_sample.py
```

いいところ

- ファイル名に `test_` とか、 `*_test` とかついていると探して実行してくれる。
- クラスを継承する必要が無いのでスッキリ書ける

## unittestとpytestの出力の違い

関数 `add_one` をわざと間違えます。 `return num + 2` と変更します。

- unittest

```bash
$ python -m unittest unittest_sample.py 
/Users/kaz/git/pyladies_2018_02/samples/unittest_sample.py:18: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(actual, expected)
F
======================================================================
FAIL: test_add_one (unittest_sample.TestAddOne)
数が1増加するか確認するテスト.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/kaz/git/pyladies_2018_02/samples/unittest_sample.py", line 18, in test_add_one
    self.assertEquals(expected, actual)
AssertionError: 2 != 3

----------------------------------------------------------------------
Ran 1 test in 0.002s

FAILED (failures=1)
```

- pytest


```bash
$ python -m pytest pytest_sample.py 
=========================================== test session starts ================================
platform darwin -- Python 3.5.0, pytest-3.4.0, py-1.5.2, pluggy-0.6.0
rootdir: /Users/kaz/git/pyladies_2018_02/samples, inifile:
collected 1 item                                                                                                                                                                                                                                             

pytest_sample.py F                                                                                                                                                                                                                                     [100%]

=========================================== FAILURES ===========================================
___________________________________________ test_add_one _______________________________________

    def test_add_one():
        """数が1増加するか確認するテスト."""
        expected = 2  # 期待する結果
        actual = add_one(1)  # 実際の結果
    
        # 比較
>       assert expected == actual
E       assert 2 == 3

pytest_sample.py:12: AssertionError
============================================ 1 failed in 0.08 seconds ===========================
```

