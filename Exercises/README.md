# 演習

## FizzBuzzHoge

作成したFizzBuzzに7で割り切れる数の場合に「Hoge」と返す処理を追加しましょう

[test_fizzbuzz.py](fizzbuzzhoge/test_fizzbuzz.py) に書き足しましょう。

TODO
- [x] 3で割り切れる数の場合は「Fizz」と返す
- [x] 5で割り切れる数の場合は「Buzz」と返す
- [ ] 7で割り切れる数の場合は「Hoge」と返す
- [x] 3と5で割り切れる数の場合は「FizzBuzz」と返す
- [ ] 3と7で割り切れる数の場合は「FizzHoge」と返す
- [ ] 5と7で割り切れる数の場合は「BuzzHoge」と返す
- [ ] 3と5と7で割り切れる数の場合は「FizzBuzzHoge」と返す
- [ ] 3でも5でも7でも割り切れない数の場合は、その数の文字列を返す

解答は [test_fizzbuzzhoge.py](fizzbuzzhoge/test_fizzbuzzhoge.py) 

## フィボナッチ数

参照: [フィボナッチ数 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A3%E3%83%9C%E3%83%8A%E3%83%83%E3%83%81%E6%95%B0)

```text
n 番目のフィボナッチ数を Fn で表すと、Fn は再帰的に

F0 = 0,
F1 = 1,
Fn + 2 = Fn + Fn + 1 (n ≧ 0)

で定義される。これは、2つの初期条件を持つ漸化式である。
```

n番目のフィボナッチ数を返す関数 `fub(n)` を作りましょう。

TODO
- [ ] fib(0) = 0
- [ ] fib(1) = 1
- [ ] fib(n+2) = fib(n+1) + fib(n) + 1 (n ≧ 0)