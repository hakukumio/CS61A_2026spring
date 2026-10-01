Homework 5 | CS 61A Spring 2026



[CS 61A](../../index.html "../../index.html")

* [Lectures](../../index.html "../../index.html")
* [Syllabus](../../articles/about-61a/index.html "../../articles/about-61a/index.html")
* [Ed](https://edstem.org/us/courses/93628/discussion "https://edstem.org/us/courses/93628/discussion")
* [Office Hours](../../office-hours.html "../../office-hours.html")
* [Contact](../../articles/contact-61a/index.html "../../articles/contact-61a/index.html")
* [Links](index.html# "index.html#")
  + [Request an Extension](https://go.cs61a.org/extensions "https://go.cs61a.org/extensions")
  + [Request a Regrade](https://go.cs61a.org/regrades "https://go.cs61a.org/regrades")
  + [Office Hours Queue](https://oh.cs61a.org/ "https://oh.cs61a.org/")
  + [Gradescope](https://www.gradescope.com/courses/1229052 "https://www.gradescope.com/courses/1229052")
  + [Add/Change Sections](https://sections.cs61a.org "https://sections.cs61a.org")
  + [Lecture Recordings](https://bcourses.berkeley.edu/courses/1547573/pages "https://bcourses.berkeley.edu/courses/1547573/pages")
  + [Python Tutor](https://pythontutor.com/cp/composingprograms.html "https://pythontutor.com/cp/composingprograms.html")
  + [Code Editors](https://code.cs61a.org/ "https://code.cs61a.org/")
* [Resources](index.html# "index.html#")
  + [Past Exams & Websites](../../resources.html "../../resources.html")
  + [Textbook](https://www.composingprograms.com "https://www.composingprograms.com")
  + [Campus Resources](../../articles/campus-res/index.html "../../articles/campus-res/index.html")
  + [Advice from Students](../../articles/advice/index.html "../../articles/advice/index.html")
  + [Scheme Specifications](../../articles/scheme-spec/index.html "../../articles/scheme-spec/index.html")
  + [Scheme Built-In Procedures](../../articles/scheme-builtins/index.html "../../articles/scheme-builtins/index.html")
* [Guides](index.html# "index.html#")
  + [Debugging Guide](https://drive.google.com/file/d/1O72u0ml65pibcjz-PXKpqeJDKaVqQ3D8/view "https://drive.google.com/file/d/1O72u0ml65pibcjz-PXKpqeJDKaVqQ3D8/view")
  + [Studying Guide](../../articles/studying/index.html "../../articles/studying/index.html")
  + [Type Hints](../../articles/type-hints.html "../../articles/type-hints.html")
  + [Composition Guide](../../articles/composition/index.html "../../articles/composition/index.html")
  + [MT1 Study Guide](../../assets/pdfs/61a-mt1-study-guide.pdf "../../assets/pdfs/61a-mt1-study-guide.pdf")
  + [MT2 Study Guide](../../assets/pdfs/61a-mt2-study-guide.pdf "../../assets/pdfs/61a-mt2-study-guide.pdf")
  + [Final Study Guide](../../assets/pdfs/61a-final-study-guide.pdf "../../assets/pdfs/61a-final-study-guide.pdf")
* [Staff](index.html# "index.html#")
  + [Instructors](../../instructor.html "../../instructor.html")
  + [TAs & Tutors](../../staff.html "../../staff.html")
  + [Teaching Interns](../../teaching-interns.html "../../teaching-interns.html")



Homework 5: Generators

* [hw05.zip](hw05.zip "hw05.zip")
=========================================================

*截止时间为 3 月 12 日（周四）晚上 11:59。*

Instructions
------------

下载 [hw05.zip](hw05.zip "hw05.zip")。在该压缩包中，你会找到一个名为 [hw05.py](hw05.py "hw05.py") 的文件，以及一份 `ok` autograder 的副本。

**提交：** 完成后，请把作业提交到 Gradescope。你可以在截止时间前多次提交；只有最后一次提交会被计分。请检查你是否已经在 Gradescope 上成功提交了你的代码。提交作业的更多说明见 [Lab 0](../../lab/lab00.html "../../lab/lab00.html")。

**使用 Ok：** 如果你对使用 Ok 有任何疑问，请参考[这份指南。](../../articles/using-ok.html "../../articles/using-ok.html")

**阅读材料：** 你可能会觉得以下参考资料很有用：

* [Section 4.2](https://www.composingprograms.com/pages/42-implicit-sequences.html "https://www.composingprograms.com/pages/42-implicit-sequences.html")

**评分：** Homework 依据正确性评分。每答错一道题，总分就会减少一分。**这份 homework 满分为 2 分。**

Required Questions
==================

Generators
----------

如果你需要复习 generators，阅读以下内容可能会有所帮助：
  

Generators (enable JavaScript)

我们可以通过编写 *generator function* 来创建自己的自定义 iterators，它返回一种特殊类型的 iterator，称为 **generator**。Generator functions 在函数体中使用 `yield` 语句而不是 `return` 语句。调用一个 generator function 会返回一个 generator object，并且*不会*执行该函数的函数体。

例如，让我们考虑以下 generator function：

```
def countdown(n):
    print("Beginning countdown!")
    while n >= 0:
        yield n
        n -= 1
    print("Blastoff!")
```

调用 `countdown(k)` 会返回一个从 `k` 倒数到 0 的 generator object。由于 generators 是 iterators，我们可以对得到的 object 调用 `iter`，这只会返回同一个 object。注意此时函数体并未执行；不会打印任何内容，也不会输出任何数字。

```
>>> c = countdown(5)
>>> c
<generator object countdown ...>
>>> c is iter(c)
True
```

那么倒数是怎样进行的呢？同样，由于 generators 是 iterators，我们对它们调用 `next` 来获取下一个 element！第一次调用 `next` 时，执行从函数体的第一行开始，一直持续到遇到 `yield` 语句为止。`yield` 语句中表达式的求值结果会作为返回值。下面的交互式会话接续上面的会话。

```
>>> next(c)
Beginning countdown!
5
```

与本课程之前见过的 functions 不同，generator functions 可以记住它们的状态。在任何连续调用 `next` 时，执行都会从之前执行过的 `yield` 语句的下一行继续。与第一次调用 `next` 一样，执行会一直持续到遇到下一个 `yield` 语句为止。注意，正因为如此，`Beginning countdown!` 不会再次被打印。

```
>>> next(c)
4
>>> next(c)
3
```

接下来的 3 次 `next` 调用将继续 yield 连续递减的整数，直到 0。在随后的一次调用中，会抛出 `StopIteration` 错误，因为已经没有更多的 values 可以 yield 了（即，在遇到 `yield` 语句之前就已经到达函数体末尾）。

```
>>> next(c)
2
>>> next(c)
1
>>> next(c)
0
>>> next(c)
Blastoff!
StopIteration
```

分别调用 `countdown` 会创建带有各自状态的不同 generator objects。通常，generators 不应该重新开始。如果你想重置这个 sequence，只需再次调用该 generator function 来创建另一个 generator object。

```
>>> c1, c2 = countdown(5), countdown(5)
>>> c1 is c2
False
>>> next(c1)
5
>>> next(c2)
5
```

以下是上述内容的总结：

* 一个 *generator function* 包含 `yield` 语句，并返回一个 *generator object*。
* 对一个 generator object 调用 `iter` function 会返回同一个 object，且不会修改它的当前状态。
* 直到对生成的 generator object 调用 `next` 之前，generator function 的函数体都不会被求值。对一个 generator object 调用 `next` function 会计算并返回其 sequence 中的下一个 object。如果 sequence 已耗尽，则会抛出 `StopIteration`。
* 一个 generator 会为下一次 `next` 调用"记住"它的状态。因此，

  + 第一次 `next` 调用是这样工作的：

    1. 进入该 function，运行到带有 `yield` 的那一行。
    2. 返回 `yield` 语句中的 value，但记住该 function 的状态，供将来的 `next` 调用使用。
  + 而后续的 `next` 调用是这样工作的：

    1. 重新进入该 function，从**之前执行过的 `yield` 语句的下一行**开始，运行到下一个 `yield` 语句。
    2. 返回 `yield` 语句中的 value，但记住该 function 的状态，供将来的 `next` 调用使用。
* 调用一个 generator function 会返回一个全新的 generator object（就像对一个 iterable object 调用 `iter` 一样）。
* 除非定义如此，generator 不应重新开始。要从一个 generator 的第一个 element 重新开始，只需再次调用该 generator function 来创建一个新的 generator。

generators 的另一个有用工具是 `yield from` 语句。`yield from` 会 yield 来自一个 iterator 或 iterable 的所有 values。

```
>>> def gen_list(lst):
...     yield from lst
...
>>> g = gen_list([1, 2, 3, 4])
>>> next(g)
1
>>> next(g)
2
>>> next(g)
3
>>> next(g)
4
>>> next(g)
StopIteration
```

### Q1: Infinite Hailstone

编写一个 generator function，它 yield 从数字 `n` 开始的 hailstone sequence 的 elements。在到达 hailstone sequence 末尾之后，该 generator 应无限地 yield 数字 1。

以下是 hailstone sequence 如何定义的简要提醒：

1. 选取一个正整数 `n` 作为起点。
2. 如果 `n` 是偶数，将它除以 2。
3. 如果 `n` 是奇数，将它乘以 3 再加 1。
4. 继续这个过程，直到 `n` 为 1。

尝试用递归的方式编写这个 generator function。如果你卡住了，可以先尝试用迭代的方式写，然后再看看如何把这个实现改写成递归的。

> **提示：** 由于 `hailstone` 返回一个 generator，你可以 `yield from` 一个对 `hailstone` 的调用！

```
def hailstone(n):
    """
    Yields the elements of the hailstone sequence starting at n.
    At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q hailstone

Copy

✂️
```

  

### Q2: Merge

**定义：** 一个 *infinite iterator* 是一个在调用 `next` 时永不停止提供 values 的 iterator。例如，`ones()` 求值为一个 infinite iterator：

```
def ones():
    while True:
        yield 1
```

编写一个 generator function `merge(a, b)`，它接收两个 infinite iterators `a` 和 `b` 作为输入。两个 iterator 都按严格递增的顺序 yield elements，且不含重复项。你的 generator 应按递增顺序产生来自两个输入 iterators 的所有不重复 elements，且不含任何重复项。

> **注意：** 输入 iterators 自身内部不包含重复项，但它们之间可能有共同的 elements。

```
def merge(a, b):
    """
    Return a generator that has all of the elements of infinite iterators a and b,
    in increasing order, without duplicates.

    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    a_val, b_val = next(a), next(b)
    while True:
        if a_val == b_val:
            "*** YOUR CODE HERE ***"
        elif a_val < b_val:
            "*** YOUR CODE HERE ***"
        else:
            "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q merge

Copy

✂️
```

  

### Q3: Stair Ways

假设你想爬上有一段 `n` 级台阶的楼梯，其中 `n` 是一个正整数。你每次可以迈**一级**或**两级台阶**。

编写一个 generator function `stair_ways`，它 yield 你爬上这段楼梯的所有不同方式。

每一种爬楼梯的 "way" 都可以用一个由 1 和 2 组成的 list 表示，其中每个数字表示你一次迈一级还是两级台阶。

例如，对于一段有 3 级台阶的楼梯，有三种爬法：

* 你可以每次迈一级台阶：`[1, 1, 1]`。
* 你可以先迈两级台阶再迈一级台阶：`[2, 1]`。
* 你可以先迈一级台阶再迈两级台阶：`[1, 2].`。

因此，`stair_ways(3)` 应 yield `[1, 1, 1]`、`[2, 1]` 和 `[1, 2]`。它们可以按任意顺序 yield。

> **提示：** 递归地思考这个问题。如果你正站在某一级台阶 n 上，你刚刚可能站在哪几级台阶上？

```
def stair_ways(n):
    """
    Yield all the ways to climb a set of n stairs taking
    1 or 2 steps at a time.

    >>> list(stair_ways(0))
    [[]]
    >>> s_w = stair_ways(4)
    >>> sorted([next(s_w) for _ in range(5)])
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
    >>> list(s_w) # Ensure you're not yielding extra
    []
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q stair_ways

Copy

✂️
```

  

### Q4: Yield Paths

编写一个 generator function `yield_paths`，它接收一棵 tree `t` 和一个目标 `target`。它 yield 从 `t` 的 root 到任何 label 为 `target` 的 node 的每一条 path。

每条 path 应以一个 list 的形式返回，其中包含从 root 到匹配 node 的 labels。这些 paths 可以按任意顺序 yield。

> **提示：** 如果你不知道如何入手，想一想如果这不是一个 generator function，你会如何解决这个问题。递归的步骤会是什么样子？

> **提示：** 记住，你可以遍历 generator objects，因为它们是一种 iterator！

```
def yield_paths(t, target):
    """
    Yields all possible paths from the root of t to a node with the label
    target as a list.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(yield_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = yield_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = tree(0, [tree(2, [t1])])
    >>> print_tree(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = yield_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    if label(t) == target:
        yield ____
    for b in branches(t):
        for ____ in ____:
            yield ____
```

使用 Ok 来测试你的代码：

```
python3 ok -q yield_paths

Copy

✂️
```

  

Check Your Score Locally
------------------------

你可以通过运行以下命令，在本地检查你在这份作业每道题上的得分：

```
python3 ok --score
```

**这并不会提交作业！** 当你对自己的得分满意后，请把作业提交到 Gradescope 以获得相应的学分。

Submit Assignment
=================

把这份作业提交上去，方法是把你编辑过的所有文件上传到**对应的 Gradescope 作业**。[Lab 00](../../lab/lab00.html "../../lab/lab00.html") 中有详细说明。

Exam Practice
=============

Homework 作业中也会包含一些往年的考题供你尝试。这些题目没有提交要求；如果你想练练手，欢迎随意尝试！

1. Summer 2016 Final Q8: [Zhen-erators Produce Power](https://inst.eecs.berkeley.edu//~cs61a/su16/assets/pdfs/61a-su16-final.pdf#page=13 "https://inst.eecs.berkeley.edu//~cs61a/su16/assets/pdfs/61a-su16-final.pdf#page=13")
2. Spring 2018 Final Q4(a): [Apply Yourself](https://inst.eecs.berkeley.edu/~cs61a/sp18/assets/pdfs/61a-sp18-final.pdf#page=5 "https://inst.eecs.berkeley.edu/~cs61a/sp18/assets/pdfs/61a-sp18-final.pdf#page=5")

* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Generators](index.html#generators "index.html#generators")

- [Q1: Infinite Hailstone](index.html#q1-infinite-hailstone "index.html#q1-infinite-hailstone")
- [Q2: Merge](index.html#q2-merge "index.html#q2-merge")
- [Q3: Stair Ways](index.html#q3-stair-ways "index.html#q3-stair-ways")
- [Q4: Yield Paths](index.html#q4-yield-paths "index.html#q4-yield-paths")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Exam Practice](index.html#exam-practice "index.html#exam-practice")
