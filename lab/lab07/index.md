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

*Due by 11:59pm on Wednesday, March 18.*

Starter Files
-------------

Download [lab07.zip](lab07.zip "lab07.zip").

Attendance
==========

If you are in a regular 61A lab, your TA will come around and check you in. You need to submit the lab problems in addition to attending to get credit for lab. If you are in the mega lab, you only need to submit the lab problems to get credit.

If you miss lab for a good reason (such as sickness or a scheduling conflict) or you don't get checked in for some reason, just fill out [this form](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance") within two weeks to receive attendance credit.

Required Questions
==================

Inheritance
-----------

Consult the drop-down if you need a refresher on Inheritance. It's
okay to skip directly to the questions and refer back
here should you get stuck.

Inheritance (enable JavaScript)

To avoid redefining attributes and methods for similar classes, we can write a
single **base class** from which more specialized classes **inherit**. For
example, we can write a class called `Pet` and define `Dog` as a **subclass** of
`Pet`:

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

Inheritance represents a hierarchical relationship between two or more
classes where one class **is a** more specific version of the other:
a dog **is a** pet.
(We use "**is a**" to describe this sort of relationship in OOP languages, not to refer to the Python `is` operator.)

Since `Dog` inherits from `Pet`, the `Dog` class will also inherit the
`Pet` class's methods, so we don't have to redefine `__init__` or `eat`.
We do want each `Dog` to `talk` in a `Dog`-specific way,
so we can **override** the `talk` method.

We can use `super()` to refer to the superclass of `self`,
and access any superclass methods as if we were an instance of the superclass.
For example, `super().talk()` in the `Dog` class will call the `talk`
method from the `Pet` class, but passes in the `Dog` instance as the `self`.

### Q1: WWPD: Inheritance ABCs

> **Important:**
> For all WWPD questions, type `Function` if you believe the answer is
> `<function...>`, `Error` if it errors, and `Nothing` if nothing is displayed.
>
> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
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

Let's improve the `Account` class from lecture, which models a bank account
that can process deposits and withdrawals.

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

Add a `time_to_retire` method to the `Account` class. This method takes in an
`amount` and returns the number of years until the current `balance` grows to at
least `amount`, assuming that the bank adds the interest (calculated as the
current `balance` multiplied by the `interest` rate) to the `balance` at the end
of each year. Make sure you're not modifying the account's balance!

> **Important**: Calling the `time_to_retire` method should not change the account balance.

```
    def time_to_retire(self, amount: float) -> int:
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q Account

Copy

✂️
```

  

### Q3: FreeChecking

Implement the `FreeChecking` class, which is like the `Account` class
except that it charges a withdraw fee `withdraw_fee` after
withdrawing `free_withdrawals` number of times.
If a withdrawal is unsuccessful, no withdrawal fee will be charged, but it still counts towards the number of free
withdrawals remaining.

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

Use Ok to test your code:

```
python3 ok -q FreeChecking

Copy

✂️
```

  

Linked Lists
------------

Consult the drop-down if you need a refresher on Linked Lists. It's
okay to skip directly to the questions and refer back
here should you get stuck.

Linked Lists (enable JavaScript)

A linked list is a data structure for storing a sequence of values. It is more
efficient than a regular built-in list for certain operations, such as inserting
a value in the middle of a long list. Linked lists are not built in, and so we
define a class called `Link` to represent them.
A linked list is either a `Link` instance or `Link.empty`
(which represents an empty linked list).

A instance of `Link` has two instance attributes, `first` and `rest`.

The `rest` attribute of a `Link` instance should always be a linked list: either
another `Link` instance or `Link.empty`. It SHOULD NEVER be `None`.

To check if a linked list is empty, compare it to `Link.empty`. Since there is only
ever one empty list, we can use `is` to compare, but `==` would work too.

```
def is_empty(s):
    """Return whether linked list s is empty."""
    return s is Link.empty:
```

You can mutate a `Link` object `s` in two ways:

* Change the first element with `s.first = ...`
* Change the rest of the elements with `s.rest = ...`

You can make a new `Link` object by calling `Link`:

* `Link(4)` makes a linked list of length 1 containing 4.
* `Link(4, s)` makes a linked list that starts with 4 followed by the elements of linked list `s`.

### Visualizing Linked Lists

If you would like some support with visualizing linked lists, please navigate
to [code.cs61a.org](https://code.cs61a.org/ "https://code.cs61a.org/"), select *Start Python Interpreter*,
and call `autodraw()`.

### Q4: WWPD: Linked Lists

Read over the `Link` class. Make sure you understand the doctests.

> Use Ok to test your knowledge with the following "What Would Python Display?"
> questions:
>
> ```
> python3 ok -q link -u
> ```
>
> Enter `Function` if you believe the answer is `<function ...>`, `Error` if it
> errors, and `Nothing` if nothing is displayed.
>
> If you get stuck, try drawing out the box-and-pointer diagram for the linked
> list on a piece of paper or loading the `Link` class into the interpreter
> with `python3 -i lab07.py`.

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

Implement `without`, which takes a linked list `s` and a non-negative integer
`i`. It returns a linked list with all of the elements of `s` except for the one
at index `i`. (Assume `s.first` is the element at index 0.)

The original linked list `s` should not be changed.

> **Hint:** Using recursive approach might be easier than the iterative approach.

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

Use Ok to test your code:

```
python3 ok -q without

Copy

✂️
```

  

### Q6: Duplicate Link

Write a function `duplicate_link` that takes in a linked list `s` and a value `val`.
It **mutates** `s` so that each element equal to `val` is followed by an additional `val` (a duplicate copy).
It returns `None`. Be careful not to get into an infinite loop where you keep duplicating the new copies!

> **Note**: In order to insert a link into a linked list, reassign the `rest` attribute of the `Link` instances that have `val` as their `first`. Try drawing out a doctest to visualize!

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

Use Ok to test your code:

```
python3 ok -q duplicate_link

Copy

✂️
```

  

Check Your Score Locally
------------------------

You can locally check your score on each question of this assignment by running

```
python3 ok --score
```

**This does NOT submit the assignment!** When you are satisfied with your score, submit the assignment to Gradescope to receive credit for it.

Submit Assignment
=================

Submit this assignment by uploading any files you've edited **to the appropriate Gradescope assignment.** [Lab 00](../lab00.html#submitting-the-assignment "../lab00.html#submitting-the-assignment") has detailed instructions.

Correctly completing all questions is worth one point. If you are in the regular lab, you will need your attendance from your TA to receive that one point. Please ensure your TA has taken your attendance before leaving.

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
