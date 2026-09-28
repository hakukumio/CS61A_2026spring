Lab 1: Functions | CS 61A Spring 2026



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



Lab 1: Functions

* [lab01.zip](lab01.zip "lab01.zip")
======================================================

*Due by 11:59pm on Wednesday, January 28.*

Starter Files
-------------

Download [lab01.zip](lab01.zip "lab01.zip").

> **Lab 1 attendance:** We do not take attendance for Lab 1. Everyone will receive the attendance point automatically.

Required Questions
==================

Review
------

> **Important:** If the `python3` command doesn't work, please try using `python` or `py`.

Using Python (enable JavaScript)

Here are the most common ways to run Python on a file.

1. Using no command-line options will run the code in the file you provide and
   return you to the command line. If your file just contains function
   definitions, you'll see no output unless there is a syntax error.

   ```
   python3 lab00.py
   ```
2. **`-i`**: The `-i` option runs the code in the file you provide, then opens
   an interactive session (with a `>>>` prompt). You can then evaluate
   expressions such as calling functions you defined. To exit, type
   `exit()`. You can also use the keyboard shortcut `Ctrl-D` on Linux/Mac
   machines or `Ctrl-Z Enter` on Windows.

   If you edit the Python file while running it interactively, you will need to
   exit and restart the interpreter in order for those changes to take effect.

   Here's how we can run `lab00.py` interactively:

   ```
   python3 -i lab00.py
   ```
3. **`-m doctest`**: Runs the doctests in a file, which are the examples in
   the docstrings of functions.

   Each test in the file consists of `>>>` followed by some Python code and
   the expected output.

   Here's how we can run the doctests in `lab00.py`:

   ```
    python3 -m doctest lab00.py
   ```

   When our code passes all of the doctests, no output is displayed. Otherwise,
   information about the tests that failed will be displayed.

  


Using OK (enable JavaScript)

In CS 61A, we use a program called Ok for autograding labs, homeworks, and
projects.

To use Ok to test a function, run the following command (replacing `FUNCTION` with the name of the function):

```
python3 ok -q FUNCTION
```

If your function contains a call to `print` that starts with `"DEBUG:"`, then this line will be ignored by OK. (Otherwise, including extra `print` calls can cause tests to fail because of the additional output displayed.)

```
print("DEBUG:", x)
```

There are more features described on the [Using OK page](../../articles/using-ok.html "../../articles/using-ok.html").
**You can quickly generate most ok commands at [ok-help](https://go.cs61a.org/ok-help "https://go.cs61a.org/ok-help").**

  

Division, Floor Div, and Modulo (enable JavaScript)

Here are examples of the division-related operators in Python 3:
  
  

| True Division: `/`   (decimal division) | Floor Division: `//`   (integer division) | Modulo: `%`   (remainder) |
| --- | --- | --- |
| ``` >>> 1 / 5 0.2  >>> 25 / 4 6.25  >>> 4 / 2 2.0  >>> 5 / 0 ZeroDivisionError ``` | ``` >>> 1 // 5 # truncate result of true division 0  >>> 25 // 4 6  >>> 4 // 2 2  >>> 5 // 0 ZeroDivisionError ``` | ``` >>> 1 % 5 1  >>> 25 % 4 1  >>> 4 % 2 0  >>> 5 % 0 ZeroDivisionError ``` |

A `ZeroDivisionError` occurs when dividing by 0.

One useful technique involving the `%` operator is to check
whether a number `x` is divisible by another number `y`:

```
x % y == 0
```

For example, in order to check if `x` is an even number: `x % 2 == 0`

  

Return and Print (enable JavaScript)

Most functions that you define will contain a `return` statement that provides
the value of the call expression used to call the function.

When Python executes a `return` statement, the function call terminates
immediately. If Python reaches the end of the function body without executing
a `return` statement, the function returns `None`.

In contrast, the `print` function is used to display values.
Unlike a `return` statement, when Python evaluates a call to `print`, the
function does *not* terminate immediately.

```
def what_prints():
    print('Hello World!')
    return 'Exiting this function.'
    print('This course is awesome!')

>>> what_prints()
Hello World!
'Exiting this function.'
```

> Notice also that `print` will display text **without the quotes**, but
> `return` will preserve the quotes.

What Would Python Display? (WWPD)
---------------------------------

### Q1: Return and Print

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
>
> ```
> python3 ok -q return-and-print -u
>
> Copy
>
> ✂️
> ```

```
>>> def welcome():
...     print('Go')
...     return 'hello'
...
>>> def cal():
...     print('Bears')
...     return 'world'
...
>>> welcome()

______



Go
'hello'

>>> print(welcome(), cal())

______



Go
Bears
hello world
```

Toggle Solution (enable JavaScript)

Write Code
----------

### Q2: Debugging Quiz

The following is a quick quiz on different debugging techniques that will be
helpful for you to use in this class. You can refer to the
[debugging article](../../articles/debugging/index.html "../../articles/debugging/index.html") to answer the questions.

Use Ok to test your understanding:

```
python3 ok -q debugging-quiz -u

Copy

✂️
```

  

### Q3: Pick a Digit

Implement `digit`, which takes positive integers `n` and `k` and has only a
single return statement as its body. It returns the digit of `n` that is `k`
positions to the left of the rightmost digit (the one's digit). If `k` is 0,
return the rightmost digit. If there is no digit of `n` that is `k` positions to
the left of the rightmost digit, return 0.

**Hint:** Use `//` and `%` and the built-in `pow` function to isolate a
particular digit of `n`.

```
def digit(n, k):
    """Return the k-th digit from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    return ____
```

Use Ok to test your code:

```
python3 ok -q digit

Copy

✂️
```

  

### Q4: Middle Number

Implement `middle` by writing a single return expression that evaluates to the
value that is neither the largest or smallest among three different integers
`a`, `b`, and `c`.

> **Hint:** Try combining all the numbers and then taking away the ones you don't
> want to return by using the built-in `min` and `max` functions.
>
> ```
> >>> max(1, 2, 3)
> 3
> >>> min(-1, -2, -3)
> -3
> ```

```
def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    return ____
```

Use Ok to test your code:

```
python3 ok -q middle

Copy

✂️
```

  

Syllabus Quiz
-------------

### Q5: Syllabus Quiz

Please fill out the [Syllabus Quiz](https://go.cs61a.org/syllabus-quiz "https://go.cs61a.org/syllabus-quiz"), which confirms your understanding of the policies on the syllabus page.

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

> **Lab 1 attendance:** We do not take attendance for Lab 1. Everyone will receive the attendance point automatically.

Optional Questions
==================

> These questions are optional. If you don't complete them, you will
> still receive credit for this assignment. They are great practice, so do them
> anyway!

**You really should work on these today!** They are marked as optional only because some students just joined the course and are getting caught up, but students who have already attended the first three lectures should be well prepared to solve these, and Homework 1 will be much smoother with the experience of solving these.

### Q6: WWPD: What If?

> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
>
> ```
> python3 ok -q if-statements -u
>
> Copy
>
> ✂️
> ```
>
>   
>
> **Hint**: `print` (unlike `return`) does *not* cause the function to exit.

```
>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)

______



10
foo
```

Toggle Solution (enable JavaScript)

```
>>> def bake(cake, make):
...     if cake == 0:
...         cake = cake + 1
...         print(cake)
...     if cake == 1:
...         print(make)
...     else:
...         return cake
...     return make
>>> bake(0, 29)

______



1
29
29

>>> bake(1, "mashed potatoes")

______



mashed potatoes
'mashed potatoes'
```

Toggle Solution (enable JavaScript)

### Q7: Falling Factorial

Let's write a function `falling`, which is a "falling" factorial
that takes two arguments, `n` and `k`, and returns the product of `k`
consecutive numbers, starting from `n` and working downwards.
When `k` is 0, the function should return 1.

```
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q falling

Copy

✂️
```

  

### Q8: Divisible By k

Write a function `divisible_by_k` that takes positive integers `n` and `k`. It prints all positive integers less than or equal to `n` that are divisible by `k` from smallest to largest. Then, it returns how many numbers were printed.

```
def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 that are divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q divisible_by_k

Copy

✂️
```

  

### Q9: Sum Digits

Write a function that takes in a nonnegative integer and sums its digits. (Using
floor division and modulo might be helpful here!)

```
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q sum_digits

Copy

✂️
```

  

### Q10: Double Eights

Write a function that takes in a number and determines if the digits contain two
adjacent 8s.

```
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q double_eights

Copy

✂️
```

* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Review](index.html#review "index.html#review")
+ [What Would Python Display? (WWPD)](index.html#what-would-python-display-wwpd "index.html#what-would-python-display-wwpd")

- [Q1: Return and Print](index.html#q1-return-and-print "index.html#q1-return-and-print")

+ [Write Code](index.html#write-code "index.html#write-code")

- [Q2: Debugging Quiz](index.html#q2-debugging-quiz "index.html#q2-debugging-quiz")
- [Q3: Pick a Digit](index.html#q3-pick-a-digit "index.html#q3-pick-a-digit")
- [Q4: Middle Number](index.html#q4-middle-number "index.html#q4-middle-number")

+ [Syllabus Quiz](index.html#syllabus-quiz "index.html#syllabus-quiz")

- [Q5: Syllabus Quiz](index.html#q5-syllabus-quiz "index.html#q5-syllabus-quiz")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Optional Questions](index.html#optional-questions "index.html#optional-questions")

+ [Q6: WWPD: What If?](index.html#q6-wwpd-what-if "index.html#q6-wwpd-what-if")
+ [Q7: Falling Factorial](index.html#q7-falling-factorial "index.html#q7-falling-factorial")
+ [Q8: Divisible By k](index.html#q8-divisible-by-k "index.html#q8-divisible-by-k")
+ [Q9: Sum Digits](index.html#q9-sum-digits "index.html#q9-sum-digits")
+ [Q10: Double Eights](index.html#q10-double-eights "index.html#q10-double-eights")
