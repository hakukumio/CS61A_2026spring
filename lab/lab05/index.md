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

*Due by 11:59pm on Wednesday, March 4.*

Starter Files
-------------

Download [lab05.zip](lab05.zip "lab05.zip").

Attendance
==========

If you are in a regular 61A lab, your TA will come around and check you in. You need to submit the lab problems in addition to attending to get credit for lab. If you are in the mega lab, you only need to submit the lab problems to get credit.

If you miss lab for a good reason (such as sickness or a scheduling conflict) or you don't get checked in for some reason, just fill out [this form](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance") within two weeks to receive attendance credit.

Required Questions
==================

Mutability
----------

Consult the drop-down if you need a refresher on mutability. It's
okay to skip directly to the questions and refer back
here should you get stuck.

List Mutation (enable JavaScript)

Some objects in Python, such as lists and dictionaries, are **mutable**,
meaning that their contents or state can be changed.
Other objects, such as numeric types, tuples, and strings, are **immutable**,
meaning they cannot be changed once they are created.

The two most common mutation operations for lists are item assignment and the
`append` method.

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

There are many other list mutation methods:

* `append(elem)`:
  Add `elem` to the end of the list. Return `None`.
* `extend(s)`:
  Add all elements of iterable `s` to the end of the list. Return `None`.
* `insert(i, elem)`:
  Insert `elem` at index `i`. If `i` is greater than or equal to the length of
  the list, then `elem` is inserted at the end. This does not replace any
  existing elements, but only adds the new element `elem`. Return `None`.
* `remove(elem)`:
  Remove the first occurrence of `elem` in list. Return `None`.
  Errors if `elem` is not in the list.
* `pop(i)`:
  Remove and return the element at index `i`.
* `pop()`:
  Remove and return the last element.

Dictionaries also have item assignment (often used) and `pop` (rarely used).

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

> **Important:**
> For all WWPD questions, type `Function` if you believe the answer is
> `<function...>`, `Error` if it errors, and `Nothing` if nothing is displayed.

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
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

Write a function that takes in a list `s`, a value `before`, and a value
`after`. It modifies `s` in place by inserting `after` just after each
value equal to `before` in `s`. It returns `s`.

> **Important:** No new lists should be created.

> **Note:**
> If the values passed into `before` and `after` are equal, make
> sure you're not creating an infinitely long list while iterating through it.
> If you find that your code is taking more than a few seconds to run, the
> function may be in an infinite loop of inserting new values.

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

Use Ok to test your code:

```
python3 ok -q insert_items

Copy

✂️
```

  


### Q3: Group By

Write a function that takes in a list `s` and a function `fn`, and returns a dictionary that groups the elements of `s` based on the result of applying `fn`.

* The dictionary should have one key for each unique result of applying `fn` to elements of `s`.
* The value for each key should be a list of all elements in `s` that, when passed to `fn`, produce that key (what it evaluates to).

In other words, for each element `e` in `s`, determine `fn(e)` and add `e` to the list corresponding to `fn(e)` in the dictionary.

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

Use Ok to test your code:

```
python3 ok -q group_by

Copy

✂️
```

  


### Q4: Sprout Leaves

Define a function `sprout_leaves` that takes in a tree `t` and a list of
leaf labels `leaves`. It returns a new tree that is identical to `t`, but in which each
old leaf node has new branches, one for each leaf label in `leaves`.

For example, say we have the tree `t = tree(1, [tree(2), tree(3, [tree(4)])])`:

```
  1
 / \
2   3
    |
    4
```

If we call `sprout_leaves(t, [5, 6])`, the result is the following tree:

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

Use Ok to test your code:

```
python3 ok -q sprout_leaves

Copy

✂️
```

  

Iterators
---------

Consult the drop-down if you need a refresher on iterators. It's
okay to skip directly to the questions and refer back
here should you get stuck.

Iterators (enable JavaScript)

An **iterable** is any value that can be iterated through, or gone through one
element at a time. One construct that we've used to iterate through an iterable
is a for statement:

```
for elem in iterable:
    # do something
```

In general, an **iterable** is an object on which calling the built-in `iter`
function returns an *iterator*. An **iterator** is an object on which calling
the built-in `next` function returns the next value.

For example, a list is an iterable value.

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

You can also use an iterator in a `for` statement because all iterators are
iterable. But note that since iterators keep their state, they're
only good to iterate through an iterable once:

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

There are built-in functions that return iterators. These built-in Python sequence
operations are said to compute results lazily.

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

> **Important:**
> Enter `StopIteration` if a `StopIteration` exception occurs,
> `Error` if you believe a different error occurs,
> and `Iterator` if the output is an iterator object.

> **Important:** Python's built-in function `map`, `filter`, and `zip` return *iterators*, not lists.

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
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

Implement `count_occurrences`, which takes an iterator `t`, an integer `n`, and
a value `x`. It returns the number of elements in the
first `n` elements of `t` that are equal to `x`.

You can assume that `t` has at least `n` elements.

> **Important**: You should call `next` on `t` exactly `n` times. If you
> need to iterate through more than `n` elements, think about how you can
> optimize your solution.

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

Use Ok to test your code:

```
python3 ok -q count_occurrences

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

Optional Questions
==================

> These questions are optional. If you don't complete them, you will
> still receive credit for this assignment. They are great practice, so do them
> anyway!

### Q7: Path Sum

Define a function `pathsum`, which takes in a tree of numbers `t` and a number `n`. It returns `True` if there is a path from the root to a leaf such that the sum of the numbers along that path is `n` and `False` otherwise.

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

Use Ok to test your code:

```
python3 ok -q pathsum

Copy

✂️
```

  

### Q8: Perfectly Balanced

Implement `sum_tree`, which returns the sum of all the labels in tree `t`.

```
def sum_tree(t):
    """Add all elements in a tree.

    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q sum_tree

Copy

✂️
```

  

Then, implement `balanced`, which returns whether every branch of `t` has the
same total sum and that the branches themselves are also balanced.

![Example Tree](assets/just-balanced.JPG)

* For example, the tree above is balanced because each branch has the same total sum, and each branch is also itself balanced.

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

Use Ok to test your code:

```
python3 ok -q balanced

Copy

✂️
```

  
> **Challenge:**
> Solve both of these parts with just 1 line of code each.

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
