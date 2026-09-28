Lab 3: Recursion, Python Lists | CS 61A Spring 2026



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



Lab 3: Recursion, Python Lists

* [lab03.zip](lab03.zip "lab03.zip")
====================================================================

*截止时间为 2 月 18 日（周三）晚上 11:59。*

Starter Files
-------------

下载 [lab03.zip](lab03.zip "lab03.zip")。

Attendance
==========

如果你参加的是常规 61A lab，你的 TA 会过来为你 check in。你除了到场之外，还需要提交 lab problems，才能获得本次 lab 的学分。如果你参加的是 mega lab，那么只需提交 lab problems 即可获得学分。

如果你因为正当理由（例如生病或时间冲突）缺席 lab，或者因为某些原因没有被 check in，只需在两周内填写[此表单](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance")即可获得 attendance 学分。

Topics
======

如果你需要复习本次 lab 的材料，请查阅本节。你也可以直接跳到[题目部分](index.html#required-questions "index.html#required-questions")，遇到困难时再回到这里查阅。

Lists (enable JavaScript)

Lists
-----

A list 是一种数据结构，可以保存有序的 item 集合。这些 item 被称为 elements，可以是任何数据类型，包括 numbers、strings，甚至其他 lists。用方括号括起来的、以逗号分隔的表达式列表会创建一个 list：

```
>>> list_of_values = [2, 1, 3, True, 3]
>>> nested_list = [2, [1, 3], [True, [3]]]
```

A list 中的每个位置都有一个 index，最左边的 element 的 index 为 `0`。

```
>>> list_of_values[0]
2
>>> nested_list[1]
[1, 3]
```

负 index 从末尾开始计数，最右边的 element 的 index 为 `-1`。

```
>>> nested_list[-1]
[True, [3]]
```

将 lists 相加会得到一个新的、更长的 list，其中包含被相加的 lists 的 elements。

```
>>> [1, 2] + [3] + [4, 5]
[1, 2, 3, 4, 5]
```

List Comprehensions (enable JavaScript)

List Comprehensions
-------------------

A list comprehension 描述一个 list 中的 elements，并求值为一个包含这些 elements 的新 list。

它有两种形式：

```
[<expression> for <element> in <sequence>]
[<expression> for <element> in <sequence> if <conditional>]
```

下面是一个例子：以 `[1, 2, 3, 4]` 开始，用 `if i % 2 == 0` 挑出偶数 elements `2` 和 `4`，然后用 `i*i` 对它们分别求平方。`for i` 的作用是为 `[1, 2, 3, 4]` 中的每个 element 起一个名字。

```
>>> [i*i for i in [1, 2, 3, 4] if i % 2 == 0]
[4, 16]
```

这个 list comprehension 求值为一个由以下内容构成的 list：

* `i*i` 的值
* 对于 sequence `[1, 2, 3, 4]` 中的每个 element `i`
* 且满足 `i % 2 == 0`

换句话说，这个 list comprehension 会创建一个新 list，其中包含原 list `[1, 2, 3, 4]` 中每个偶数 element 的平方。

我们也可以把 list comprehension 改写为等价的 `for` statement，比如上面的例子可以写成：

```
>>> result = []
>>> for i in [1, 2, 3, 4]:
...     if i % 2 == 0:
...         result = result + [i*i]
>>> result
[4, 16]
```

For Loops (enable JavaScript)

`for` Statements
----------------

A `for` statement 会针对 sequence（例如 list 或 range）的每个 element 执行一段代码。每次执行代码时，`for` 后面的名字会被绑定到 sequence 中不同的 element。

```
for <name> in <expression>:
    <suite>
```

首先，`<expression>` 会被求值。它必须求值为一个 sequence。然后，按顺序对 sequence 中的每个 element，

1. `<name>` 被绑定到该 element。
2. `<suite>` 被执行。

下面是一个例子：

```
for x in [-1, 4, 2, 0, 5]:
    print("Current elem:", x)
```

它会显示如下内容：

```
Current elem: -1
Current elem: 4
Current elem: 2
Current elem: 0
Current elem: 5
```

Ranges (enable JavaScript)

Ranges
------

A range 是一种数据结构，用于保存整数 sequence。range 可以通过以下方式创建：

* `range(stop)` 包含 0, 1, ..., `stop` - 1
* `range(start, stop)` 包含 `start`, `start` + 1, ..., `stop` - 1

注意 range function 不包含 `stop` 值；它生成到 `stop` 值为止的数字，但不包括 `stop` 值。

例如：

```
>>> for i in range(3):
...     print(i)
...
0
1
2
```

虽然 ranges 和 lists 都是 [sequences](https://en.wikibooks.org/wiki/Python_Programming/Sequences "https://en.wikibooks.org/wiki/Python_Programming/Sequences")，但 range object 与 list 不同。可以通过调用 `list()` 把 range 转换为 list：

```
>>> range(3, 6)
range(3, 6)  # this is a range object
>>> list(range(3, 6))
[3, 4, 5]  # list() converts the range object to a list
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(1, 6))
[1, 2, 3, 4, 5]
```

  

Type Checking
=============

Type hints 可以出现在 `assignment` 和 `def` statements（以及少数其他位置）中，用于指明变量应该具有的值类型，或者 function 应该返回的类型。

一个没有 type hints 的例子：

```
x = 4

def pair(y, z):
    return [y, z]
```

同样例子的 type hints，表明 `x`、`y` 和 `z` 是 integers，并且 `pair` function 返回一个整数 list：

```
x: int = 4

def pair(y: int, z: int) -> list[int]:
    return [y, z]
```

无论有没有 type hints，代码的行为都完全相同。你可以在 [type hints](../../articles/type-hints.html "../../articles/type-hints.html") 一文中阅读更多内容。

**Automatic Type Checking**：VS Code 可以被配置为在某个变量被赋了一个类型不符合预期的值时，在相应位置进行标注。要启用 type checking，请打开 VS Code 设置：在 Mac 上同时按 Command 和 `,` 键，在 Windows 上同时按 Control 和 `,` 键。在搜索栏中输入 `type checking`，应该会显示出下方截图中的 Type Checking 选项。使用下拉菜单将 type checking 从默认的 `off` 改为 `basic`。

![type-hints](assets/type_hints_vscode.png)

如果没有出现这些 type checking 选项，你可能需要安装 Pylance 扩展。在 Mac 上同时按住 Shift、Command 和 `X`，在 Windows 上同时按住 Shift、Control 和 `X`，即可打开 Extensions 视图。在搜索栏中输入 `Pylance`，然后按安装按钮。

要确认 type checking 已启用，请在 Python 文件中输入以下内容：

```
a: int = 'not an int'
```

你应该会在 `'not an int'` 下方看到红色波浪线。如果你把鼠标悬停在 `'not an int'` 上，VS Code 会显示一条错误信息，说明 `'not an int'` 与期望的类型 `int` 不匹配。写代码时请留意这些错误！它们通常是在提示你代码中的 bug 所在。

Required Questions
==================

Lists
-----

> **重要：**
> 对于所有 WWPD 题目，如果你认为答案是
> `<function...>`，请输入 `Function`；如果会报错，请输入 `Error`；如果没有显示任何内容，请输入 `Nothing`。
>
> ### Q1: WWPD: Lists & Ranges
>
> 使用 Ok 来通过以下 "What Would Python Display?" 题目检验你的理解：
>
> ```
> python3 ok -q lists-wwpd -u
>
> Copy
>
> ✂️
> ```

预测当你在交互式解释器中输入以下内容时 Python 会显示什么。然后实际运行以检验你的答案。

```
>>> s = [7//3, 5, [4, 0, 1], 2]
>>> s[0]

______



2

>>> s[2]

______



[4, 0, 1]

>>> s[-1]

______



2

>>> len(s)

______



4

>>> 4 in s

______



False

>>> 4 in s[2]

______



True

>>> s[2] + [3 + 2]

______



[4, 0, 1, 5]

>>> 5 in s[2]

______



False

>>> s[2] * 2

______



[4, 0, 1, 4, 0, 1]

>>> list(range(3, 6))

______



[3, 4, 5]

>>> range(3, 6)

______



range(3, 6)

>>> r = range(3, 6)
>>> [r[0], r[2]]

______



[3, 5]

>>> range(4)[-1]

______



3
```

Toggle Solution (enable JavaScript)

### Q2: Close

实现 `close`，它接收一个整数 list `s` 和一个非负 integer `k`。它返回 `s` 中有多少个 element 与其 index 的差在 `k` 以内。也就是说，element 与其 index 之差的绝对值小于或等于 `k`。

> 记住 list 是 "zero-indexed" 的；第一个 element 的 index 是 `0`。

```
def close(s: list[int], k: int) -> int:
    """Return how many elements of s are within k of their index.

    >>> t = [6, 2, 4, 3, 5]
    >>> close(t, 0)  # Only 3 is equal to its index
    1
    >>> close(t, 1)  # 2, 3, and 5 are within 1 of their index
    3
    >>> close(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    4
    >>> close(list(range(10)), 0)
    10
    """
    assert k >= 0
    count = 0
    for i in range(len(s)):  # Use a range to loop over indices
        "*** YOUR CODE HERE ***"
    return count
```

使用 Ok 来测试你的代码：

```
python3 ok -q close

Copy

✂️
```

  

List Comprehensions
-------------------

> **重要：**
> 对于所有 WWPD 题目，如果你认为答案是
> `<function...>`，请输入 `Function`；如果会报错，请输入 `Error`；如果没有显示任何内容，请输入 `Nothing`。
>
> ### Q3: WWPD: List Comprehensions
>
> 使用 Ok 来通过以下 "What Would Python Display?" 题目检验你的理解：
>
> ```
> python3 ok -q list-comprehensions-wwpd -u
>
> Copy
>
> ✂️
> ```

预测当你在交互式解释器中输入以下内容时 Python 会显示什么。然后实际运行以检验你的答案。

```
>>> [2 * x for x in range(4)]

______



[0, 2, 4, 6]

>>> [y for y in [6, 1, 6, 1] if y > 2]

______



[6, 6]

>>> [[1] + s for s in [[4], [5, 6]]]

______



[[1, 4], [1, 5, 6]]

>>> [z + 1 for z in range(10) if z % 3 == 0]

______



[1, 4, 7, 10]
```

Toggle Solution (enable JavaScript)

### Q4: Close List

实现 `close_list`，它接收一个整数 list `s` 和一个非负 integer `k`。它返回一个 list，其中包含 `s` 中与其 index 的差在 `k` 以内的 elements。也就是说，element 与其 index 之差的绝对值小于或等于 `k`。

```
def close_list(s: list[int], k: int) -> list[int]:
    """Return a list of the elements of s that are within k of their index.

    >>> t = [6, 2, 4, 3, 5]
    >>> close_list(t, 0)  # Only 3 is equal to its index
    [3]
    >>> close_list(t, 1)  # 2, 3, and 5 are within 1 of their index
    [2, 3, 5]
    >>> close_list(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    [2, 4, 3, 5]
    """
    assert k >= 0
    return [___ for i in range(len(s)) if ___]
```

使用 Ok 来测试你的代码：

```
python3 ok -q close_list

Copy

✂️
```

  

Recursion
---------

### Q5: Double Eights

写一个 **recursive** function，它接收一个正整数 `n`，并判断它的各位数字中是否包含两个相邻的 `8`（也就是两个紧挨着的 `8`）。

> **提示：** 先想出一个 recursive plan：一个数字的各位数字包含 double eights，当且仅当（想想有什么是容易检查的）或者其余数字中包含 double eights。
>
> **重要：** 使用 recursion；如果你使用任何循环（for、while）、`in` 运算符或 `str` function，测试将会失败。

```
def double_eights(n: int) -> bool:
    """Returns whether or not n has two digits in row that
    are the number 8.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> # ban iteration, in operator and str function 
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'double_eights', ['While', 'For', 'In', 'Str'])
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q double_eights

Copy

✂️
```

  

### Q6: Making Onions

写一个 function `make_onion`，它接收两个单参数 function `f` 和 `g`。它返回一个接收三个参数 `x`、`y` 和 `limit` 的 function。若可以只通过最多 `limit` 次对 `f` 和 `g` 的调用，从 `x` 得到 `y`，则该返回的 function 返回 `True`，否则返回 `False`。

例如，如果 `f` 表示加 1，`g` 表示乘以 2，那么可以从 5 出发在四次调用内得到 25：`f(g(g(f(5))))`。

```
def make_onion(f, g):
    """Return a function can_reach(x, y, limit) that returns
    whether some call expression containing only f, g, and x with
    up to limit calls will give the result y.

    >>> up = lambda x: x + 1
    >>> double = lambda y: y * 2
    >>> can_reach = make_onion(up, double)
    >>> can_reach(5, 25, 4)      # 25 = up(double(double(up(5))))
    True
    >>> can_reach(5, 25, 3)      # Not possible
    False
    >>> can_reach(1, 1, 0)      # 1 = 1
    True
    >>> add_ing = lambda x: x + "ing"
    >>> add_end = lambda y: y + "end"
    >>> can_reach_string = make_onion(add_ing, add_end)
    >>> can_reach_string("cry", "crying", 1)      # "crying" = add_ing("cry")
    True
    >>> can_reach_string("un", "unending", 3)     # "unending" = add_ing(add_end("un"))
    True
    >>> can_reach_string("peach", "folding", 4)   # Not possible
    False
    """
    def can_reach(x, y, limit):
        if limit < 0:
            return ____
        elif x == y:
            return ____
        else:
            return can_reach(____, ____, limit - 1) or can_reach(____, ____, limit - 1)
    return can_reach
```

使用 Ok 来测试你的代码：

```
python3 ok -q make_onion

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

把这份作业提交上去，方法是把你编辑过的所有文件上传到**对应的 Gradescope 作业**。[Lab 00](../lab00.html#submitting-the-assignment "../lab00.html#submitting-the-assignment") 中有详细说明。

正确完成所有题目值 1 分。如果你参加的是常规 lab，你还需要 TA 记录的 attendance 才能拿到这 1 分。请在离开前确认你的 TA 已经记录了你的 attendance。

Optional Questions
==================

> 这些题目是可选的。如果你没有完成它们，
> 你仍然可以获得这份作业的学分。它们是很好的练习，所以还是做一下吧！

### Q7: Function Repeater

定义一个 function `make_fn_repeater`，它接收一个单参数 function `f` 和一个 integer `x`。它应该返回另一个 function，该 function 接收一个参数，也就是另一个 integer。这个 function 返回把 `f` 作用于 `x` 该次数后的结果。

确保你的解法使用 recursion。

```
def make_func_repeater(f, x):
    """
    >>> increment_repeater = make_func_repeater(lambda x: x + 1, 1)
    >>> increment_repeater(2) #same as f(f(x))
    3
    >>> increment_repeater(5)
    6
    """
    def repeat(____):
        if ____:
            return ____
        else:
            return ____
    return ____
```

使用 Ok 来测试你的代码：

```
python3 ok -q make_func_repeater

Copy

✂️
```

  

这道题和某道 homework 题目非常相似，但是要求用 recursion。
如果有时间，我们建议讲一讲这道题，它以一种有趣的方式把 recursion 和 higher order functions 结合了起来。
请务必与 self-reference 做对比，说明为什么这不是 self-reference，
无论是在行为上（这里一次 function 调用会产生大量计算，而不是许多次 function 调用）
还是在实现上（这里调用 repeat 是*调用* repeat，而不是返回一个新的 repeat function）。

### Q8: Ten-Pairs

写一个 function，它接收一个正整数 `n`，并返回其中包含的 ten-pairs 的数量。一个 ten-pair 是 `n` 中两个和为 10 的数字组成的数对。

数字 7,823,952 有 3 个 ten-pairs。第一位和第四位数字之和为 7+3=10，第二位和第三位数字之和为 8+2=10，第二位和最后一位数字之和为 8+2=10。

重要说明：

* 一个数字可以属于多个 ten-pairs。
* 一个 5 不能和它自己组成一个 ten-pair。

> *建议*：完成并使用 helper function `count_digit` 来计算某个数字在 `n` 中出现的次数。

**重要：** 使用 recursion；如果你使用任何循环（for、while），测试将会失败。

```
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952) # 7+3, 8+2, and 8+2
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469) # 9+1, 6+4, 6+4, 4+6, 1+9, 4+6 
    6
    >>> # ban iteration
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'ten_pairs', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5) # digit 5 appears 4 times in 55055
    4
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q ten_pairs

Copy

✂️
```

* [Attendance](index.html#attendance "index.html#attendance")
* [Topics](index.html#topics "index.html#topics")
* [Type Checking](index.html#type-checking "index.html#type-checking")
* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Lists](index.html#lists "index.html#lists")

- [Q1: WWPD: Lists & Ranges](index.html#q1-wwpd-lists-amp-ranges "index.html#q1-wwpd-lists-amp-ranges")
- [Q2: Close](index.html#q2-close "index.html#q2-close")

+ [List Comprehensions](index.html#list-comprehensions "index.html#list-comprehensions")

- [Q3: WWPD: List Comprehensions](index.html#q3-wwpd-list-comprehensions "index.html#q3-wwpd-list-comprehensions")
- [Q4: Close List](index.html#q4-close-list "index.html#q4-close-list")

+ [Recursion](index.html#recursion "index.html#recursion")

- [Q5: Double Eights](index.html#q5-double-eights "index.html#q5-double-eights")
- [Q6: Making Onions](index.html#q6-making-onions "index.html#q6-making-onions")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Optional Questions](index.html#optional-questions "index.html#optional-questions")

+ [Q7: Function Repeater](index.html#q7-function-repeater "index.html#q7-function-repeater")
+ [Q8: Ten-Pairs](index.html#q8-ten-pairs "index.html#q8-ten-pairs")
