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

*Due by 11:59pm on Thursday, March 19*

Instructions
------------

This homework is quite long, it's in your best interest to start early.
Download [hw06.zip](hw06.zip "hw06.zip"). Inside the archive, you will find a file called
[hw06.py](hw06.py "hw06.py"), along with a copy of the `ok` autograder.

**Submission:** When you are done, submit the assignment to Gradescope. You may submit more than once before the deadline; only the
final submission will be scored. Check that you have successfully submitted
your code on Gradescope.
See [Lab 0](../../lab/lab00.html "../../lab/lab00.html") for more instructions on submitting assignments.

**Using Ok:** If you have any questions about using Ok, please
refer to [this guide.](../../articles/using-ok.html "../../articles/using-ok.html")

**Grading:** Homework is graded based on
correctness. Each incorrect problem will decrease the total score by one point.
**This homework is out of 2 points.**

Required Questions
==================

  

Midsemester Survey
------------------

### Q1: Mid-Semester Feedback

As part of this assignment, fill out the
[Mid-Semester Feedback](https://forms.gle/7SMhFR2qELXQvpqG8 "https://forms.gle/7SMhFR2qELXQvpqG8") form.

Once you finish the survey, you will be presented with a passphrase. Put
this passphrase, as a string, on the line that says
`passphrase = 'REPLACE_THIS_WITH_PASSPHRASE'` in the Python file for this assignment.
E.g. if the passphrase is `abc`, then the line should be `passphrase = 'abc'`.

Use Ok to test your code:

```
python3 ok -q midsem_survey

Copy

✂️
```

  
  

OOP
---

### Q2: Vending Machine

In this question you'll create a [vending machine](https://en.wikipedia.org/wiki/Vending_machine "https://en.wikipedia.org/wiki/Vending_machine") that sells a single product and provides change when needed.

Implement the `VendingMachine` class, which models a vending machine for one specific product.
The methods of a `VendingMachine` object return strings to describe the machine’s status and operations.
Ensure that your output matches *exactly* with the strings provided in the doctests, including punctuation and spacing.

> You may find Python's formatted string literals, or [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting "https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting") useful.
> A quick example:
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

Use Ok to test your code:

```
python3 ok -q VendingMachine

Copy

✂️
```

  

Linked Lists
------------

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

### Q3: Store Digits

Write a function `store_digits` that takes in an integer `n` and returns
a linked list containing the digits of `n` in the same order (from left to right).

> **Important**: Do not use any string manipulation functions, such as `str` or `reversed`.

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

Use Ok to test your code:

```
python3 ok -q store_digits

Copy

✂️
```

  

### Q4: Mutable Mapping

Implement `deep_map_mut(func, s)`, which applies the function `func` to each
element in the linked list `s`. If an element is itself a linked list,
recursively apply `func` to its elements as well.

Your implementation should *mutate* the original linked list. **Do not
create any new linked lists.** The function returns `None`.

> **Hint**: You can use the built-in `isinstance` function to determine if an element is a linked list.
>
> ```
> >>> s = Link(1, Link(2, Link(3, Link(4))))
> >>> isinstance(s, Link)
> True
> >>> isinstance(s, int)
> False
> ```

> **Construct Check**: The final test case for this problem checks
> that your function does not create any new linked lists.
> If you are failing this doctest, make sure that you are not
> creating link lists by calling the constructor, i.e.
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

Use Ok to test your code:

```
python3 ok -q deep_map_mut

Copy

✂️
```

  

Mutable Trees
-------------

Trees (enable JavaScript)

A `Tree` instance has two instance attributes:

* `label` is the value stored at the root of the tree.
* `branches` is a list of `Tree` instances that hold the labels in the rest of the tree.

The `Tree` class (with its `__repr__` and `__str__` methods omitted) is defined as:

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

To construct a `Tree` instance from a label `x` (any value) and a list of branches `bs` (a list of `Tree` instances) and give it the name `t`, write `t = Tree(x, bs)`.

For a tree `t`:

* Its root label can be any value, and `t.label` evaluates to it.
* Its branches are always `Tree` instances, and `t.branches` evaluates to the **list** of its branches.
* `t.is_leaf()` returns `True` if `t.branches` is empty and `False` otherwise.
* To construct a leaf with label `x`, write `Tree(x)`.

Displaying a tree `t`:

* `repr(t)` returns a Python expression that evaluates to an equivalent tree.
* `str(t)` returns one line for each label indented once more than its parent with children below their parents.

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

Changing (also known as mutating) a tree `t`:

* `t.label = y` changes the root label of `t` to `y` (any value).
* `t.branches = ns` changes the branches of `t` to `ns` (a list of `Tree` instances).
* Mutation of `t.branches` will change `t`. For example,
  `t.branches.append(Tree(y))` will add a leaf labeled `y` as the right-most
  branch.
* Mutation of any branch in `t` will change `t`. For example,
  `t.branches[0].label = y` will change the root label of the left-most branch
  to `y`.

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

Here is a summary of the differences between the tree data abstraction implemented as a functional abstraction vs. implemented as a class:

| - | Tree constructor and selector functions | Tree class |
| --- | --- | --- |
| Constructing a tree | To construct a tree given a `label` and a list of `branches`, we call `tree(label, branches)` | To construct a tree object given a `label` and a list of `branches`, we call `Tree(label, branches)` (which calls the `Tree.__init__` method). |
| Label and branches | To get the label or branches of a tree `t`, we call `label(t)` or `branches(t)` respectively | To get the label or branches of a tree `t`, we access the instance attributes `t.label` or `t.branches` respectively. |
| Mutability | The functional tree data abstraction is immutable (without violating its abstraction barrier) because we cannot assign values to call expressions | The `label` and `branches` attributes of a `Tree` instance can be reassigned, mutating the tree. |
| Checking if a tree is a leaf | To check whether a tree `t` is a leaf, we call the function `is_leaf(t)` | To check whether a tree `t` is a leaf, we call the method `t.is_leaf()`. This method can only be called on `Tree` objects. |

### Q5: Prune Small

Removing some nodes from a tree is called *pruning* the tree.

Complete the function `prune_small` that takes in a `Tree` `t` and a number `n`.
For each node with more than `n` branches, keep only the `n` branches with the
smallest labels and remove (*prune*) the rest.

> **Hint**: The `max` function takes in an `iterable` as well as an optional `key` argument (which takes in a one-argument function).
> For example, `max([-7, 2, -1], key=abs)` would return `-7` since `abs(-7)` is greater than `abs(2)` and `abs(-1)`.

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

Use Ok to test your code:

```
python3 ok -q prune_small

Copy

✂️
```

  

### Q6: Delete

Implement `delete`, which takes a Tree `t` and removes all non-root nodes labeled `x`.
The parent of each remaining node is its nearest ancestor that was not removed.
The root node is never removed, even if its label is `x`.

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

Use Ok to test your code:

```
python3 ok -q delete

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

Submit this assignment by uploading any files you've edited **to the appropriate Gradescope assignment.** [Lab 00](../../lab/lab00.html "../../lab/lab00.html") has detailed instructions.

Optional Questions
==================

### Q7: Two List

Implement a function `two_list` that takes in two lists and returns a linked list. The first list contains the
values that we want to put in the linked list, and the second list contains the number of each corresponding value.
Assume both lists are the same size and have a length of 1 or greater. Assume all elements in the second list
are greater than 0.

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

Use Ok to test your code:

```
python3 ok -q two_list

Copy

✂️
```

  

Exam Practice
=============

Homework assignments will also contain prior exam questions for you to try.
These questions have no submission component; feel free to attempt them if you'd like some practice!

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
