# 作业 2：高阶函数

[hw02.zip](hw02.zip)

*截止时间：2月5日（周四）晚 11:59*

原文来源：<https://lr2933.github.io/cs61a-spring-2026/hw/hw02/index.html>

## 说明

下载 [hw02.zip](hw02.zip)。压缩包中有一个名为 [hw02.py](hw02.py) 的文件，以及一份
`ok` 自动评分器的副本。

**提交：** 完成后，请将作业提交到 Gradescope。在截止时间之前可以多次提交，只有最后一次提交
会被评分。请确认你的代码已成功提交到 Gradescope。

关于提交作业的更多说明，请参见
[Lab 0](https://lr2933.github.io/cs61a-spring-2026/lab/lab00.html)。

**使用 Ok：** 如果你对 Ok 的使用有任何疑问，请参阅
[本指南](https://lr2933.github.io/cs61a-spring-2026/articles/using-ok.html)。

**阅读材料：** 以下参考资料可能对你有帮助：

- [第 1.6 节](https://www.composingprograms.com/pages/16-higher-order-functions.html)

**评分：** 作业按正确性评分。每答错一题，总分扣一分。**本次作业满分为 2 分。**

## 必做题目

若干 doctest 会引用以下函数：

```python
from operator import add, mul

def square(x):
    return x * x

def identity(x):
    return x

def triple(x):
    return 3 * x

def increment(x):
    return x + 1
```

本作业的旧版本中，这些函数是用 lambda 表达式写的，原计划在
[周一的讲课视频](https://www.youtube.com/watch?v=vCeNq_P3akI&list=PL6BsET-8jgYXTuSlJNYQS740YMCRHT79g&index=5)
中讲解。如果你下载的是旧版本，可以把 `square`、`identity`、`triple` 和 `increment`
当作按上面这样定义即可。无论哪个版本，你需要写的代码都是一样的，提交旧版本也不会影响你的
自动评分成绩。

### 高阶函数

#### Q1: Product

编写一个名为 `product` 的函数，返回某个序列前 `n` 项的乘积。具体来说，`product` 接受一个整数
`n` 和一个单参数函数 `term`，后者确定一个序列（也就是说，`term(i)` 给出序列的第 `i` 项）。
`product(n, term)` 应返回 `term(1) * ... * term(n)`。

```python
def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term: a function that takes an index as input and produces a term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 测试你的代码：

```bash
python3 ok -q product
```

#### Q2: Accumulate

我们来看看 `product` 如何是更一般的函数 `accumulate` 的一个特例，下面我们想实现这个函数：

```python
def accumulate(fuse, start, n, term):
    """Return the result of fusing together the first n terms in a sequence
    and start.  The terms to be fused are term(1), term(2), ..., term(n).
    The function fuse is a two-argument commutative & associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11 (fuse is never used)
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    """
    "*** YOUR CODE HERE ***"
```

`accumulate` 有以下参数：

- `fuse`：一个双参数函数，指定当前项如何与之前累积的结果进行融合
- `start`：累积的起始值
- `n`：一个非负整数，表示要融合的项数
- `term`：一个单参数函数；`term(i)` 是序列的第 `i` 项

实现 `accumulate`，它用 `fuse` 函数把由 `term` 定义的序列的前 `n` 项与 `start` 值融合起来。

例如，`accumulate(add, 11, 3, square)` 的结果是

```text
add(11,  add(square(1), add(square(2),  square(3)))) =
    11 +     square(1) +    square(2) + square(3)    =
    11 +     1         +    4         + 9            = 25
```

> 假设 `fuse` 满足交换律 `fuse(a, b) == fuse(b, a)`，以及结合律
> `fuse(fuse(a, b), c) == fuse(a, fuse(b, c))`。

用 Ok 测试你的代码：

```bash
python3 ok -q accumulate
```

接下来，把 `summation`（课上讲过）和 `product` 实现为对 `accumulate` 的一行调用。

> **重要：** `summation_using_accumulate` 和 `product_using_accumulate` 都必须只用一行以
> `return` 开头的代码实现。

```python
def summation_using_accumulate(n, term):
    """Returns the sum: term(1) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square) # square(1) + square(2) + ... + square(4) + square(5)
    55
    >>> summation_using_accumulate(5, triple) # triple(1) + triple(2) + ... + triple(4) + triple(5)
    45
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return ____

def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square) # square(1) * square(2) * square(3) * square()
    576
    >>> product_using_accumulate(6, triple) # triple(1) * triple(2) * ... * triple(5) * triple(6)
    524880
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return ____
```

用 Ok 测试你的代码：

```bash
python3 ok -q summation_using_accumulate
python3 ok -q product_using_accumulate
```

#### Q3: Make Repeater

实现函数 `make_repeater`，它接受一个单参数函数 `f` 和一个正整数 `n`。它返回一个单参数函数，
使得 `make_repeater(f, n)(x)` 返回 `f(f(...f(x)...))` 的值，其中 `f` 对 `x` 应用了 `n` 次。
例如，`make_repeater(square, 3)(5)` 把 5 平方三次并返回 390625，就像
`square(square(square(5)))` 一样。

```python
def make_repeater(f, n):
    """Returns the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * (3 * (3 * (3 * (3 * 1))))
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 测试你的代码：

```bash
python3 ok -q make_repeater
```

### 在本地检查分数

你可以在本地检查本次作业每道题的得分，方法是运行

```bash
python3 ok --score
```

**这不会提交作业！** 当你对分数满意时，把作业提交到 Gradescope 才能拿到成绩。

## 提交作业

把任何你修改过的文件上传**到对应的 Gradescope 作业**来提交本次作业。
[Lab 00](https://lr2933.github.io/cs61a-spring-2026/lab/lab00.html) 有详细说明。

### [可选] 考试练习

以下是一些往年考试中的相关题目，供你练习。这些题目是可选的，无法提交。

1. Fall 2019 MT1 Q3：[You Again](https://lr2933.github.io/cs61a-spring-2026/exam/fa19/mt1/61a-fa19-mt1.pdf#page=4) [高阶函数]
2. Fall 2021 MT1 Q1b：[tik](https://lr2933.github.io/cs61a-spring-2026/exam/fa21/mt1/61a-fa21-mt1.pdf#page=4) [函数与表达式]
