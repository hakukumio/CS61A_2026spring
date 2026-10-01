Lab 1: Functions | CS 61A Spring 2026



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



Lab 1: Functions

* [lab01.zip](lab01.zip "lab01.zip")
======================================================

*截止时间为 1 月 28 日（周三）晚上 11:59。*

Starter Files
-------------

下载 [lab01.zip](lab01.zip "lab01.zip")。

> **Lab 1 attendance：** 我们不为 Lab 1 记录 attendance。每个人都会自动获得 attendance 分。

Required Questions
==================

Review
------

> **重要：** 如果 `python3` 命令无法运行，请尝试使用 `python` 或 `py`。

Using Python (enable JavaScript)

以下是在文件上运行 Python 的最常见方式。

1. 不使用任何命令行选项会运行你所提供文件中的代码，然后返回到命令行。如果你的文件只包含 function 定义，除非存在语法错误，否则你不会看到任何输出。

   ```
   python3 lab00.py
   ```
2. **`-i`**：`-i` 选项会运行你所提供文件中的代码，然后打开一个交互式会话（带有 `>>>` 提示符）。然后你可以求值表达式，例如调用你定义的 functions。要退出，请输入 `exit()`。你也可以使用键盘快捷键：在 Linux/Mac 机器上按 `Ctrl-D`，在 Windows 上按 `Ctrl-Z Enter`。

   如果你在交互式运行 Python 文件时编辑了它，你需要退出并重新启动解释器，这些更改才会生效。

   下面是我们如何交互式地运行 `lab00.py`：

   ```
   python3 -i lab00.py
   ```
3. **`-m doctest`**：运行文件中的 doctests，也就是 functions docstrings 里的示例。

   文件中的每个测试都由 `>>>` 后跟一些 Python 代码和期望输出组成。

   下面是我们如何运行 `lab00.py` 中的 doctests：

   ```
    python3 -m doctest lab00.py
   ```

   当我们的代码通过所有 doctests 时，不会显示任何输出。否则，会显示关于失败测试的信息。

  
Using OK (enable JavaScript)

在 CS 61A 中，我们使用一个名为 Ok 的程序来自动评分 labs、homeworks 和 projects。

要使用 Ok 测试一个 function，请运行以下命令（把 `FUNCTION` 替换为该 function 的名字）：

```
python3 ok -q FUNCTION
```

如果你的 function 包含以 `"DEBUG:"` 开头的 `print` 调用，那么这一行会被 OK 忽略。（否则，包含额外的 `print` 调用可能会因为显示了额外输出而导致测试失败。）

```
print("DEBUG:", x)
```

更多功能在 [Using OK page](../../articles/using-ok.html "../../articles/using-ok.html") 中有介绍。
**你可以在 [ok-help](https://go.cs61a.org/ok-help "https://go.cs61a.org/ok-help") 快速生成大多数 ok 命令。**

  

Division, Floor Div, and Modulo (enable JavaScript)

以下是 Python 3 中与除法相关的运算符示例：
  
  
| True Division: `/`（小数除法） | Floor Division: `//`（整数除法） | Modulo: `%`（余数） |
| --- | --- | --- |
| ``` >>> 1 / 5 0.2  >>> 25 / 4 6.25  >>> 4 / 2 2.0  >>> 5 / 0 ZeroDivisionError ``` | ``` >>> 1 // 5 # truncate result of true division 0  >>> 25 // 4 6  >>> 4 // 2 2  >>> 5 // 0 ZeroDivisionError ``` | ``` >>> 1 % 5 1  >>> 25 % 4 1  >>> 4 % 2 0  >>> 5 % 0 ZeroDivisionError ``` |

当除以 0 时会出现 `ZeroDivisionError`。

`%` 运算符的一个有用技巧是检查一个数 `x` 能否被另一个数 `y` 整除：

```
x % y == 0
```

例如，为了检查 `x` 是否为偶数：`x % 2 == 0`

  

Return and Print (enable JavaScript)

你定义的大多数 functions 都会包含一个 `return` statement，它为用于调用该 function 的 call expression 提供值。

当 Python 执行 `return` statement 时，function call 会立即终止。如果 Python 在未执行 `return` statement 的情况下到达 function body 的末尾，那么该 function 返回 `None`。

相比之下，`print` function 用于显示值。与 `return` statement 不同，当 Python 求值对 `print` 的调用时，该 function *不会*立即终止。

```
def what_prints():
    print('Hello World!')
    return 'Exiting this function.'
    print('This course is awesome!')

>>> what_prints()
Hello World!
'Exiting this function.'
```

> 另请注意，`print` 会显示**不带引号**的文本，而 `return` 会保留引号。

What Would Python Display? (WWPD)
---------------------------------

### Q1: Return and Print

> 使用 Ok 来通过以下 "What Would Python Display?" 题目检验你的理解：
>
> ```
> python3 ok -q return-and-print -u
>
> Copy
>
> ✂️
> ```

```
>>> def welcome():
...     print('Go')
...     return 'hello'
...
>>> def cal():
...     print('Bears')
...     return 'world'
...
>>> welcome()

______



Go
'hello'

>>> print(welcome(), cal())

______



Go
Bears
hello world
```

Toggle Solution (enable JavaScript)

Write Code
----------

### Q2: Debugging Quiz

以下是关于不同 debugging 技巧的快速测验，这些技巧对你在本课程中会很有帮助。你可以参考 [debugging article](../../articles/debugging/index.html "../../articles/debugging/index.html") 来回答这些问题。

使用 Ok 来检验你的理解：

```
python3 ok -q debugging-quiz -u

Copy

✂️
```

  

### Q3: Pick a Digit

实现 `digit`，它接收正整数 `n` 和 `k`，并且函数体只有一条 return statement。它返回 `n` 中从最右边数字（个位）向左第 `k` 位的数字。如果 `k` 为 0，则返回最右边的数字。如果 `n` 中不存在从最右边数字向左第 `k` 位的数字，则返回 0。

**提示：** 使用 `//` 和 `%` 以及内置的 `pow` function 来分离出 `n` 的某一位数字。

```
def digit(n, k):
    """Return the k-th digit from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    return ____
```

使用 Ok 来测试你的代码：

```
python3 ok -q digit

Copy

✂️
```

  

### Q4: Middle Number

通过编写单个 return expression 来实现 `middle`，该 expression 求值为三个不同的整数 `a`、`b` 和 `c` 中既不是最大也不是最小的那个值。

> **提示：** 试着先把所有数字组合起来，再用内置的 `min` 和 `max` functions 去掉你不想返回的那些。
>
> ```
> >>> max(1, 2, 3)
> 3
> >>> min(-1, -2, -3)
> -3
> ```

```
def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    return ____
```

使用 Ok 来测试你的代码：

```
python3 ok -q middle

Copy

✂️
```

  

Syllabus Quiz
-------------

### Q5: Syllabus Quiz

请填写 [Syllabus Quiz](https://go.cs61a.org/syllabus-quiz "https://go.cs61a.org/syllabus-quiz")，它用于确认你理解了 syllabus 页面上的各项政策。

Check Your Score Locally
------------------------

你可以通过运行以下命令，在本地检查你在这份作业每道题上的得分

```
python3 ok --score
```

**这并不会提交作业！** 当你对自己的得分满意后，请把作业提交到 Gradescope 以获得相应的学分。

Submit Assignment
=================

把这份作业提交上去，方法是把你编辑过的所有文件上传到**对应的 Gradescope 作业**。[Lab 00](../lab00.html#submitting-the-assignment "../lab00.html#submitting-the-assignment") 中有详细说明。

正确完成所有题目值 1 分。如果你参加的是常规 lab，你还需要 TA 记录的 attendance 才能拿到这 1 分。请在离开前确认你的 TA 已经记录了你的 attendance。

> **Lab 1 attendance：** 我们不为 Lab 1 记录 attendance。每个人都会自动获得 attendance 分。

Optional Questions
==================

> 这些题目是可选的。如果你没有完成它们，你仍然可以获得这份作业的学分。它们是很好的练习，所以还是做一下吧！

**你今天真的应该做这些题！** 它们被标记为可选，只是因为有些学生刚加入这门课程、正在追赶进度，但已经上过前三讲的学生应该完全有能力解出这些题，而且有了这些解题经验，Homework 1 会顺利得多。

### Q6: WWPD: What If?

> 使用 Ok 来通过以下 "What Would Python Display?" 题目检验你的理解：
>
> ```
> python3 ok -q if-statements -u
>
> Copy
>
> ✂️
> ```
>
>   
>
> **提示**：`print`（与 `return` 不同）*不会*导致 function 退出。

```
>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)

______



10
foo
```

Toggle Solution (enable JavaScript)

```
>>> def bake(cake, make):
...     if cake == 0:
...         cake = cake + 1
...         print(cake)
...     if cake == 1:
...         print(make)
...     else:
...         return cake
...     return make
>>> bake(0, 29)

______



1
29
29

>>> bake(1, "mashed potatoes")

______



mashed potatoes
'mashed potatoes'
```

Toggle Solution (enable JavaScript)

### Q7: Falling Factorial

我们来写一个 function `falling`，它是一个 "falling" factorial，接收两个参数 `n` 和 `k`，返回从 `n` 开始向下连续 `k` 个数的乘积。当 `k` 为 0 时，该 function 应返回 1。

```
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q falling

Copy

✂️
```

  

### Q8: Divisible By k

写一个 function `divisible_by_k`，它接收正整数 `n` 和 `k`。它按从小到大的顺序打印所有小于等于 `n` 且能被 `k` 整除的正整数。然后，它返回打印了多少个数。

```
def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 that are divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q divisible_by_k

Copy

✂️
```

  

### Q9: Sum Digits

写一个 function，它接收一个非负整数并对其各位数字求和。（在这里使用整除和取模可能会有所帮助！）

```
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q sum_digits

Copy

✂️
```

  

### Q10: Double Eights

写一个 function，它接收一个数字，并判断其各位数字中是否包含两个相邻的 8。

```
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q double_eights

Copy

✂️
```

* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Review](index.html#review "index.html#review")
+ [What Would Python Display? (WWPD)](index.html#what-would-python-display-wwpd "index.html#what-would-python-display-wwpd")

- [Q1: Return and Print](index.html#q1-return-and-print "index.html#q1-return-and-print")

+ [Write Code](index.html#write-code "index.html#write-code")

- [Q2: Debugging Quiz](index.html#q2-debugging-quiz "index.html#q2-debugging-quiz")
- [Q3: Pick a Digit](index.html#q3-pick-a-digit "index.html#q3-pick-a-digit")
- [Q4: Middle Number](index.html#q4-middle-number "index.html#q4-middle-number")

+ [Syllabus Quiz](index.html#syllabus-quiz "index.html#syllabus-quiz")

- [Q5: Syllabus Quiz](index.html#q5-syllabus-quiz "index.html#q5-syllabus-quiz")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Optional Questions](index.html#optional-questions "index.html#optional-questions")

+ [Q6: WWPD: What If?](index.html#q6-wwpd-what-if "index.html#q6-wwpd-what-if")
+ [Q7: Falling Factorial](index.html#q7-falling-factorial "index.html#q7-falling-factorial")
+ [Q8: Divisible By k](index.html#q8-divisible-by-k "index.html#q8-divisible-by-k")
+ [Q9: Sum Digits](index.html#q9-sum-digits "index.html#q9-sum-digits")
+ [Q10: Double Eights](index.html#q10-double-eights "index.html#q10-double-eights")
