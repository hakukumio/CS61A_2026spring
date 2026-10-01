Lab 7: Inheritance, Linked Lists | CS 61A Spring 2026



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



Lab 7: Inheritance, Linked Lists

* [lab07.zip](lab07.zip "lab07.zip")
======================================================================

*截止时间为 3 月 18 日（周三）晚上 11:59。*

Starter Files
-------------

下载 [lab07.zip](lab07.zip "lab07.zip")。

Attendance
==========

如果你参加的是常规 61A lab，你的 TA 会过来为你 check in。你除了到场之外，还需要提交 lab problems，才能获得本次 lab 的学分。如果你参加的是 mega lab，那么只需提交 lab problems 即可获得学分。

如果你因为正当理由（例如生病或时间冲突）缺席 lab，或者因为某些原因没有被 check in，只需在两周内填写[此表单](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance")即可获得 attendance 学分。

Required Questions
==================

Inheritance
-----------

如果你需要复习 Inheritance，请查阅下拉框。你也可以直接跳到题目部分，遇到困难时再回到这里查阅。

Inheritance (enable JavaScript)

为了避免为相似的 classes 重复定义 attributes 和 methods，我们可以编写一个单一的 **base class**，让更专门的 classes **inherit** 它。例如，我们可以编写一个名为 `Pet` 的 class，并把 `Dog` 定义为 `Pet` 的 **subclass**：

```
class Pet:

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
        super().talk()
        print('This Dog says woof!')
```

Inheritance 表示两个或多个 classes 之间的层级关系，其中一个 class **is a** 另一个 class 更具体的版本：a dog **is a** pet。（我们用 "**is a**" 来描述 OOP 语言中的这种关系，而不是指 Python 的 `is` 运算符。）

由于 `Dog` 继承自 `Pet`，`Dog` class 也会继承 `Pet` class 的 methods，所以我们不必重新定义 `__init__` 或 `eat`。我们希望每个 `Dog` 以 `Dog` 特有的方式 `talk`，所以我们可以 **override** 这个 `talk` method。

我们可以用 `super()` 来引用 `self` 的 superclass，并像 superclass 的实例一样访问任何 superclass methods。例如，`Dog` class 中的 `super().talk()` 会调用 `Pet` class 的 `talk` method，但会把 `Dog` 实例作为 `self` 传入。

### Q1: WWPD: Inheritance ABCs

> **重要：**
> 对于所有 WWPD 题目，如果你认为答案是
> `<function...>`，请输入 `Function`；如果会报错，请输入 `Error`；如果没有显示任何内容，请输入 `Nothing`。
>
> 使用 Ok 来通过以下 "What Would Python Display?" 题目检验你的理解：
>
> ```
> python3 ok -q inheritance-abc -u
>
> Copy
>
> ✂️
> ```

```
>>> class A:
...   x, y = 0, 0
...   def __init__(self):
...         return
>>> class B(A):
...   def __init__(self):
...         return
>>> class C(A):
...   def __init__(self):
...         return
>>> print(A.x, B.x, C.x)

______



0 0 0

>>> B.x = 2
>>> print(A.x, B.x, C.x)

______



0 2 0

>>> A.x += 1
>>> print(A.x, B.x, C.x)

______



1 2 1

>>> obj = C()
>>> obj.y = 1
>>> C.y == obj.y

______



False

>>> A.y = obj.y
>>> print(A.y, B.y, C.y, obj.y)

______



1 1 1 1
```

Toggle Solution (enable JavaScript)

Class Practice
--------------

### Checking Accounts

让我们改进 lecture 中的 `Account` class，它模拟了一个可以处理存款和取款的银行账户。

```
class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> a.time_to_retire(10.25)  # 10 -> 10.2 -> 10.404
    2
    >>> a.balance                # Calling time_to_retire method should not change the balance
    10
    >>> a.time_to_retire(11)     # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """
    max_withdrawal: int = 10
    interest: float = 0.02

    def __init__(self, account_holder: str):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount: int) -> int:
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount: int) -> int | str:
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance
```

### Q2: Retirement

给 `Account` class 添加一个 `time_to_retire` method。这个 method 接收一个 `amount`，返回当前 `balance` 增长到至少 `amount` 所需的年数，假设银行在每年年末把利息（按当前 `balance` 乘以 `interest` 利率计算）加到 `balance` 上。请确保你没有修改账户的 balance！

> **重要**：调用 `time_to_retire` method 不应改变账户的 balance。

```
    def time_to_retire(self, amount: float) -> int:
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q Account

Copy

✂️
```

  

### Q3: FreeChecking

实现 `FreeChecking` class，它类似于 `Account` class，不同之处在于它在取款 `free_withdrawals` 次之后会收取取款费 `withdraw_fee`。如果一次取款不成功，不会收取取款费，但它仍然计入剩余的免费取款次数。

```
class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!

    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free. Still counts as a free withdrawal even though it was unsuccessful
    'Insufficient funds'
    >>> ch.withdraw(3)    # Second withdrawal is also free
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Now there is a fee because free_withdrawals is only 2
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee: int = 1
    free_withdrawals: int = 2

    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q FreeChecking

Copy

✂️
```

  

Linked Lists
------------

如果你需要复习 Linked Lists，请查阅下拉框。你也可以直接跳到题目部分，遇到困难时再回到这里查阅。

Linked Lists (enable JavaScript)

A linked list 是一种用于存储 values 的 sequence 的数据结构。对于某些操作（例如在很长的 list 中间插入一个 value），它比常规的内置 list 更高效。linked lists 不是内置的，所以我们定义了一个名为 `Link` 的 class 来表示它们。一个 linked list 要么是一个 `Link` 实例，要么是 `Link.empty`（表示空的 linked list）。

一个 `Link` 实例有两个 instance attributes，`first` 和 `rest`。

一个 `Link` 实例的 `rest` attribute 应始终是一个 linked list：要么是另一个 `Link` 实例，要么是 `Link.empty`。它绝不应该为 `None`。

要检查一个 linked list 是否为空，把它与 `Link.empty` 比较。由于空 list 永远只有一个，我们可以用 `is` 来比较，但 `==` 也可以。

```
def is_empty(s):
    """Return whether linked list s is empty."""
    return s is Link.empty:
```

你可以通过两种方式修改（mutate）一个 `Link` object `s`：

* 用 `s.first = ...` 改变第一个 element
* 用 `s.rest = ...` 改变其余 elements

你可以通过调用 `Link` 来创建一个新的 `Link` object：

* `Link(4)` 创建一个长度为 1、包含 4 的 linked list。
* `Link(4, s)` 创建一个以 4 开头、后接 linked list `s` 的 elements 的 linked list。

### Visualizing Linked Lists

如果你在可视化 linked lists 方面需要一些帮助，请访问 [code.cs61a.org](https://code.cs61a.org/ "https://code.cs61a.org/")，选择 *Start Python Interpreter*，然后调用 `autodraw()`。

### Q4: WWPD: Linked Lists

读一遍 `Link` class。确保你理解这些 doctests。

> 使用 Ok 来通过以下 "What Would Python Display?" 题目检验你的理解：
>
> ```
> python3 ok -q link -u
> ```
>
> 如果你认为答案是 `<function ...>`，请输入 `Function`；如果会报错，请输入 `Error`；如果没有显示任何内容，请输入 `Nothing`。
>
> 如果你卡住了，试着在纸上画出这个 linked list 的 box-and-pointer diagram，或者用 `python3 -i lab07.py` 把 `Link` class 加载到解释器中。

```
>>> link = Link(1000)
>>> link.first

______



1000

>>> link.rest is Link.empty

______



True

>>> link = Link(1000, 2000)

______



AssertionError

>>> link = Link(1000, Link())

______



TypeError
```

Toggle Solution (enable JavaScript)

```
>>> link = Link(1, Link(2, Link(3)))
>>> link.first

______



1

>>> link.rest.first

______



2

>>> link.rest.rest.rest is Link.empty

______



True

>>> link.first = 9001
>>> link.first

______



9001

>>> link.rest = link.rest.rest
>>> link.rest.first

______



3

>>> link = Link(1)
>>> link.rest = link
>>> link.rest.rest is Link.empty

______



False

>>> link.rest.rest.rest.rest.first

______



1

>>> link = Link(2, Link(3, Link(4)))
>>> link2 = Link(1, link)
>>> link2.first

______



1

>>> link2.rest.first

______



2
```

Toggle Solution (enable JavaScript)

```
>>> link = Link(5, Link(6, Link(7)))
>>> link                 # Look at the __repr__ method of Link

______



Link(5, Link(6, Link(7)))

>>> print(link)          # Look at the __str__ method of Link

______



(5 6 7)
```

Toggle Solution (enable JavaScript)

### Q5: Without One

实现 `without`，它接收一个 linked list `s` 和一个非负整数 `i`。它返回一个 linked list，其中包含 `s` 的所有 elements，只是不包含 index `i` 处的那个。（假设 `s.first` 是 index 0 处的 element。）

原始的 linked list `s` 不应被改变。

> **提示**：使用递归方法可能比迭代方法更容易。

```
def without(s: Link, i: int) -> Link:
    """Return a new linked list like s but without the element at index i.

    >>> s = Link(3, Link(5, Link(7, Link(9))))
    >>> without(s, 0)
    Link(5, Link(7, Link(9)))
    >>> without(s, 2)
    Link(3, Link(5, Link(9)))
    >>> without(s, 4)  # There is no index 4, so all of s is retained.
    Link(3, Link(5, Link(7, Link(9))))
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q without

Copy

✂️
```

  

### Q6: Duplicate Link

编写一个 function `duplicate_link`，它接收一个 linked list `s` 和一个 value `val`。它**修改**（mutates）`s`，使得每个等于 `val` 的 element 后面都跟着一个额外的 `val`（一份重复的副本）。它返回 `None`。注意不要陷入不断复制新副本的无限循环！

> **注意**：为了把一个 link 插入 linked list，重新赋值那些以 `val` 为 `first` 的 `Link` 实例的 `rest` attribute。试着画出一个 doctest 来可视化！

```
def duplicate_link(s: Link, val: int) -> None:
    """Mutates s so that each element equal to val is followed by another val.

    >>> x = Link(5, Link(4, Link(5)))
    >>> duplicate_link(x, 5)
    >>> x
    Link(5, Link(5, Link(4, Link(5, Link(5)))))
    >>> y = Link(2, Link(4, Link(6, Link(8))))
    >>> duplicate_link(y, 10)
    >>> y
    Link(2, Link(4, Link(6, Link(8))))
    >>> z = Link(1, Link(2, Link(2, Link(3))))
    >>> duplicate_link(z, 2) # ensures that back to back links with val are both duplicated
    >>> z
    Link(1, Link(2, Link(2, Link(2, Link(2, Link(3))))))
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q duplicate_link

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

* [Attendance](index.html#attendance "index.html#attendance")
* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Inheritance](index.html#inheritance "index.html#inheritance")

- [Q1: WWPD: Inheritance ABCs](index.html#q1-wwpd-inheritance-abcs "index.html#q1-wwpd-inheritance-abcs")

+ [Class Practice](index.html#class-practice "index.html#class-practice")

- [Checking Accounts](index.html#checking-accounts "index.html#checking-accounts")
- [Q2: Retirement](index.html#q2-retirement "index.html#q2-retirement")
- [Q3: FreeChecking](index.html#q3-freechecking "index.html#q3-freechecking")

+ [Linked Lists](index.html#linked-lists "index.html#linked-lists")

- [Visualizing Linked Lists](index.html#visualizing-linked-lists "index.html#visualizing-linked-lists")
- [Q4: WWPD: Linked Lists](index.html#q4-wwpd-linked-lists "index.html#q4-wwpd-linked-lists")
- [Q5: Without One](index.html#q5-without-one "index.html#q5-without-one")
- [Q6: Duplicate Link](index.html#q6-duplicate-link "index.html#q6-duplicate-link")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
