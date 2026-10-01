Homework 6 | CS 61A Spring 2026



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



Homework 6: OOP, Linked Lists, Mutable Trees

* [hw06.zip](hw06.zip "hw06.zip")
===============================================================================

*截止时间为 3 月 19 日（周四）晚上 11:59。*

Instructions
------------

这份 homework 相当长，尽早开始对你更有利。下载 [hw06.zip](hw06.zip "hw06.zip")。在该压缩包中，你会找到一个名为 [hw06.py](hw06.py "hw06.py") 的文件，以及一份 `ok` autograder 的副本。

**提交：** 完成后，请把作业提交到 Gradescope。你可以在截止时间前多次提交；只有最后一次提交会被计分。请检查你是否已经在 Gradescope 上成功提交了你的代码。提交作业的更多说明见 [Lab 0](../../lab/lab00.html "../../lab/lab00.html")。

**使用 Ok：** 如果你对使用 Ok 有任何疑问，请参考[这份指南。](../../articles/using-ok.html "../../articles/using-ok.html")

**评分：** Homework 依据正确性评分。每答错一道题，总分就会减少一分。**这份 homework 满分为 2 分。**

Required Questions
==================

  

Midsemester Survey
------------------

### Q1: Mid-Semester Feedback

作为这份作业的一部分，请填写 [Mid-Semester Feedback](https://forms.gle/7SMhFR2qELXQvpqG8 "https://forms.gle/7SMhFR2qELXQvpqG8") 表单。

完成问卷后，你会看到一个 passphrase。请把这个 passphrase 作为一个 string，填到这份作业的 Python 文件中写着 `passphrase = 'REPLACE_THIS_WITH_PASSPHRASE'` 的那一行。例如，如果 passphrase 是 `abc`，那么这一行应该是 `passphrase = 'abc'`。

使用 Ok 来测试你的代码：

```
python3 ok -q midsem_survey

Copy

✂️
```

  
  

OOP
---

### Q2: Vending Machine

在这道题中，你将创建一个[自动售货机](https://en.wikipedia.org/wiki/Vending_machine "https://en.wikipedia.org/wiki/Vending_machine")，它只售卖一种商品，并在需要时找零。

实现 `VendingMachine` class，它模拟一台只售卖某一特定商品的自动售货机。`VendingMachine` object 的 methods 返回 strings 来描述机器的状态和操作。请确保你的输出与 doctests 中提供的 strings *完全*一致，包括标点和空格。

> 你可能会觉得 Python 的 formatted string literals，即 [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting "https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting") 很有用。
> 一个简单的例子：
>
> ```
> >>> feeling = 'love'
> >>> course = 'CS 61A!'
> >>> combined_string = f'I {feeling} {course}'
> >>> combined_string
> 'I love CS 61A!'
> ```

```
class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product: str, price: int):
        """Set the product and its price, as well as other instance attributes."""
        "*** YOUR CODE HERE ***"

    def restock(self, n: int) -> str:
        """Add n to the stock and return a message about the updated stock level.

        E.g., Current candy stock: 3
        """
        "*** YOUR CODE HERE ***"

    def add_funds(self, n: int) -> str:
        """If the machine is out of stock, return a message informing the user to restock
        (and return their n dollars).

        E.g., Nothing left to vend. Please restock. Here is your $4.

        Otherwise, add n to the balance and return a message about the updated balance.

        E.g., Current balance: $4
        """
        "*** YOUR CODE HERE ***"

    def vend(self) -> str:
        """Dispense the product if there is sufficient stock and funds and
        return a message. Update the stock and balance accordingly.

        E.g., Here is your candy and $2 change.

        If not, return a message suggesting how to correct the problem.

        E.g., Nothing left to vend. Please restock.
              Please add $3 more funds.
        """
        "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q VendingMachine

Copy

✂️
```

  

Linked Lists
------------

Linked Lists (enable JavaScript)

A linked list 是一种用于存储 values sequence 的 data structure。对于某些操作，例如在一个很长的 list 中间插入一个 value，它比普通的内置 list 更高效。Linked lists 不是内置的，因此我们定义了一个名为 `Link` 的 class 来表示它们。A linked list 要么是一个 `Link` instance，要么是 `Link.empty`（它表示一个空的 linked list）。

一个 `Link` 的 instance 有两个 instance attributes：`first` 和 `rest`。

`Link` instance 的 `rest` attribute 应始终是一个 linked list：要么是另一个 `Link` instance，要么是 `Link.empty`。它绝不应该为 `None`。

要检查一个 linked list 是否为空，可将它与 `Link.empty` 比较。由于空的 list 永远只有一个，我们可以用 `is` 来比较，但用 `==` 也可以。

```
def is_empty(s):
    """Return whether linked list s is empty."""
    return s is Link.empty:
```

你可以用两种方式 mutate 一个 `Link` object `s`：

* 用 `s.first = ...` 修改第一个 element
* 用 `s.rest = ...` 修改其余的 elements

你可以通过调用 `Link` 来创建一个新的 `Link` object：

* `Link(4)` 创建一个长度为 1、包含 4 的 linked list。
* `Link(4, s)` 创建一个以 4 开头、后接 linked list `s` 的 elements 的 linked list。

### Q3: Store Digits

编写一个 function `store_digits`，它接收一个 integer `n`，并返回一个 linked list，其中按相同顺序（从左到右）包含 `n` 的各位数字。

> **重要**：不要使用任何 string 操作 functions，例如 `str` 或 `reversed`。

```
def store_digits(n: int):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> store_digits(2450)
    Link(2, Link(4, Link(5, Link(0))))
    >>> store_digits(20105)
    Link(2, Link(0, Link(1, Link(0, Link(5)))))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q store_digits

Copy

✂️
```

  

### Q4: Mutable Mapping

实现 `deep_map_mut(func, s)`，它把 function `func` 应用于 linked list `s` 中的每个 element。如果一个 element 本身就是一个 linked list，则同样递归地把 `func` 应用于它的 elements。

你的实现应该 *mutate* 原来的 linked list。**不要创建任何新的 linked lists。** 该 function 返回 `None`。

> **提示**：你可以使用内置的 `isinstance` function 来判断一个 element 是否是 linked list。
>
> ```
> >>> s = Link(1, Link(2, Link(3, Link(4))))
> >>> isinstance(s, Link)
> True
> >>> isinstance(s, int)
> False
> ```

> **构造检查**：这道题的最后一个测试用例会检查你的 function 没有创建任何新的 linked lists。如果你没有通过这个 doctest，请确保你没有通过调用 constructor 来创建 linked lists，即
>
> ```
> s = Link(1)
> ```

```
def deep_map_mut(func, s: Link) -> None:
    """Mutates a deep link s by replacing each item found with the
    result of calling func on the item. Does NOT create new Links (so
    no use of Link's constructor).

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> square = lambda x: x * x
    >>> print(link1)
    (3 (4) 5 6)
    >>> link2 = Link(1, Link(Link(Link(2, Link(3))), Link(4)))
    >>> double = lambda x: x * 2
    >>> print(link2)
    (1 ((2 3)) 4)
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(square, link1)
    ...     deep_map_mut(double, link2)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    (9 (16) 25 36)
    >>> print(link2)
    (2 ((4 6)) 8)
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q deep_map_mut

Copy

✂️
```

  

Mutable Trees
-------------

Trees (enable JavaScript)

一个 `Tree` instance 有两个 instance attributes：

* `label` 是存储在 tree 的 root 处的 value。
* `branches` 是一个由 `Tree` instances 组成的 list，保存 tree 其余部分的 labels。

`Tree` class（省略了它的 `__repr__` 和 `__str__` methods）定义如下：

```
class Tree:
    """A tree has a label and a list of branches.

    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
```

要由一个 label `x`（任意 value）和一个 branches list `bs`（一个由 `Tree` instances 组成的 list）构造一个 `Tree` instance，并把它命名为 `t`，可以写 `t = Tree(x, bs)`。

对于一棵 tree `t`：

* 它的 root label 可以是任意 value，`t.label` 求值为该 value。
* 它的 branches 始终是 `Tree` instances，`t.branches` 求值为其 branches 的 **list**。
* 如果 `t.branches` 为空，`t.is_leaf()` 返回 `True`，否则返回 `False`。
* 要构造一个 label 为 `x` 的 leaf，写 `Tree(x)`。

显示一棵 tree `t`：

* `repr(t)` 返回一个求值为等价 tree 的 Python expression。
* `str(t)` 为每个 label 返回一行，其缩进比其 parent 多一级，children 位于 parents 下方。

```
>>> t = Tree(3, [Tree(1, [Tree(4), Tree(1)]), Tree(5, [Tree(9)])])

>>> t         # displays the contents of repr(t)
Tree(3, [Tree(1, [Tree(4), Tree(1)]), Tree(5, [Tree(9)])])

>>> print(t)  # displays the contents of str(t)
3
  1
    4
    1
  5
    9
```

修改（也叫 mutate）一棵 tree `t`：

* `t.label = y` 把 `t` 的 root label 改为 `y`（任意 value）。
* `t.branches = ns` 把 `t` 的 branches 改为 `ns`（一个由 `Tree` instances 组成的 list）。
* mutate `t.branches` 会改变 `t`。例如，`t.branches.append(Tree(y))` 会添加一个 label 为 `y` 的 leaf 作为最右边的 branch。
* mutate `t` 中的任何 branch 都会改变 `t`。例如，`t.branches[0].label = y` 会把最左边 branch 的 root label 改为 `y`。

```
>>> t.label = 3.0
>>> t.branches[1].label = 5.0
>>> t.branches.append(Tree(2, [Tree(6)]))
>>> print(t)
3.0
  1
    4
    1
  5.0
    9
  2
    6
```

以下是 tree data abstraction 以 functional abstraction 实现与以 class 实现之间差异的总结：

| - | Tree constructor 和 selector functions | Tree class |
| --- | --- | --- |
| 构造一棵 tree | 要在给定 `label` 和 `branches` list 的情况下构造一棵 tree，我们调用 `tree(label, branches)` | 要在给定 `label` 和 `branches` list 的情况下构造一个 tree object，我们调用 `Tree(label, branches)`（它会调用 `Tree.__init__` method）。 |
| Label 和 branches | 要获取 tree `t` 的 label 或 branches，我们分别调用 `label(t)` 或 `branches(t)` | 要获取 tree `t` 的 label 或 branches，我们分别访问 instance attributes `t.label` 或 `t.branches`。 |
| 可变性 | functional tree data abstraction 是不可变的（在不违反其 abstraction barrier 的前提下），因为我们无法给 call expressions 赋值 | `Tree` instance 的 `label` 和 `branches` attributes 可以被重新赋值，从而 mutate 这棵 tree。 |
| 检查一棵 tree 是否为 leaf | 要检查一棵 tree `t` 是否为 leaf，我们调用 function `is_leaf(t)` | 要检查一棵 tree `t` 是否为 leaf，我们调用 method `t.is_leaf()`。这个 method 只能在 `Tree` objects 上调用。 |

### Q5: Prune Small

从一棵 tree 中移除一些 nodes 被称为对这棵 tree 进行 *pruning*。

完成 function `prune_small`，它接收一棵 `Tree` `t` 和一个数字 `n`。对于每个 branch 数多于 `n` 的 node，只保留 labels 最小的 `n` 个 branches，并移除（*prune*）其余的。

> **提示**：`max` function 接收一个 `iterable`，以及一个可选的 `key` 参数（它接收一个单参数 function）。例如，`max([-7, 2, -1], key=abs)` 会返回 `-7`，因为 `abs(-7)` 大于 `abs(2)` 和 `abs(-1)`。

```
def prune_small(t, n):
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest labels.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    while ____:
        largest = max(____, key=____)
        ____
    for b in t.branches:
        ____
```

使用 Ok 来测试你的代码：

```
python3 ok -q prune_small

Copy

✂️
```

  

### Q6: Delete

实现 `delete`，它接收一棵 Tree `t`，并移除所有 label 为 `x` 的非 root nodes。每个保留下来的 node 的 parent 是它最近的、未被移除的 ancestor。root node 永远不会被移除，即使它的 label 是 `x`。

```
def delete(t, x):
    """Remove all nodes labeled x below the root within Tree t. When a non-leaf
    node is deleted, the deleted node's children become children of its parent.

    The root node will never be removed.

    >>> t = Tree(3, [Tree(2, [Tree(2), Tree(2)]), Tree(2), Tree(2, [Tree(2, [Tree(2), Tree(2)])])])
    >>> delete(t, 2)
    >>> t
    Tree(3)
    >>> t = Tree(1, [Tree(2, [Tree(4, [Tree(2)]), Tree(5)]), Tree(3, [Tree(6), Tree(2)]), Tree(4)])
    >>> delete(t, 2)
    >>> t
    Tree(1, [Tree(4), Tree(5), Tree(3, [Tree(6)]), Tree(4)])
    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(2)]), Tree(2, [Tree(6),  Tree(2), Tree(7), Tree(8)]), Tree(4)])
    >>> delete(t, 2)
    >>> t
    Tree(1, [Tree(4), Tree(5), Tree(3, [Tree(6)]), Tree(6), Tree(7), Tree(8), Tree(4)])
    """
    new_branches = []
    for _________ in ________________:
        _______________________
        if b.label == x:
            __________________________________
        else:
            __________________________________
    t.branches = ___________________
```

使用 Ok 来测试你的代码：

```
python3 ok -q delete

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

Optional Questions
==================

### Q7: Two List

实现一个 function `two_list`，它接收两个 lists，并返回一个 linked list。第一个 list 包含我们想要放入 linked list 的 values，第二个 list 包含每个对应 value 的数量。假设两个 lists 大小相同，长度都至少为 1。假设第二个 list 中的所有 elements 都大于 0。

```
def two_list(vals, counts):
    """
    Returns a linked list according to the two lists that were passed in. Assume
    vals and counts are the same size. Elements in vals represent the value, and the
    corresponding element in counts represents the number of this value desired in the
    final linked list. Assume all elements in counts are greater than 0. Assume both
    lists have at least one element.
    >>> a = [1, 3]
    >>> b = [1, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(3))
    >>> a = [1, 3, 2]
    >>> b = [2, 2, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(1, Link(3, Link(3, Link(2)))))
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q two_list

Copy

✂️
```

  

Exam Practice
=============

Homework 作业中也会包含一些往年的考题供你尝试。这些题目没有提交要求；如果你想练练手，欢迎随意尝试！

Object-Oriented Programming

1. Spring 2022 MT2 Q8: [CS61A Presents The Game of Hoop.](../../exam/sp22/mt2/61a-sp22-mt2.pdf#page=17 "../../exam/sp22/mt2/61a-sp22-mt2.pdf#page=17")
2. Fall 2020 MT2 Q3: [Sparse Lists](../../exam/fa20/mt2/61a-fa20-mt2.pdf#page=9 "../../exam/fa20/mt2/61a-fa20-mt2.pdf#page=9")
3. Fall 2019 MT2 Q7: [Version 2.0](../../exam/fa19/mt2/61a-fa19-mt2.pdf#page=8 "../../exam/fa19/mt2/61a-fa19-mt2.pdf#page=8")

Linked Lists

1. Fall 2020 Final Q3: [College Party](../../exam/fa20/final/61a-fa20-final.pdf#page=9 "../../exam/fa20/final/61a-fa20-final.pdf#page=9")
2. Fall 2018 MT2 Q6: [Dr. Frankenlink](../../exam/fa18/mt2/61a-fa18-mt2.pdf#page=6 "../../exam/fa18/mt2/61a-fa18-mt2.pdf#page=6")
3. Spring 2017 MT1 Q5: [Insert](../../exam/sp17/mt1/61a-sp17-mt1.pdf#page=7 "../../exam/sp17/mt1/61a-sp17-mt1.pdf#page=7")

* [Instructions](index.html#instructions "index.html#instructions")
* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Midsemester Survey](index.html#midsemester-survey "index.html#midsemester-survey")

- [Q1: Mid-Semester Feedback](index.html#q1-mid-semester-feedback "index.html#q1-mid-semester-feedback")

+ [OOP](index.html#oop "index.html#oop")

- [Q2: Vending Machine](index.html#q2-vending-machine "index.html#q2-vending-machine")

+ [Linked Lists](index.html#linked-lists "index.html#linked-lists")

- [Q3: Store Digits](index.html#q3-store-digits "index.html#q3-store-digits")
- [Q4: Mutable Mapping](index.html#q4-mutable-mapping "index.html#q4-mutable-mapping")

+ [Mutable Trees](index.html#mutable-trees "index.html#mutable-trees")

- [Q5: Prune Small](index.html#q5-prune-small "index.html#q5-prune-small")
- [Q6: Delete](index.html#q6-delete "index.html#q6-delete")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Optional Questions](index.html#optional-questions "index.html#optional-questions")

+ [Q7: Two List](index.html#q7-two-list "index.html#q7-two-list")

* [Exam Practice](index.html#exam-practice "index.html#exam-practice")
