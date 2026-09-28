Homework 2 | CS 61A Spring 2026



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



Homework 2: Higher-Order Functions

* [hw02.zip](hw02.zip "hw02.zip")
=====================================================================

*Due by 11:59pm on Thursday, February 5*

Instructions
------------

Download [hw02.zip](hw02.zip "hw02.zip"). Inside the archive, you will find
a file called [hw02.py](hw02.py "hw02.py"), along with a copy of the `ok`
autograder.

**Submission:** When you are done, submit the assignment to Gradescope. You may submit more than once before the deadline; only the
final submission will be scored. Check that you have successfully submitted
your code on Gradescope.
See [Lab 0](../../lab/lab00.html "../../lab/lab00.html") for more instructions on submitting assignments.

**Using Ok:** If you have any questions about using Ok, please
refer to [this guide.](../../articles/using-ok.html "../../articles/using-ok.html")

**Readings:** You might find the following references
useful:

* [Section 1.6](https://www.composingprograms.com/pages/16-higher-order-functions.html "https://www.composingprograms.com/pages/16-higher-order-functions.html")

**Grading:** Homework is graded based on
correctness. Each incorrect problem will decrease the total score by one point.
**This homework is out of 2 points.**

Required Questions
==================

Several doctests refer to these functions:

```
from operator import add, mul

def square(x):
    return x * x

def identity(x):
    return x

def triple(x):
    return 3 * x

def increment(x):
    return x + 1
```

A previous version of this assignment included versions of these functions
written with lambda expressions, which were slated to be covered in
[Monday's lecture videos](https://www.youtube.com/watch?v=vCeNq_P3akI&list=PL6BsET-8jgYXTuSlJNYQS740YMCRHT79g&index=5 "https://www.youtube.com/watch?v=vCeNq_P3akI&list=PL6BsET-8jgYXTuSlJNYQS740YMCRHT79g&index=5"). If you downloaded the old
version of this assignment, you can pretend that `square`, `identity`, `triple`,
and `increment` are defined as above. The code you need to write will be
the same either way, and submitting an old version of the assignment will
not affect your autograder score.

  

Higher-Order Functions
----------------------

### Q1: Product

Write a function called `product` that returns the product of the first `n` terms of a sequence.
Specifically, `product` takes in an integer `n` and `term`, a single-argument function that determines a sequence
(That is, `term(i)` gives the `i`th term of the sequence).
`product(n, term)` should return `term(1) * ... * term(n)`.

```
def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term: a function that takes an index as input and produces a term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q product

Copy

✂️
```

  

### Q2: Accumulate

Let's take a look at how `product` is an instance of a more
general function called `accumulate`, which we would like to implement:

```
def accumulate(fuse, start, n, term):
    """Return the result of fusing together the first n terms in a sequence 
    and start.  The terms to be fused are term(1), term(2), ..., term(n). 
    The function fuse is a two-argument commutative & associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11 (fuse is never used)
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    """
    "*** YOUR CODE HERE ***"
```

`accumulate` has the following parameters:

* `fuse`: a two-argument function that specifies how the current term
  is fused with the previously accumulated terms
* `start`: value at which to start the accumulation
* `n`: a non-negative integer indicating the number of terms to fuse
* `term`: a single-argument function; `term(i)` is the `i`th term of the sequence

Implement `accumulate`, which fuses the first `n` terms of the sequence defined
by `term` with the `start` value using the `fuse` function.

For example, the result of `accumulate(add, 11, 3, square)` is

```
add(11,  add(square(1), add(square(2),  square(3)))) =
    11 +     square(1) +    square(2) + square(3)    =
    11 +     1         +    4         + 9            = 25
```

> Assume that `fuse` is commutative, `fuse(a, b) == fuse(b, a)`, and
> associative, `fuse(fuse(a, b), c) == fuse(a, fuse(b, c))`.

Use Ok to test your code:

```
python3 ok -q accumulate

Copy

✂️
```

  

Then, implement `summation` (from lecture) and `product` as one-line calls to
`accumulate`.

> **Important:** Both `summation_using_accumulate` and `product_using_accumulate`
> should be implemented with a single line of code starting with `return`.

```
def summation_using_accumulate(n, term):
    """Returns the sum: term(1) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square) # square(1) + square(2) + ... + square(4) + square(5)
    55
    >>> summation_using_accumulate(5, triple) # triple(1) + triple(2) + ... + triple(4) + triple(5)
    45
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return ____

def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square) # square(1) * square(2) * square(3) * square()
    576
    >>> product_using_accumulate(6, triple) # triple(1) * triple(2) * ... * triple(5) * triple(6)
    524880
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return ____
```

Use Ok to test your code:

```
python3 ok -q summation_using_accumulate
python3 ok -q product_using_accumulate

Copy

✂️
```

  



### Q3: Make Repeater

Implement the function `make_repeater` which takes a one-argument function `f`
and a positive integer `n`. It returns a one-argument function so that
`make_repeater(f, n)(x)` returns the value of `f(f(...f(x)...))`, in which `f` is
applied `n` times to `x`. For example, `make_repeater(square, 3)(5)` squares 5
three times and returns 390625, just like `square(square(square(5)))`.

```
def make_repeater(f, n):
    """Returns the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * (3 * (3 * (3 * (3 * 1))))
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q make_repeater

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

[Optional] Exam Practice
------------------------

Here are some related questions from past exams for you to try. These are optional.
There is no way to submit them.

1. Fall 2019 MT1 Q3: [You Again](../../exam/fa19/mt1/61a-fa19-mt1.pdf#page=4 "../../exam/fa19/mt1/61a-fa19-mt1.pdf#page=4") [Higher-Order Functions]
2. Fall 2021 MT1 Q1b: [tik](../../exam/fa21/mt1/61a-fa21-mt1.pdf#page=4 "../../exam/fa21/mt1/61a-fa21-mt1.pdf#page=4") [Functions and Expressions]

* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Higher-Order Functions](index.html#higher-order-functions "index.html#higher-order-functions")

- [Q1: Product](index.html#q1-product "index.html#q1-product")
- [Q2: Accumulate](index.html#q2-accumulate "index.html#q2-accumulate")
- [Q3: Make Repeater](index.html#q3-make-repeater "index.html#q3-make-repeater")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")

+ [[Optional] Exam Practice](index.html#optional-exam-practice "index.html#optional-exam-practice")
