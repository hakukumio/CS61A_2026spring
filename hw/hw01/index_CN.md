Homework 1 | CS 61A Spring 2026



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



Homework 1: Functions, Control

* [hw01.zip](hw01.zip "hw01.zip")
=================================================================

*截止时间为 1 月 29 日（周四）晚上 11:59。*

Instructions
------------

下载 [hw01.zip](hw01.zip "hw01.zip")。

**提交：** 完成后，请把作业提交到 Gradescope。在截止时间之前，你可以提交多次；只有最后一次提交会被评分。请确认你已经在 Gradescope 上成功提交了你的代码。关于提交作业的更多说明，请参见 [Lab 0](../../lab/lab00.html "../../lab/lab00.html")。

**使用 Ok：** 如果你对使用 Ok 有任何疑问，请参阅[这份指南。](../../articles/using-ok.html "../../articles/using-ok.html")

**阅读材料：** 你可能会觉得以下参考资料很有用：

* [Section 1.1](https://www.composingprograms.com/pages/11-getting-started.html "https://www.composingprograms.com/pages/11-getting-started.html")
* [Section 1.2](https://www.composingprograms.com/pages/12-elements-of-programming.html "https://www.composingprograms.com/pages/12-elements-of-programming.html")
* [Section 1.3](https://www.composingprograms.com/pages/13-defining-new-functions.html "https://www.composingprograms.com/pages/13-defining-new-functions.html")
* [Section 1.4](https://www.composingprograms.com/pages/14-designing-functions.html "https://www.composingprograms.com/pages/14-designing-functions.html")
* [Section 1.5](https://www.composingprograms.com/pages/15-control.html "https://www.composingprograms.com/pages/15-control.html")

**评分：** 作业根据正确性评分。每答错一道题，总分就会减少一分。**本次作业满分为 2 分。**

Required Questions
==================

### Q1: A Plus Abs B

Python 的 `operator` 模块包含双参数 functions，例如用于 Python 内置算术运算符的 `add` 和 `sub`。例如，`add(2, 3)` 求值为 5，就像表达式 `2 + 3` 一样。

填写下面 function 中的空，把 `a` 加到 `b` 的绝对值上，且不调用 `abs` function。除了这两个空以外，你**不得**修改任何提供的代码。

```
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = _____
    else:
        f = _____
    return f(a, b)
```

使用 Ok 来测试你的代码：

```
python3 ok -q a_plus_abs_b

Copy

✂️
```

  

使用 Ok 来运行本地语法检查器（它会检查你没有修改提供的代码中除这两个空以外的任何部分）：

```
python3 ok -q a_plus_abs_b_syntax_check
```

### Q2: Two of Three

写一个 function，接收三个*正数*作为参数，并返回其中最小的两个数的平方和。**function 的主体只能使用一行。**

```
def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return _____
```

> **提示：** 考虑使用 `max` 或 `min` function：
>
> ```
> >>> max(1, 2, 3)
> 3
> >>> min(-1, -2, -3)
> -3
> ```

使用 Ok 来测试你的代码：

```
python3 ok -q two_of_three

Copy

✂️
```

  

使用 Ok 来运行本地语法检查器（它会检查你在 function 的主体中只使用了一行）：

```
python3 ok -q two_of_three_syntax_check
```

### Q3: Largest Factor

写一个 function，接收一个**大于 1** 的整数 `n`，并返回小于 `n` 且能整除 `n` 的最大整数。

```
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factors are 1, 13
    1
    """
    "*** YOUR CODE HERE ***"
```

> **提示：** 要检查 `b` 是否能整除 `a`，
> 请使用表达式 `a % b == 0`，它可以读作
> “`a` 除以 `b` 的余数是 0”。

使用 Ok 来测试你的代码：

```
python3 ok -q largest_factor

Copy

✂️
```

  

### Q4: Hailstone

Douglas Hofstadter 荣获普利策奖的著作 *Gödel, Escher, Bach* 提出了以下数学谜题。

1. 选取一个正整数 `n` 作为起点。
2. 如果 `n` 是偶数，就把它除以 2。
3. 如果 `n` 是奇数，就把它乘以 3 再加 1。
4. 不断重复这个过程，直到 `n` 为 1。

数字 `n` 会上下起伏，但最终会落到 1（至少对所有曾经被尝试过的数字都是如此——还从未有人证明这个序列会终止）。类似地，hailstone 在大气中上下起伏，最终落到地面。

这串 `n` 的取值序列通常被称为 Hailstone 序列。写一个 function，它接收一个形参名为 `n` 的单个参数，打印出从 `n` 开始的 hailstone 序列，并返回序列中的步数：

```
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
```

Hailstone 序列可能会变得相当长！试试 27。你能找到的最长序列是多长？

> 注意，如果一开始 `n == 1`，那么序列只有一步长。   
> **提示：** 如果你看到的是 4.0 但只想要 4，试试用整除 `//` 代替普通除法 `/`。

使用 Ok 来测试你的代码：

```
python3 ok -q hailstone

Copy

✂️
```

  

**对 hailstone 序列感到好奇？看看这篇文章：**

* 2019 年，人们对 hailstone 猜想为何对大多数数字成立的理解取得了一项重大[进展](https://www.quantamagazine.org/mathematician-terence-tao-and-the-collatz-conjecture-20191211/ "https://www.quantamagazine.org/mathematician-terence-tao-and-the-collatz-conjecture-20191211/")！

Check Your Score Locally
------------------------

你可以通过运行以下命令，在本地检查你在这份作业每道题上的得分

```
python3 ok --score
```

**这并不会提交作业！** 当你对自己的得分满意后，请把作业提交到 Gradescope 以获得相应的学分。

Submit Assignment
=================

把这份作业提交上去，方法是把你编辑过的所有文件上传到**对应的 Gradescope 作业**。[Lab 00](../../lab/lab00.html "../../lab/lab00.html") 中有详细说明。

* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Q1: A Plus Abs B](index.html#q1-a-plus-abs-b "index.html#q1-a-plus-abs-b")
+ [Q2: Two of Three](index.html#q2-two-of-three "index.html#q2-two-of-three")
+ [Q3: Largest Factor](index.html#q3-largest-factor "index.html#q3-largest-factor")
+ [Q4: Hailstone](index.html#q4-hailstone "index.html#q4-hailstone")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
