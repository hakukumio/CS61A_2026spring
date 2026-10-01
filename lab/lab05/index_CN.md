Lab 5: Mutability, Iterators | CS 61A Spring 2026



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



Lab 5: Mutability, Iterators

* [lab05.zip](lab05.zip "lab05.zip")
==================================================================

*截止时间为 3 月 4 日（周三）晚上 11:59。*

Starter Files
-------------

下载 [lab05.zip](lab05.zip "lab05.zip")。

Attendance
==========

如果你参加的是常规 61A lab，你的 TA 会过来为你 check in。你除了到场之外，还需要提交 lab problems，才能获得本次 lab 的学分。如果你参加的是 mega lab，那么只需提交 lab problems 即可获得学分。

如果你因为正当理由（例如生病或时间冲突）缺席 lab，或者因为某些原因没有被 check in，只需在两周内填写[此表单](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance")即可获得 attendance 学分。

Required Questions
==================

Mutability
----------

如果你需要复习 mutability，请查阅下拉框。你也可以直接跳到题目部分，遇到困难时再回到这里查阅。

List Mutation (enable JavaScript)

Python 中有些 objects，例如 lists 和 dictionaries，是 **mutable** 的，这意味着它们的内容或状态可以改变。其他 objects，例如 numeric types、tuples 和 strings，是 **immutable** 的，这意味着它们一旦创建就不能被修改。

lists 最常见的两种 mutation 操作是 item assignment 和 `append` method。

```
>>> s = [1, 3, 4]
>>> t = s  # A second name for the same list
>>> t[0] = 2  # this changes the first element of the list to 2, affecting both s and t
>>> s
[2, 3, 4]
>>> s.append(5)  # this adds 5 to the end of the list, affecting both s and t
>>> t
[2, 3, 4, 5]
```

还有许多其他 list mutation methods：

* `append(elem)`：把 `elem` 添加到 list 末尾。返回 `None`。
* `extend(s)`：把 iterable `s` 的所有 elements 添加到 list 末尾。返回 `None`。
* `insert(i, elem)`：在 index `i` 处插入 `elem`。如果 `i` 大于或等于 list 的长度，则把 `elem` 插入到末尾。这不会替换任何已有的 elements，只是添加新 element `elem`。返回 `None`。
* `remove(elem)`：移除 `elem` 在 list 中第一次出现的位置。返回 `None`。如果 `elem` 不在 list 中则会报错。
* `pop(i)`：移除并返回 index `i` 处的 element。
* `pop()`：移除并返回最后一个 element。

Dictionaries 也有 item assignment（经常使用）和 `pop`（很少使用）。

```
>>> d = {2: 3, 4: 16}
>>> d[2] = 4
>>> d[3] = 9
>>> d
{2: 4, 4: 16, 3: 9}
>>> d.pop(4)
16
>>> d
{2: 4, 3: 9}
```

### Q1: WWPD: List-Mutation

> **重要：**
> 对于所有 WWPD 题目，如果你认为答案是
> `<function...>`，请输入 `Function`；如果会报错，请输入 `Error`；如果没有显示任何内容，请输入 `Nothing`。

> 使用 Ok 来通过以下 "What Would Python Display?" 题目检验你的理解：
>
> ```
> python3 ok -q list-mutation -u
>
> Copy
>
> ✂️
> ```

```
>>> s = [6, 7, 8]
>>> print(s.append(6))

______



None

>>> s

______



[6, 7, 8, 6]

>>> s.insert(0, 9)
>>> s

______



[9, 6, 7, 8, 6]

>>> x = s.pop(1)
>>> s

______



[9, 7, 8, 6]

>>> s.remove(x)
>>> s

______



[9, 7, 8]

>>> a, b = s, s[:]
>>> a is s

______



True

>>> b == s

______



True

>>> b is s

______



False

>>> a.pop()

______



8

>>> a + b

______



[9, 7, 9, 7, 8]

>>> s = [3]
>>> s.extend([4, 5])
>>> s

______



[3, 4, 5]

>>> a

______



[9, 7]

>>> s.extend([s.append(9), s.append(10)])
>>> s

______



[3, 4, 5, 9, 10, None, None]
```

Toggle Solution (enable JavaScript)

### Q2: Insert Items

写一个 function，它接收一个 list `s`、一个 value `before` 和一个 value `after`。它就地修改 `s`，在每个等于 `before` 的 value 之后插入 `after`。它返回 `s`。

> **重要：** 不应创建任何新的 lists。

> **注意：**
> 如果传入 `before` 和 `after` 的 values 相等，请确保你在遍历 list 时没有创建无限长的 list。如果你发现代码运行时间超过几秒钟，该 function 可能陷入了不断插入新 values 的无限循环。

```
def insert_items(s: list[int], before: int, after: int) -> list[int]:
    """Insert after into s following each occurrence of before and then return s.

    >>> test_s = [1, 5, 8, 5, 2, 3]
    >>> new_s = insert_items(test_s, 5, 7)
    >>> new_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> test_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> new_s is test_s
    True
    >>> double_s = [1, 2, 1, 2, 3, 3]
    >>> double_s = insert_items(double_s, 3, 4)
    >>> double_s
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_s = [1, 4, 8]
    >>> large_s2 = insert_items(large_s, 4, 4)
    >>> large_s2
    [1, 4, 4, 8]
    >>> large_s3 = insert_items(large_s2, 4, 6)
    >>> large_s3
    [1, 4, 6, 4, 6, 8]
    >>> large_s3 is large_s
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q insert_items

Copy

✂️
```

  

### Q3: Group By

写一个 function，它接收一个 list `s` 和一个 function `fn`，并返回一个 dictionary，根据对 `s` 的 elements 应用 `fn` 的结果进行分组。

* 对于把 `fn` 应用到 `s` 的 elements 上得到的每个不同结果，dictionary 都应该有一个对应的 key。
* 每个 key 的 value 应是一个 list，包含 `s` 中所有传给 `fn` 后能产生该 key（也就是其求值结果）的 elements。

换句话说，对于 `s` 中的每个 element `e`，求出 `fn(e)`，把 `e` 添加到 dictionary 中 `fn(e)` 对应的 list 里。

```
def group_by(s: list[int], fn) -> dict[int, list[int]]:
    """Return a dictionary of lists that together contain the elements of s.
    The key for each list is the value that fn returns when called on any of the
    values of that list.

    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for ____ in ____:
        key = ____
        if key in grouped:
            ____
        else:
            grouped[key] = ____
    return grouped
```

使用 Ok 来测试你的代码：

```
python3 ok -q group_by

Copy

✂️
```

  

### Q4: Sprout Leaves

定义一个 function `sprout_leaves`，它接收一棵 tree `t` 和一个 leaf labels 的 list `leaves`。它返回一棵与 `t` 完全相同的新 tree，但其中每个原来的 leaf node 都长出了新的 branches，`leaves` 中的每个 leaf label 对应一个 branch。

例如，假设我们有 tree `t = tree(1, [tree(2), tree(3, [tree(4)])])`：

```
  1
 / \
2   3
    |
    4
```

如果我们调用 `sprout_leaves(t, [5, 6])`，结果就是下面这棵 tree：

```
       1
     /   \
    2     3
   / \    |
  5   6   4
         / \
        5   6
```

```
def sprout_leaves(t, leaves):
    """Sprout new leaves containing the labels in leaves at each leaf of
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q sprout_leaves

Copy

✂️
```

  

Iterators
---------

如果你需要复习 iterators，请查阅下拉框。你也可以直接跳到题目部分，遇到困难时再回到这里查阅。

Iterators (enable JavaScript)

一个 **iterable** 是任何可以被迭代、也就是可以一次一个 element 地遍历的 value。我们用来遍历 iterable 的一种结构是 for statement：

```
for elem in iterable:
    # do something
```

一般来说，一个 **iterable** 是这样一个 object：对它调用内置的 `iter` function 会返回一个 *iterator*。一个 **iterator** 是这样一个 object：对它调用内置的 `next` function 会返回下一个 value。

例如，一个 list 就是一个 iterable value。

```
>>> s = [1, 2, 3, 4]
>>> next(s)       # s is iterable, but not an iterator
TypeError: 'list' object is not an iterator
>>> t = iter(s)   # Creates an iterator
>>> t
<list_iterator object ...>
>>> next(t)       # Calling next on an iterator
1
>>> next(t)       # Calling next on the same iterator
2
>>> next(iter(t)) # Calling iter on an iterator returns itself
3
>>> t2 = iter(s)
>>> next(t2)      # Second iterator starts at the beginning of s
1
>>> next(t)       # First iterator is unaffected by second iterator
4
>>> next(t)       # No elements left!
StopIteration
>>> s             # Original iterable is unaffected
[1, 2, 3, 4]
```

你也可以在 `for` statement 中使用 iterator，因为所有 iterators 都是 iterable 的。但请注意，由于 iterators 会保存自己的状态，它们只适合遍历一次 iterable：

```
>>> t = iter([4, 3, 2, 1])
>>> for e in t:
...     print(e)
4
3
2
1
>>> for e in t:
...     print(e)
```

有一些内置 functions 会返回 iterators。这些内置的 Python sequence 操作会惰性地计算结果。

```
>>> m = map(lambda x: x * x, [3, 4, 5])
>>> next(m)
9
>>> next(m)
16
>>> f = filter(lambda x: x > 3, [3, 4, 5])
>>> next(f)
4
>>> next(f)
5
>>> z = zip([30, 40, 50], [3, 4, 5])
>>> next(z)
(30, 3)
>>> next(z)
(40, 4)
```

### Q5: WWPD: Iterators

> **重要：**
> 如果发生 `StopIteration` exception，请输入 `StopIteration`，
> 如果你认为发生的是别的错误，请输入 `Error`，
> 如果输出是一个 iterator object，请输入 `Iterator`。

> **重要：** Python 的内置 function `map`、`filter` 和 `zip` 返回的是 *iterators*，而不是 lists。

> 使用 Ok 来通过以下 "What Would Python Display?" 题目检验你的理解：
>
> ```
> python3 ok -q iterators-wwpd -u
>
> Copy
>
> ✂️
> ```

```
>>> s = [1, 2, 3, 4]
>>> t = iter(s)
>>> next(s)

______



Error

>>> next(t)

______



1

>>> next(t)

______



2

>>> next(iter(s))

______



1

>>> next(iter(s))

______



1

>>> u = t
>>> next(u)

______



3

>>> next(t)

______



4
```

Toggle Solution (enable JavaScript)

```
>>> r = range(6)
>>> r_iter = iter(r)
>>> next(r_iter)

______



0

>>> [x + 1 for x in r]

______



[1, 2, 3, 4, 5, 6]

>>> [x + 1 for x in r_iter]

______



[2, 3, 4, 5, 6]

>>> next(r_iter)

______



StopIteration
```

Toggle Solution (enable JavaScript)

```
>>> map_iter = map(lambda x : x + 10, range(5))
>>> next(map_iter)

______



10

>>> next(map_iter)

______



11

>>> list(map_iter)

______



[12, 13, 14]

>>> for e in filter(lambda x : x % 4 == 0, range(1000, 1008)):
...     print(e)

______



1000
1004

>>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]

______



[5, 7, 9]
```

Toggle Solution (enable JavaScript)

### Q6: Count Occurrences

实现 `count_occurrences`，它接收一个 iterator `t`、一个 integer `n` 和一个 value `x`。它返回 `t` 的前 `n` 个 elements 中等于 `x` 的 element 数量。

你可以假设 `t` 至少有 `n` 个 elements。

> **重要**：你应该对 `t` 恰好调用 `next` `n` 次。如果你需要遍历超过 `n` 个 elements，想想如何优化你的解法。

```
from typing import Iterator  # "t: Iterator[int]" means t is an iterator that yields integers

def count_occurrences(t: Iterator[int], n: int, x: int) -> int:
    """Return the number of times that x is equal to one of the
    first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(t, 3, 10)
    2
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(u, 1, 3)  # Only iterate over 3
    1
    >>> count_occurrences(u, 3, 2)  # Only iterate over 2, 2, 2
    3
    >>> list(u)                     # Ensure that the iterator has advanced the right amount
    [1, 2, 1, 4, 4, 5, 5, 5]
    >>> v = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
    >>> count_occurrences(v, 6, 6)
    2
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q count_occurrences

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

把这份作业提交上去，方法是把你编辑过的所有文件上传到**对应的 Gradescope 作业**。[Lab 00](../lab00.html#submitting-the-assignment "../lab00.html#submitting-the-assignment") 中有详细说明。

正确完成所有题目值 1 分。如果你参加的是常规 lab，你还需要 TA 记录的 attendance 才能拿到这 1 分。请在离开前确认你的 TA 已经记录了你的 attendance。

Optional Questions
==================

> 这些题目是可选的。如果你没有完成它们，你仍然可以获得这份作业的学分。它们是很好的练习，所以还是做一下吧！

### Q7: Path Sum

定义一个 function `pathsum`，它接收一棵装数字的 tree `t` 和一个数 `n`。如果存在一条从根到 leaf 的 path，使得沿该 path 的数字之和为 `n`，则返回 `True`，否则返回 `False`。

```
def pathsum(t, n):
    """
    >>> my_tree = tree(2, [tree(3, [tree(5), tree(7)]), tree(4)])
    >>> pathsum(my_tree, 12) # 2 -> 3 -> 7
    True
    >>> pathsum(my_tree, 5)  # A path that doesn't reach a leaf such as 2 -> 3 doesn't count
    False
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q pathsum

Copy

✂️
```

  

### Q8: Perfectly Balanced

实现 `sum_tree`，它返回 tree `t` 中所有 labels 的和。

```
def sum_tree(t):
    """Add all elements in a tree.

    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q sum_tree

Copy

✂️
```

  

然后实现 `balanced`，它返回 `t` 的每个 branch 是否都具有相同的总和，并且每个 branch 自身是否也平衡。

![Example Tree](assets/just-balanced.JPG)

* 例如，上面的 tree 是平衡的，因为每个 branch 的总和都相同，而且每个 branch 自身也是平衡的。

```
def balanced(t):
    """Checks if each branch has same sum of all elements and
    if each branch is balanced.

    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q balanced

Copy

✂️
```

  
> **挑战：**
> 两个部分都只用 1 行代码来解决。

* [Attendance](index.html#attendance "index.html#attendance")
* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Mutability](index.html#mutability "index.html#mutability")

- [Q1: WWPD: List-Mutation](index.html#q1-wwpd-list-mutation "index.html#q1-wwpd-list-mutation")
- [Q2: Insert Items](index.html#q2-insert-items "index.html#q2-insert-items")
- [Q3: Group By](index.html#q3-group-by "index.html#q3-group-by")
- [Q4: Sprout Leaves](index.html#q4-sprout-leaves "index.html#q4-sprout-leaves")

+ [Iterators](index.html#iterators "index.html#iterators")

- [Q5: WWPD: Iterators](index.html#q5-wwpd-iterators "index.html#q5-wwpd-iterators")
- [Q6: Count Occurrences](index.html#q6-count-occurrences "index.html#q6-count-occurrences")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Optional Questions](index.html#optional-questions "index.html#optional-questions")

+ [Q7: Path Sum](index.html#q7-path-sum "index.html#q7-path-sum")
+ [Q8: Perfectly Balanced](index.html#q8-perfectly-balanced "index.html#q8-perfectly-balanced")
