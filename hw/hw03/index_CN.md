Homework 3 | CS 61A Spring 2026



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



Homework 3: Recursion, Tree Recursion

* [hw03.zip](hw03.zip "hw03.zip")
========================================================================

*截止时间为 2 月 19 日（周四）晚上 11:59。*

Instructions
------------

下载 [hw03.zip](hw03.zip "hw03.zip")。在压缩包中，你会找到一个名为 [hw03.py](hw03.py "hw03.py") 的文件，以及一份 `ok` 自动评分器的副本。

**提交：** 完成后，请把作业提交到 Gradescope。在截止时间之前，你可以提交多次；只有最后一次提交会被评分。请确认你已经在 Gradescope 上成功提交了你的代码。关于提交作业的更多说明，请参见 [Lab 0](../../lab/lab00.html "../../lab/lab00.html")。

**使用 Ok：** 如果你对使用 Ok 有任何疑问，请参阅[这份指南。](../../articles/using-ok.html "../../articles/using-ok.html")

**阅读材料：** 你可能会觉得以下参考资料很有用：

* [Section 1.7](https://www.composingprograms.com/pages/17-recursive-functions.html "https://www.composingprograms.com/pages/17-recursive-functions.html")

**评分：** 作业根据正确性评分。每答错一道题，总分就会减少一分。**本次作业满分为 2 分。**

Required Questions
==================

Recursion
---------

### Q1: Num Eights

写一个 recursive function `num_eights`，它接收一个正整数 `num`，并返回数字 8 在 `num` 中出现的次数。

> **重要：**
> 请使用递归；如果你使用任何 assignment statements 或循环，测试将会失败。
> （你可以定义新的 functions，但也不要在其中放 assignment statements。）

```
def num_eights(num):
    """Returns the number of times 8 appears as a digit of num.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q num_eights

Copy

✂️
```

  

### Q2: Digit Distance

对于一个给定的整数，*digit distance* 是相邻数字之间绝对差的总和。例如：

* `61` 的 digit distance 是 `5`，因为 `6 - 1` 的绝对值是 `5`。
* `71253` 的 digit distance 是 `12`（`abs(7-1) + abs(1-2) + abs(2-5) + abs(5-3)` = `6 + 1 + 3 + 2`）。
* `6` 的 digit distance 是 `0`，因为没有相邻的数字对。

写一个 function，求出某个正整数的 digit distance。你必须使用递归，否则测试会失败。

```
def digit_distance(num):
    """Determines the digit distance of num.

    >>> digit_distance(3)
    0
    >>> digit_distance(777) # 0 + 0
    0
    >>> digit_distance(314) # 2 + 3
    5
    >>> digit_distance(31415926535) # 2 + 3 + 3 + 4 + ... + 2
    32
    >>> digit_distance(3464660003)  # 1 + 2 + 2 + 2 + ... + 3
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q digit_distance

Copy

✂️
```

  

### Q3: Interleaved Sum

写一个 function `interleaved_sum`，它接收一个数字 `num` 和两个单参数 functions：`f_odd` 和 `f_even`。它返回对从 1 到 `num`（*包含* `num`）的每个奇数应用 `f_odd`、对每个偶数应用 `f_even` 所得结果的总和。

例如，执行 `interleaved_sum(5, lambda x: x, lambda x: x * x)` 返回 `1 + 2*2 + 3 + 4*4 + 5 = 29`。

> **重要：** 实现这个 function 时不要使用任何循环，也不要直接判断一个数字是奇数还是偶数（不要使用 `%`）。与其直接检查一个数字是偶数还是奇数，不如从 1 开始，因为你知道 1 是奇数。
>
> **提示：** 引入一个内部 helper function，它接收一个奇数 `k`，并计算从 `k` 到 `num`（包含 `num`）的 interleaved sum。或者，你也可以使用 mutual recursion。

```
def interleaved_sum(num, f_odd, f_even):
    """Compute the sum f_odd(1) + f_even(2) + f_odd(3) + ..., up
    to num.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    >>> check(SOURCE_FILE, 'interleaved_sum', ['BitAnd', 'BitOr', 'BitXor']) # ban bitwise operators, don't worry about these if you don't know what they are
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q interleaved_sum

Copy

✂️
```

  

Tree Recursion
--------------

### Q4: Count Dollars

给定一个正整数 `sum_needed`，如果一组美元纸币的面值总和为 `sum_needed`，那么这组纸币就能为 `sum_needed` 找零。这里我们使用标准的美元纸币面额：1、5、10、20、50 和 100。例如，以下纸币组合可以为 `15` 找零：

* 15 张 1 美元纸币
* 10 张 1 美元、1 张 5 美元纸币
* 5 张 1 美元、2 张 5 美元纸币
* 5 张 1 美元、1 张 10 美元纸币
* 3 张 5 美元纸币
* 1 张 5 美元、1 张 10 美元纸币

因此，为 `15` 找零共有 6 种方式。写一个**递归** function `count_dollars`，它接收一个正整数 `sum_needed`，并返回使用 1、5、10、20、50 和 100 美元纸币为 `sum_needed` 找零的方式数。

在你的解法中使用 `next_smaller_dollar`：`next_smaller_dollar` 会返回输入值之后的下一个更小美元纸币面额（例如 `next_smaller_dollar(5)` 是 `1`）。*如果下一个美元纸币面额不存在，该 function 将返回 `None`。*

> **重要：** 请使用递归；如果你使用循环，测试将会失败。
>
> **提示：**
> 参考 `count_partitions` 的[实现](https://www.composingprograms.com/pages/17-recursive-functions.html#example-partitions "https://www.composingprograms.com/pages/17-recursive-functions.html#example-partitions")，了解如何用更小的部分累加到某个最终值来计数。
> 如果你需要在递归调用之间跟踪多个值，
> 可以考虑写一个 helper function。

```
def next_smaller_dollar(bill):
    """Returns the next smaller bill in order."""
    if bill == 100:
        return 50
    if bill == 50:
        return 20
    if bill == 20:
        return 10
    elif bill == 10:
        return 5
    elif bill == 5:
        return 1

def count_dollars(sum_needed):
    """Return the number of ways to make change.

    >>> count_dollars(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_dollars', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q count_dollars

Copy

✂️
```

  

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

Optional Questions
==================

> 这些题目是可选的。如果你没有完成它们，你仍然会获得这份作业的学分。它们是很好的练习，所以无论如何都做做看吧！

### Q5: Count Dollars Upward

写一个**递归** function `count_dollars_upward`，它与 `count_dollars` 类似，只是使用 `next_larger_dollar`，它返回输入值之后的下一个更大美元纸币面额（例如 `next_larger_dollar(5)` 是 `10`）。*如果下一个美元纸币面额不存在，该 function 将返回 `None`。*

> **重要：** 请使用递归；如果你使用循环，测试将会失败。

```
def next_larger_dollar(bill):
    """Returns the next larger bill in order."""
    if bill == 1:
        return 5
    elif bill == 5:
        return 10
    elif bill == 10:
        return 20
    elif bill == 20:
        return 50
    elif bill == 50:
        return 100

def count_dollars_upward(sum_needed):
    """Return the number of ways to make change using bills.

    >>> count_dollars_upward(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars_upward(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars_upward(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars_upward(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars_upward(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars_upward(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_dollars_upward', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q count_dollars_upward

Copy

✂️
```

  

Exam Practice
=============

作业中还会包含一些往年的考试级题目供你参考。这些题目没有需要提交的部分；如果你想挑战一下，欢迎尝试！

1. Fall 2017 MT1 Q4a: [Digital](https://inst.eecs.berkeley.edu/~cs61a/fa21/exam/fa17/mt1/61a-fa17-mt1.pdf#page=5 "https://inst.eecs.berkeley.edu/~cs61a/fa21/exam/fa17/mt1/61a-fa17-mt1.pdf#page=5")
2. Fall 2019 Final Q6b: [Palindromes](https://inst.eecs.berkeley.edu/~cs61a/sp21/exam/fa19/final/61a-fa19-final.pdf#page=6 "https://inst.eecs.berkeley.edu/~cs61a/sp21/exam/fa19/final/61a-fa19-final.pdf#page=6")

Just For Fun Questions
======================

下面的题目超出了 61A 的范围。如果你想挑战一下，可以尝试它们，但它们只是一些谜题，并非课程要求。几乎所有学生都会跳过它们，这没什么关系。我们**不会**在 Ed 上或 Office Hours 期间优先为这些问题提供支持。

### Q6: Knapsack

你是一个小偷，你的任务是在 `n` 件重量和价值各不相同的物品中进行挑选。你有一个最多能装 `c` 磅的背包，你想挑选物品中的某个子集，使你偷到的价值最大化。

定义 `knapsack`，它接收一个 list `weights`、一个 list `values` 和一个容量 `c`，并返回那个最大值。你可以假设第 0 件物品重 `weights[0]` 磅，价值为 `values[0]`；第 1 件物品重 `weights[1]` 磅，价值为 `values[1]`；依此类推。

```
def knapsack(weights, values, c):
    """
    >>> w = [2, 6, 3, 3]
    >>> v = [1, 5, 3, 3]
    >>> knapsack(w, v, 6)
    6
    """
    "*** YOUR CODE HERE ***"
```

### Q7: Towers of Hanoi

一个名为 Towers of Hanoi 的经典谜题是一种游戏，它由三根杆和若干大小不同、可以套到任意一根杆上的圆盘组成。游戏开始时，`num` 个圆盘按大小递增的顺序整齐地叠放在 `start` 杆上，最小的在最上面，形成一个锥形。
![Towers of Hanoi](https://upload.wikimedia.org/wikipedia/commons/0/07/Tower_of_Hanoi.jpeg)
这个谜题的目标是把整叠圆盘全部移到 `end` 杆上，同时遵守以下规则：

* 一次只能移动一个圆盘。
* 每次移动包括从某一根杆上取下最上面（最小）的圆盘，并把它套到另一根杆上，放在该杆上可能已有的其他圆盘之上。
* 任何圆盘都不能放在比它小的圆盘之上。

补全 `move_stack` 的定义，它打印出在不违反规则的前提下把 `num` 个圆盘从 `start` 杆移到 `end` 杆所需的步骤。提供的 `print_move` function 会打印出把单个圆盘从给定的 `origin` 移动到给定的 `destination` 的步骤。
> **提示：**
> 在纸上画几局不同 `num` 的游戏推演，试着找出适用于任意 `num` 的圆盘移动规律。在你的解法中，每当需要把少于 `num` 个圆盘从一根杆移到另一根杆时，就采用递归的信仰之跃。如果你需要更多帮助，请看下面的提示。

Hint 1 (enable JavaScript)

看看下面这个 Towers of Hanoi 的动画，它来自 [Wikimedia](https://commons.wikimedia.org/wiki/File:Iterative_algorithm_solving_a_6_disks_Tower_of_Hanoi.gif "https://commons.wikimedia.org/wiki/File:Iterative_algorithm_solving_a_6_disks_Tower_of_Hanoi.gif")，作者是用户 [Trixx](https://commons.wikimedia.org/wiki/User:Trixx "https://commons.wikimedia.org/wiki/User:Trixx")。

![](https://upload.wikimedia.org/wikipedia/commons/8/8d/Iterative_algorithm_solving_a_6_disks_Tower_of_Hanoi.gif)

  

Hint 2 (enable JavaScript)

Towers of Hanoi 中使用的策略是：把除最下面圆盘以外的所有圆盘移到第二根杆上，然后把最下面的圆盘移到第三根杆上，再把除第二个圆盘以外的所有圆盘从第二根杆移到第三根杆上。

  

Hint 3 (enable JavaScript)

有一件事你不用担心，那就是收集所有步骤。只要你确保移动是按顺序打印的，`print` 实际上会在终端中“收集”所有结果。

```
def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(num, start, end):
    """Print the moves required to move num disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    num -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least num disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top num start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q move_stack

Copy

✂️
```

  

### Q8: Anonymous Factorial

> 这道题说明，即使不在 global frame 中给 recursive functions 起名字，也可以写出它们。

通过使用[条件表达式](http://docs.python.org/py3k/reference/expressions.html#conditional-expressions "http://docs.python.org/py3k/reference/expressions.html#conditional-expressions")，recursive factorial function 可以写成单个表达式。

```
>>> fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))
>>> fact(5)
120
```

然而，这个实现依赖于 `fact` 有一个名字这一事实（这里没有双关的意思），我们在 `fact` 的函数体里引用了这个名字。为了写一个 recursive function，我们一直使用 `def` 或 assignment statement 给它起名字，这样就能在它自己的函数体里引用它。在这道题中，你的任务是递归地定义 `fact`，且不使用 `def` 或 assignment statement 给它起名字。

写一个表达式，只使用 call expressions、conditional expressions 和 `lambda` expressions 来计算 `n` 的阶乘（不使用 assignment 或 `def` statements）。

> **注意：**
> 你的 return 表达式中不允许使用 `make_anonymous_factorial`。

`operator` 模块中的 `sub` 和 `mul` functions 是解决这道题唯一需要用到的内置 functions。

> **提示：**
> 为了递归地计算阶乘，你需要一个在 recursive calls 中使用的名字。
> 除了 assignment statements 和 `def` statements，
> 我们还学过哪些给某个东西起名字的其他方法？

```
from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
```

使用 Ok 来测试你的代码：

```
python3 ok -q make_anonymous_factorial

Copy

✂️
```

* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Recursion](index.html#recursion "index.html#recursion")

- [Q1: Num Eights](index.html#q1-num-eights "index.html#q1-num-eights")
- [Q2: Digit Distance](index.html#q2-digit-distance "index.html#q2-digit-distance")
- [Q3: Interleaved Sum](index.html#q3-interleaved-sum "index.html#q3-interleaved-sum")

+ [Tree Recursion](index.html#tree-recursion "index.html#tree-recursion")

- [Q4: Count Dollars](index.html#q4-count-dollars "index.html#q4-count-dollars")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Optional Questions](index.html#optional-questions "index.html#optional-questions")

+ [Q5: Count Dollars Upward](index.html#q5-count-dollars-upward "index.html#q5-count-dollars-upward")

* [Exam Practice](index.html#exam-practice "index.html#exam-practice")
* [Just For Fun Questions](index.html#just-for-fun-questions "index.html#just-for-fun-questions")

+ [Q6: Knapsack](index.html#q6-knapsack "index.html#q6-knapsack")
+ [Q7: Towers of Hanoi](index.html#q7-towers-of-hanoi "index.html#q7-towers-of-hanoi")
+ [Q8: Anonymous Factorial](index.html#q8-anonymous-factorial "index.html#q8-anonymous-factorial")
