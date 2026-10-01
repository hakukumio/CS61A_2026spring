Homework 4 | CS 61A Spring 2026



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



Homework 4: Sequences, Data Abstraction, Trees

* [hw04.zip](hw04.zip "hw04.zip")
=================================================================================

*截止时间为 3 月 5 日（周四）晚上 11:59。*

Instructions
------------

下载 [hw04.zip](hw04.zip "hw04.zip")。在压缩包中，你会找到一个名为 [hw04.py](hw04.py "hw04.py") 的文件，以及一份 `ok` 自动评分器的副本。

**提交：** 完成后，请把作业提交到 Gradescope。在截止时间之前，你可以提交多次；只有最后一次提交会被评分。请确认你已经在 Gradescope 上成功提交了你的代码。关于提交作业的更多说明，请参见 [Lab 0](../../lab/lab00.html "../../lab/lab00.html")。

**使用 Ok：** 如果你对使用 Ok 有任何疑问，请参阅[这份指南。](../../articles/using-ok.html "../../articles/using-ok.html")

**阅读材料：** 你可能会觉得以下参考资料很有用：

* [Section 2.2](https://www.composingprograms.com/pages/22-data-abstraction.html "https://www.composingprograms.com/pages/22-data-abstraction.html")
* [Section 2.3](https://www.composingprograms.com/pages/23-sequences.html#trees "https://www.composingprograms.com/pages/23-sequences.html#trees")
* [Section 2.4](https://www.composingprograms.com/pages/24-mutable-data.html#sequence-objects "https://www.composingprograms.com/pages/24-mutable-data.html#sequence-objects")

**评分：** 作业根据正确性评分。每答错一道题，总分就会减少一分。**本次作业满分为 2 分。**

Required Questions
==================

Sequences
---------

### Q1: Shuffle

实现 `shuffle`，它接收一个包含偶数个 elements 的 sequence `s`（例如 list 或 range）。它返回一个新的 list，把 `s` 前半部分的 elements 与后半部分的 elements *交错* 排列。它不会修改 `s`。

把两个 sequences `s0` 和 `s1` *交错*，就是创建一个新 list，其中包含 `s0` 的第一个 element、`s1` 的第一个 element、`s0` 的第二个 element、`s1` 的第二个 element，依此类推。例如，如果 `s = [1, 2, 3, 4, 5, 6]`，那么前半部分是 `s0 = [1, 2, 3]`，后半部分是 `s1 = [4, 5, 6]`，把 `s0` 和 `s1` 交错排列会得到 `[1, 4, 2, 5, 3, 6]`。

```
def shuffle(s):
    """Return a shuffled list that interleaves the two halves of s.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    >>> shuffle(letters)
    ['a', 'e', 'b', 'f', 'c', 'g', 'd', 'h']
    >>> shuffle(shuffle(letters))
    ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
    >>> letters  # Original list should not be modified
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    assert len(s) % 2 == 0, 'len(seq) must be even'
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q shuffle

Copy

✂️
```

  

### Q2: Deep Map

**定义：** 一个 *nested list of numbers* 是指包含数字和 list 的 list。它可能只包含数字、只包含 list，或者两者混合。其中的 list 也必须是 *nested list of numbers*。例如：`[1, [2, [3]], 4]`、`[1, 2, 3]` 和 `[[1, 2], [3, 4]]` 都是 *nested list of numbers*。

写一个 function `deep_map`，它接收两个参数：一个 nested list of numbers `s` 和一个单参数 function `f`。它通过把 `s` 中的每个数字替换为对该数字调用 `f` 的结果来**就地**修改 `s`。

> **重要：** `deep_map` 返回 `None`，且不应创建任何新的 list。

> **提示：** 如果 `a` 是一个 list，`type(a) == list` 会求值为 `True`。

```
def deep_map(f, s):
    """Replace all non-list elements x with f(x) in the nested list s.

    >>> six = [1, 2, [3, [4], 5], 6]
    >>> deep_map(lambda x: x * x, six)
    >>> six
    [1, 4, [9, [16], 25], 36]
    >>> # Check that you're not making new lists
    >>> s = [3, [1, [4, [1]]]]
    >>> s1 = s[1]
    >>> s2 = s1[1]
    >>> s3 = s2[1]
    >>> deep_map(lambda x: x + 1, s)
    >>> s
    [4, [2, [5, [2]]]]
    >>> s1 is s[1]
    True
    >>> s2 is s1[1]
    True
    >>> s3 is s2[1]
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q deep_map

Copy

✂️
```

  

Data Abstraction
----------------

### Mobiles

这道题基于 Structure and Interpretation of Computer Programs 中的一道题
[Section 2.2.2](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book-Z-H-15.html#%_sec_2.2.2 "https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book-Z-H-15.html#%_sec_2.2.2")。

![Mobile example](assets/mobile-planet.png)

我们正在制作一个天文馆 mobile。一个 [mobile](https://www.northwestnatureshop.com/wp-content/uploads/2015/04/AMSolarSystem.jpg "https://www.northwestnatureshop.com/wp-content/uploads/2015/04/AMSolarSystem.jpg") 是一种悬挂式雕塑。一个 binary mobile 由两根 arms 组成。每根 arm 是一根有特定长度的杆，末端悬挂着一个 planet 或另一个 mobile。例如，下面的示意图展示了 Mobile A 的左 arm 和右 arm，以及每根 arm 末端悬挂着什么。

![Labeled Mobile example](assets/mobile-planet-labeled.png)

我们将使用下面的 data abstractions 来表示一个 binary mobile。

* 一个 `mobile` 必须同时有左 `arm` 和右 `arm`。
* 一根 `arm` 具有正的长度，且末端必须悬挂着某个东西，要么是 `mobile`，要么是 `planet`。
* 一个 `planet` 具有正的质量，且其下不悬挂任何东西。

下面是 `mobile` 和 `arm` data abstraction 的各种 constructors 和 selectors。
它们已经为你实现好了，不过这里没有展示代码。
与任何 data abstraction 一样，你应该关注 function 做什么，而不是它的具体实现。
在 Mobiles 编程练习中，你可以随意使用它们的任何 constructor 和 selector functions。

*Mobile Data Abstraction*（**仅供你参考，这里无需做任何事**）：

```
def mobile(left, right):
    """
    Construct a mobile from a left arm and a right arm.

    Arguments:
        left: An arm representing the left arm of the mobile.
        right: An arm representing the right arm of the mobile.

    Returns:
        A mobile constructed from the left and right arms.
    """
    pass

def is_mobile(m):
    """
    Return whether m is a mobile.

    Arguments:
        m: An object to be checked.

    Returns:
        True if m is a mobile, False otherwise.
    """
    pass

def left(m):
    """
    Select the left arm of a mobile.

    Arguments:
        m: A mobile.

    Returns:
        The left arm of the mobile.
    """
    pass

def right(m):
    """
    Select the right arm of a mobile.

    Arguments:
        m: A mobile.

    Returns:
        The right arm of the mobile.
    """
    pass
```

*Arm Data Abstraction*（**仅供你参考，这里无需做任何事**）：

```
def arm(length, mobile_or_planet):
    """
    Construct an arm: a length of rod with a mobile or planet at the end.

    Arguments:
        length: The length of the rod.
        mobile_or_planet: A mobile or a planet at the end of the arm.

    Returns:
        An arm constructed from the given length and mobile or planet.
    """
    pass

def is_arm(s):
    """
    Return whether s is an arm.

    Arguments:
        s: An object to be checked.

    Returns:
        True if s is an arm, False otherwise.
    """
    pass

def length(s):
    """
    Select the length of an arm.

    Arguments:
        s: An arm.

    Returns:
        The length of the arm.
    """
    pass

def end(s):
    """
    Select the mobile or planet hanging at the end of an arm.

    Arguments:
        s: An arm.

    Returns:
        The mobile or planet at the end of the arm.
    """
    pass
```

### Q3: Mass

实现 `planet` data abstraction，补全 `planet` constructor 和 `mass` selector。planet constructor 应创建并返回一个 planet。
一个 planet 应使用一个包含两个 elements 的 list 来表示，其中第一个 element 是 string `'planet'`，第二个 element 是
planet 的质量。`mass` function 应返回作为参数传入的 `planet` object 的质量。

```
def planet(mass):
    """Construct a planet of some mass."""
    assert mass > 0
    "*** YOUR CODE HERE ***"

def mass(p):
    """Select the mass of a planet."""
    assert is_planet(p), 'must call mass on a planet'
    "*** YOUR CODE HERE ***"

def is_planet(p):
    """Whether p is a planet."""
    return type(p) == list and len(p) == 2 and p[0] == 'planet'
```

`total_mass` function 演示了 mobile、arm 和 planet abstractions 的用法。
它已经为你实现好了。*你可以在后面的题目中使用 `total_mass` function。*

```
def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                             arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return t, u, v

def total_mass(m):
    """Return the total mass of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_mass(t)
    3
    >>> total_mass(u)
    6
    >>> total_mass(v)
    9
    """
    if is_planet(m):
        return mass(m)
    else:
        assert is_mobile(m), "must get total mass of a mobile or a planet"
        return total_mass(end(left(m))) + total_mass(end(right(m)))
```

运行 `total_mass` 的 `ok` 测试，确保你的 `planet` 和 `mass`
functions 实现正确。

使用 Ok 来测试你的代码：

```
python3 ok -q total_mass

Copy

✂️
```

  

### Q4: Balanced

实现 `balanced` function，它返回 `m` 是否是一个 *balanced* mobile。如果**同时**满足以下两个条件，一个 mobile 就是 *balanced* 的：

1. 它左 arm 施加的 *torque* 等于它右 arm 施加的 *torque*。一根 arm 的 *torque* 是杆的长度乘以
   悬挂在该杆上的总质量。例如，
   如果左 arm 的长度为 `5`，且左 arm 末端悬挂着一个 `mobile`，
   其总质量为 `10`，那么我们 mobile 左侧的 torque 就是 `50`。
2. 悬挂在它各 arm 末端的每个 mobile 自身也是 *balanced* 的。**提示：** 递归结构！这让你想起了什么吗？

planet 本身已经是 balanced 的，因为其下不悬挂任何东西。

> **提醒：** 你可以使用上面的 `total_mass` function。**不要违反 abstraction barriers。** 而应使用已经定义好的 selector functions。

```
def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> p = mobile(arm(3, t), arm(2, u))
    >>> balanced(p)
    False
    >>> balanced(mobile(arm(1, v), arm(1, p)))
    False
    >>> balanced(mobile(arm(1, p), arm(1, v)))
    False
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(SOURCE_FILE, 'balanced', ['Index'])
    True
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q balanced

Copy

✂️
```

  

Trees
-----

### Q5: Pruning Leaves

实现 `prune_leaves`，它接收一个 tree `t` 和一个 values 的 tuple `vals`。
它返回 `t` 的一个版本，其中所有 label 在 `vals` 中的 **leaves** 都被移除。不要移除不是 leaf 的 nodes，也不要移除不匹配 `vals` 中任何项的 leaves。如果修剪 tree 后 tree 中不再有任何 nodes，则返回 `None`。

```
def prune_leaves(t, vals):
    """Return a version of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q prune_leaves

Copy

✂️
```

  

### Q6: Maximum Path Sum

写一个 function，它接收一个由正数组成的 tree，并返回 tree 中任意一条 *root-to-leaf path* 上 labels 之和的最大值。一条
*root-to-leaf path* 是一串从 root 开始、到 tree 的某个 leaf 结束的 nodes 序列。

```
def max_path_sum(t):
    """Return the maximum root-to-leaf path sum of a tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t) # 1, 10
    11
    >>> t2 = tree(5, [tree(4, [tree(1), tree(3)]), tree(2, [tree(10), tree(3)])])
    >>> max_path_sum(t2) # 5, 2, 10
    17
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q max_path_sum

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

Exam Practice
=============

作业中还会包含一些往年的考试级题目供你参考。这些题目没有需要提交的部分；如果你想挑战一下，欢迎尝试！

1. Summer 2021 MT Q4: [Maximum Exponen-tree-ation](../../exam/su21/midterm/61a-su21-midterm.pdf#page=10 "../../exam/su21/midterm/61a-su21-midterm.pdf#page=10")
2. Summer 2019 MT Q8: [Leaf It To Me](https://inst.eecs.berkeley.edu/~cs61a/sp20/exam/su19/mt/61a-su19-mt.pdf#page=9 "https://inst.eecs.berkeley.edu/~cs61a/sp20/exam/su19/mt/61a-su19-mt.pdf#page=9")
3. Summer 2017 MT Q9: [Temmie Flakes](https://inst.eecs.berkeley.edu//~cs61a/su17/assets/pdfs/61a-su17-mt.pdf#page=11 "https://inst.eecs.berkeley.edu//~cs61a/su17/assets/pdfs/61a-su17-mt.pdf#page=11")

* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Sequences](index.html#sequences "index.html#sequences")

- [Q1: Shuffle](index.html#q1-shuffle "index.html#q1-shuffle")
- [Q2: Deep Map](index.html#q2-deep-map "index.html#q2-deep-map")

+ [Data Abstraction](index.html#data-abstraction "index.html#data-abstraction")

- [Mobiles](index.html#mobiles "index.html#mobiles")
- [Q3: Mass](index.html#q3-mass "index.html#q3-mass")
- [Q4: Balanced](index.html#q4-balanced "index.html#q4-balanced")

+ [Trees](index.html#trees "index.html#trees")

- [Q5: Pruning Leaves](index.html#q5-pruning-leaves "index.html#q5-pruning-leaves")
- [Q6: Maximum Path Sum](index.html#q6-maximum-path-sum "index.html#q6-maximum-path-sum")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Exam Practice](index.html#exam-practice "index.html#exam-practice")
