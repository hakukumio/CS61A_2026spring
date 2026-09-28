Homework 5 | CS 61A Spring 2026



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



Homework 5: Generators

* [hw05.zip](hw05.zip "hw05.zip")
=========================================================

*Due by 11:59pm on Thursday, March 12*

Instructions
------------

Download [hw05.zip](hw05.zip "hw05.zip"). Inside the archive, you will find a file called
[hw05.py](hw05.py "hw05.py"), along with a copy of the `ok` autograder.

**Submission:** When you are done, submit the assignment to Gradescope. You may submit more than once before the deadline; only the
final submission will be scored. Check that you have successfully submitted
your code on Gradescope.
See [Lab 0](../../lab/lab00.html "../../lab/lab00.html") for more instructions on submitting assignments.

**Using Ok:** If you have any questions about using Ok, please
refer to [this guide.](../../articles/using-ok.html "../../articles/using-ok.html")

**Readings:** You might find the following references
useful:

* [Section 4.2](https://www.composingprograms.com/pages/42-implicit-sequences.html "https://www.composingprograms.com/pages/42-implicit-sequences.html")

**Grading:** Homework is graded based on
correctness. Each incorrect problem will decrease the total score by one point.
**This homework is out of 2 points.**

Required Questions
==================

Generators
----------

If you need a refresher on generators, this may be helpful to read:
  

Generators (enable JavaScript)

We can create our own custom iterators by writing a *generator function*, which
returns a special type of iterator called a **generator**. Generator functions
have `yield` statements within the body of the function instead of `return`
statements. Calling a generator function will return a generator object and
will *not* execute the body of the function.

For example, let's consider the following generator function:

```
def countdown(n):
    print("Beginning countdown!")
    while n >= 0:
        yield n
        n -= 1
    print("Blastoff!")
```

Calling `countdown(k)` will return a generator object that counts down from `k`
to 0. Since generators are iterators, we can call `iter` on the resulting
object, which will simply return the same object. Note that the body is not
executed at this point; nothing is printed and no numbers are outputted.

```
>>> c = countdown(5)
>>> c
<generator object countdown ...>
>>> c is iter(c)
True
```

So how is the counting done? Again, since generators are iterators, we call
`next` on them to get the next element! The first time `next` is called,
execution begins at the first line of the function body and continues until the
`yield` statement is reached. The result of evaluating the expression in the
`yield` statement is returned. The following interactive session continues
from the one above.

```
>>> next(c)
Beginning countdown!
5
```

Unlike functions we've seen before in this course, generator functions can
remember their state. On any consecutive calls to `next`, execution picks up
from the line after the `yield` statement that was previously executed. Like
the first call to `next`, execution will continue until the next `yield`
statement is reached. Note that because of this, `Beginning countdown!` doesn't
get printed again.

```
>>> next(c)
4
>>> next(c)
3
```

The next 3 calls to `next` will continue to yield consecutive descending
integers until 0. On the following call, a `StopIteration` error will be
raised because there are no more values to yield (i.e. the end of the function
body was reached before hitting a `yield` statement).

```
>>> next(c)
2
>>> next(c)
1
>>> next(c)
0
>>> next(c)
Blastoff!
StopIteration
```

Separate calls to `countdown` will create distinct generator objects with their
own state. Usually, generators shouldn't restart. If you'd like to reset the
sequence, create another generator object by calling the generator function
again.

```
>>> c1, c2 = countdown(5), countdown(5)
>>> c1 is c2
False
>>> next(c1)
5
>>> next(c2)
5
```

Here is a summary of the above:

* A *generator function* has a `yield` statement and returns a *generator object*.
* Calling the `iter` function on a generator object returns the same object
  without modifying its current state.
* The body of a generator function is not evaluated until `next` is called on
  a resulting generator object. Calling the `next` function on a generator
  object computes and returns the next object in its sequence. If the sequence
  is exhausted, `StopIteration` is raised.
* A generator "remembers" its state for the next `next` call. Therefore,

  + the first `next` call works like this:

    1. Enter the function and run until the line with `yield`.
    2. Return the value in the `yield` statement, but remember the state of the
       function for future `next` calls.
  + And subsequent `next` calls work like this:

    1. Re-enter the function, start at **the line after the `yield` statement that
       was previously executed**, and run until the next `yield` statement.
    2. Return the value in the `yield` statement, but remember the state of the
       function for future `next` calls.
* Calling a generator function returns a brand new generator object (like
  calling `iter` on an iterable object).
* A generator should not restart unless it's defined that way. To start over
  from the first element in a generator, just call the generator function again
  to create a new generator.

Another useful tool for generators is the `yield from` statement. `yield from`
will yield all values from an iterator or iterable.

```
>>> def gen_list(lst):
...     yield from lst
...
>>> g = gen_list([1, 2, 3, 4])
>>> next(g)
1
>>> next(g)
2
>>> next(g)
3
>>> next(g)
4
>>> next(g)
StopIteration
```

### Q1: Infinite Hailstone

Write a generator function that yields the elements of the hailstone sequence starting at number `n`.
After reaching the end of the hailstone sequence, the generator should yield the number 1 indefinitely.

Here is a quick reminder of how the hailstone sequence is defined:

1. Pick a positive integer `n` as the start.
2. If `n` is even, divide it by 2.
3. If `n` is odd, multiply it by 3 and add 1.
4. Continue this process until `n` is 1.

Try to write this generator function recursively. If you are stuck, you can first try writing it iteratively
and then seeing how you can turn that implementation into a recursive one.

> **Hint:** Since `hailstone` returns a generator, you can `yield from` a call to `hailstone`!

```
def hailstone(n):
    """
    Yields the elements of the hailstone sequence starting at n.
    At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q hailstone

Copy

✂️
```

  

### Q2: Merge

**Definition:** An *infinite iterator* is an iterator that never stops providing
values when `next` is called. For example, `ones()` evaluates to an infinite
iterator:

```
def ones():
    while True:
        yield 1
```

Write a generator function `merge(a, b)` that takes two infinite iterators, `a` and `b`, as inputs. Both iterators yield elements in strictly increasing order with no duplicates. Your generator should produce all unique elements from both input iterators in increasing order, without any duplicates.

> **Note:** The input iterators do not contain duplicates within themselves, but they may have common elements between them.

```
def merge(a, b):
    """
    Return a generator that has all of the elements of infinite iterators a and b,
    in increasing order, without duplicates.

    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    a_val, b_val = next(a), next(b)
    while True:
        if a_val == b_val:
            "*** YOUR CODE HERE ***"
        elif a_val < b_val:
            "*** YOUR CODE HERE ***"
        else:
            "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q merge

Copy

✂️
```

  

### Q3: Stair Ways

Imagine that you want to go up a staircase that has `n` steps,
where `n` is a positive integer. You can take either **one** or **two steps** each time you move.

Write a generator function `stair_ways` that yields all the different ways you can climb the staircase.

Each "way" of climbing a staircase can be represented by a list of 1s and 2s, where each number indicates whether you take one step or two steps at a time.

For example, for a staircase with 3 steps, there are three ways to climb it:

* You can take one step each time: `[1, 1, 1]`.
* You can take two steps then one step: `[2, 1]`.
* You can take one step then two steps: `[1, 2].`.

Therefore, `stair_ways(3)` should yield `[1, 1, 1]`, `[2, 1]`, and `[1, 2]`. These can be yielded in any order.

> **Hint:** Think about the problem recursively. If you're on some step n, which steps could you have just been on?

```
def stair_ways(n):
    """
    Yield all the ways to climb a set of n stairs taking
    1 or 2 steps at a time.

    >>> list(stair_ways(0))
    [[]]
    >>> s_w = stair_ways(4)
    >>> sorted([next(s_w) for _ in range(5)])
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
    >>> list(s_w) # Ensure you're not yielding extra
    []
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q stair_ways

Copy

✂️
```

  

### Q4: Yield Paths

Write a generator function `yield_paths` that takes a tree `t` and a target `target`. It yields each path from the root of `t` to any node with the label `target`.

Each path should be returned as a list of labels from the root to the matching node. The paths can be yielded in any order.

> **Hint:** If you are having trouble getting started, think about how you would approach this
> problem if it was not a generator function. What would the recursive steps look like?

> **Hint:** Remember, you can iterate over generator objects because they are a type of iterator!

```
def yield_paths(t, target):
    """
    Yields all possible paths from the root of t to a node with the label
    target as a list.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(yield_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = yield_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = tree(0, [tree(2, [t1])])
    >>> print_tree(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = yield_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    if label(t) == target:
        yield ____
    for b in branches(t):
        for ____ in ____:
            yield ____
```

Use Ok to test your code:

```
python3 ok -q yield_paths

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

Exam Practice
=============

Homework assignments will also contain prior exam questions for you to try.
These questions have no submission component; feel free to attempt them if you'd like some practice!

1. Summer 2016 Final Q8: [Zhen-erators Produce Power](https://inst.eecs.berkeley.edu//~cs61a/su16/assets/pdfs/61a-su16-final.pdf#page=13 "https://inst.eecs.berkeley.edu//~cs61a/su16/assets/pdfs/61a-su16-final.pdf#page=13")
2. Spring 2018 Final Q4(a): [Apply Yourself](https://inst.eecs.berkeley.edu/~cs61a/sp18/assets/pdfs/61a-sp18-final.pdf#page=5 "https://inst.eecs.berkeley.edu/~cs61a/sp18/assets/pdfs/61a-sp18-final.pdf#page=5")

* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Generators](index.html#generators "index.html#generators")

- [Q1: Infinite Hailstone](index.html#q1-infinite-hailstone "index.html#q1-infinite-hailstone")
- [Q2: Merge](index.html#q2-merge "index.html#q2-merge")
- [Q3: Stair Ways](index.html#q3-stair-ways "index.html#q3-stair-ways")
- [Q4: Yield Paths](index.html#q4-yield-paths "index.html#q4-yield-paths")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Exam Practice](index.html#exam-practice "index.html#exam-practice")
