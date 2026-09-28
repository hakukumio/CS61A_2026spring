Lab 3: Recursion, Python Lists | CS 61A Spring 2026



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



Lab 3: Recursion, Python Lists

* [lab03.zip](lab03.zip "lab03.zip")
====================================================================

*Due by 11:59pm on Wednesday, February 18.*

Starter Files
-------------

Download [lab03.zip](lab03.zip "lab03.zip").

Attendance
==========

If you are in a regular 61A lab, your TA will come around and check you in. You need to submit the lab problems in addition to attending to get credit for lab. If you are in the mega lab, you only need to submit the lab problems to get credit.

If you miss lab for a good reason (such as sickness or a scheduling conflict) or you don't get checked in for some reason, just fill out [this form](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance") within two weeks to receive attendance credit.

Topics
======

Consult this section if you need a refresher on the material for this lab. It's
okay to skip directly to [the questions](index.html#required-questions "index.html#required-questions") and refer back
here should you get stuck.

Lists (enable JavaScript)

Lists
-----

A list is a data structure that can hold an ordered collection of items.
These items, known as elements, can be of any data type, including numbers, strings, or even other lists.
A comma-separated list of expressions in square brackets creates a list:

```
>>> list_of_values = [2, 1, 3, True, 3]
>>> nested_list = [2, [1, 3], [True, [3]]]
```

Each position in a list has an index, with the left-most element indexed `0`.

```
>>> list_of_values[0]
2
>>> nested_list[1]
[1, 3]
```

A negative index counts from the end, with the right-most element indexed `-1`.

```
>>> nested_list[-1]
[True, [3]]
```

Adding lists creates a longer list containing the elements of the added lists.

```
>>> [1, 2] + [3] + [4, 5]
[1, 2, 3, 4, 5]
```

List Comprehensions (enable JavaScript)

List Comprehensions
-------------------

A list comprehension describes the elements in a list and evaluates to a new list
containing those elements.

There are two forms:

```
[<expression> for <element> in <sequence>]
[<expression> for <element> in <sequence> if <conditional>]
```

Here's an example that starts with `[1, 2, 3, 4]`, picks out the even elements
`2` and `4` using `if i % 2 == 0`, then squares each of these using `i*i`. The
purpose of `for i` is to give a name to each element in `[1, 2, 3, 4]`.

```
>>> [i*i for i in [1, 2, 3, 4] if i % 2 == 0]
[4, 16]
```

This list comprehension evaluates to a list of:

* The value of `i*i`
* For each element `i` in the sequence `[1, 2, 3, 4]`
* For which `i % 2 == 0`

In other words, this list comprehension will create a new list that contains
the square of every even element of the original list `[1, 2, 3, 4]`.

We can also rewrite a list comprehension as an equivalent `for` statement,
such as for the example above:

```
>>> result = []
>>> for i in [1, 2, 3, 4]:
...     if i % 2 == 0:
...         result = result + [i*i]
>>> result
[4, 16]
```

For Loops (enable JavaScript)

`for` Statements
----------------

A `for` statement executes code for each element of a sequence, such as a list or range. Each time the code is executed, the name right after `for` is bound to a different element of the sequence.

```
for <name> in <expression>:
    <suite>
```

First, `<expression>` is evaluated. It must evaluate to a sequence. Then, for each element in the sequence in order,

1. `<name>` is bound to the element.
2. `<suite>` is executed.

Here is an example:

```
for x in [-1, 4, 2, 0, 5]:
    print("Current elem:", x)
```

This would display the following:

```
Current elem: -1
Current elem: 4
Current elem: 2
Current elem: 0
Current elem: 5
```

Ranges (enable JavaScript)

Ranges
------

A range is a data structure that holds integer sequences. A range can be created by:

* `range(stop)` contains 0, 1, ..., `stop` - 1
* `range(start, stop)` contains `start`, `start` + 1, ..., `stop` - 1

Notice how the range function doesn't include the `stop` value; it generates numbers up to, but not including, the `stop` value.

For example:

```
>>> for i in range(3):
...     print(i)
...
0
1
2
```

While ranges and lists are both [sequences](https://en.wikibooks.org/wiki/Python_Programming/Sequences "https://en.wikibooks.org/wiki/Python_Programming/Sequences"), a range object is different from a list. A range can be converted to a list by calling `list()`:

```
>>> range(3, 6)
range(3, 6)  # this is a range object
>>> list(range(3, 6))
[3, 4, 5]  # list() converts the range object to a list
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(1, 6))
[1, 2, 3, 4, 5]
```

  

Type Checking
=============

Type hints can appear in `assignment` and `def` statements (and a few other
places) to indicate the types of value that a variable should have or that
functions should return.

An example without type hints:

```
x = 4

def pair(y, z):
    return [y, z]
```

The same example with type hints that `x`, `y`, and `z` are integers and the
`pair` function returns a list of integers:

```
x: int = 4

def pair(y: int, z: int) -> list[int]:
    return [y, z]
```

Code behaves identically with or without type hints. You can read more in the
[type hints](../../articles/type-hints.html "../../articles/type-hints.html") article.

**Automatic Type Checking**: VS Code can be configured to annotate locations
where a variable has been assigned a value that does not have the expected type.
To enable type checking, open the VS Code settings, which you can do by pressing
the Command and `,` keys on a Mac, or the Control and `,` keys simultaneously on
a Windows machine. Type `type checking` in the search bar, which should pull up
the Type Checking options shown in the screenshot below. Use the dropdown menu
to change type checking from the default of `off` to `basic`.

![type-hints](assets/type_hints_vscode.png)

If these type checking options did not appear, you may need to install the Pylance
extension. Open the Extensions view by holding Shift, Command, and `X` on a Mac
or Shift, Control, and `X` on Windows. Type `Pylance` in the search bar, and
press the install button.

To check to ensure that type checking has been enabled, type the following into
a Python file:

```
a: int = 'not an int'
```

You should see a red underline under `'not an int'`. If you hover over `'not an int'`,
VS Code displays an error message, explaining that `'not an int'` does not match
the expected type `int`. Keep an eye out for these errors while you're writing code!
They're usually a hint about where your code has a bug.

Required Questions
==================

Lists
-----

> **Important:**
> For all WWPD questions, type `Function` if you believe the answer is
> `<function...>`, `Error` if it errors, and `Nothing` if nothing is displayed.
>
> ### Q1: WWPD: Lists & Ranges
>
> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
>
> ```
> python3 ok -q lists-wwpd -u
>
> Copy
>
> ✂️
> ```

Predict what Python will display when you type the following into the
interactive interpreter. Then try it to check your answers.

```
>>> s = [7//3, 5, [4, 0, 1], 2]
>>> s[0]

______



2

>>> s[2]

______



[4, 0, 1]

>>> s[-1]

______



2

>>> len(s)

______



4

>>> 4 in s

______



False

>>> 4 in s[2]

______



True

>>> s[2] + [3 + 2]

______



[4, 0, 1, 5]

>>> 5 in s[2]

______



False

>>> s[2] * 2

______



[4, 0, 1, 4, 0, 1]

>>> list(range(3, 6))

______



[3, 4, 5]

>>> range(3, 6)

______



range(3, 6)

>>> r = range(3, 6)
>>> [r[0], r[2]]

______



[3, 5]

>>> range(4)[-1]

______



3
```

Toggle Solution (enable JavaScript)

### Q2: Close

Implement `close`, which takes a list of integers `s` and a non-negative integer `k`. It returns how many of the elements of `s` are within `k` of their index. That is, the absolute value of the difference between the element and its index is less than or equal to `k`.

> Remember that list is "zero-indexed"; the index of the first element is `0`.

```
def close(s: list[int], k: int) -> int:
    """Return how many elements of s are within k of their index.

    >>> t = [6, 2, 4, 3, 5]
    >>> close(t, 0)  # Only 3 is equal to its index
    1
    >>> close(t, 1)  # 2, 3, and 5 are within 1 of their index
    3
    >>> close(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    4
    >>> close(list(range(10)), 0)
    10
    """
    assert k >= 0
    count = 0
    for i in range(len(s)):  # Use a range to loop over indices
        "*** YOUR CODE HERE ***"
    return count
```

Use Ok to test your code:

```
python3 ok -q close

Copy

✂️
```

  

List Comprehensions
-------------------

> **Important:**
> For all WWPD questions, type `Function` if you believe the answer is
> `<function...>`, `Error` if it errors, and `Nothing` if nothing is displayed.
>
> ### Q3: WWPD: List Comprehensions
>
> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
>
> ```
> python3 ok -q list-comprehensions-wwpd -u
>
> Copy
>
> ✂️
> ```

Predict what Python will display when you type the following into the
interactive interpreter. Then try it to check your answers.

```
>>> [2 * x for x in range(4)]

______



[0, 2, 4, 6]

>>> [y for y in [6, 1, 6, 1] if y > 2]

______



[6, 6]

>>> [[1] + s for s in [[4], [5, 6]]]

______



[[1, 4], [1, 5, 6]]

>>> [z + 1 for z in range(10) if z % 3 == 0]

______



[1, 4, 7, 10]
```

Toggle Solution (enable JavaScript)

### Q4: Close List

Implement `close_list`, which takes a list of integers `s` and a non-negative integer `k`. It returns a list of the elements of `s` that are within `k` of their index. That is, the absolute value of the difference between the element and its index is less than or equal to `k`.

```
def close_list(s: list[int], k: int) -> list[int]:
    """Return a list of the elements of s that are within k of their index.

    >>> t = [6, 2, 4, 3, 5]
    >>> close_list(t, 0)  # Only 3 is equal to its index
    [3]
    >>> close_list(t, 1)  # 2, 3, and 5 are within 1 of their index
    [2, 3, 5]
    >>> close_list(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    [2, 4, 3, 5]
    """
    assert k >= 0
    return [___ for i in range(len(s)) if ___]
```

Use Ok to test your code:

```
python3 ok -q close_list

Copy

✂️
```

  

Recursion
---------

### Q5: Double Eights

Write a **recursive** function that takes in a positive integer `n` and determines if its
digits contain two adjacent `8`s (that is, two `8`s right next to each other).

> **Hint:** Start by coming up with a recursive plan: the digits of a number have double eights if either  (think of something that is straightforward to check) or double eights appear in the rest of the digits.
>
> **Important:** Use recursion; the tests will fail if you use any loops (for, while), the `in` operator, or the `str` function.

```
def double_eights(n: int) -> bool:
    """Returns whether or not n has two digits in row that
    are the number 8.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> # ban iteration, in operator and str function 
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'double_eights', ['While', 'For', 'In', 'Str'])
    True
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q double_eights

Copy

✂️
```

  

### Q6: Making Onions

Write a function `make_onion` that takes in two one-argument functions, `f` and
`g`. It returns a function that takes in three arguments: `x`, `y`, and
`limit`. The returned function returns `True` if it is possible to reach `y`
from `x` using up to `limit` calls to `f` and `g`, and `False` otherwise.

For example, if `f` adds 1 and `g` doubles, then it is possible to reach 25 from
5 in four calls: `f(g(g(f(5))))`.

```
def make_onion(f, g):
    """Return a function can_reach(x, y, limit) that returns
    whether some call expression containing only f, g, and x with
    up to limit calls will give the result y.

    >>> up = lambda x: x + 1
    >>> double = lambda y: y * 2
    >>> can_reach = make_onion(up, double)
    >>> can_reach(5, 25, 4)      # 25 = up(double(double(up(5))))
    True
    >>> can_reach(5, 25, 3)      # Not possible
    False
    >>> can_reach(1, 1, 0)      # 1 = 1
    True
    >>> add_ing = lambda x: x + "ing"
    >>> add_end = lambda y: y + "end"
    >>> can_reach_string = make_onion(add_ing, add_end)
    >>> can_reach_string("cry", "crying", 1)      # "crying" = add_ing("cry")
    True
    >>> can_reach_string("un", "unending", 3)     # "unending" = add_ing(add_end("un"))
    True
    >>> can_reach_string("peach", "folding", 4)   # Not possible
    False
    """
    def can_reach(x, y, limit):
        if limit < 0:
            return ____
        elif x == y:
            return ____
        else:
            return can_reach(____, ____, limit - 1) or can_reach(____, ____, limit - 1)
    return can_reach
```

Use Ok to test your code:

```
python3 ok -q make_onion

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

### Q7: Function Repeater

Define a function `make_fn_repeater` which takes in a one-argument function `f` and an integer `x`.
It should return another function which takes in one argument, another integer.
This function returns the result of applying `f` to `x` this number of times.

Make sure to use recursion in your solution.

```
def make_func_repeater(f, x):
    """
    >>> increment_repeater = make_func_repeater(lambda x: x + 1, 1)
    >>> increment_repeater(2) #same as f(f(x))
    3
    >>> increment_repeater(5)
    6
    """
    def repeat(____):
        if ____:
            return ____
        else:
            return ____
    return ____
```

Use Ok to test your code:

```
python3 ok -q make_func_repeater

Copy

✂️
```

  

This is very similar to a homework problem, but recursive.
We recommend covering this if you have time, it ties recursion and higher order functions together in an interesting way.
Make sure to contrast with self-reference and show why this isn’t that,
both in behavior (here a single function call results in a bunch of computation not many function calls)
and in implementation (here a call to repeat *calls* repeat rather than returning a new repeat function).

### Q8: Ten-Pairs

Write a function that takes a positive integer `n` and returns the
number of ten-pairs it contains. A ten-pair is a pair of digits
within `n` that sums to 10.

The number 7,823,952 has 3 ten-pairs. The first and fourth digits sum
to 7+3=10, the second and third digits sum to 8+2=10, and the second
and last digit sum to 8+2=10.

Important notes:

* A digit can be part of more than one ten-pair.
* One 5 does not make a ten-pair with itself.

> *Recommended*: Complete and use the helper function `count_digit` to calculate
> how many times a digit appears in `n`.

**Important:** Use recursion; the tests will fail if you use any loops (for, while).

```
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952) # 7+3, 8+2, and 8+2
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469) # 9+1, 6+4, 6+4, 4+6, 1+9, 4+6 
    6
    >>> # ban iteration
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'ten_pairs', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5) # digit 5 appears 4 times in 55055
    4
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q ten_pairs

Copy

✂️
```

* [Attendance](index.html#attendance "index.html#attendance")
* [Topics](index.html#topics "index.html#topics")
* [Type Checking](index.html#type-checking "index.html#type-checking")
* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Lists](index.html#lists "index.html#lists")

- [Q1: WWPD: Lists & Ranges](index.html#q1-wwpd-lists-amp-ranges "index.html#q1-wwpd-lists-amp-ranges")
- [Q2: Close](index.html#q2-close "index.html#q2-close")

+ [List Comprehensions](index.html#list-comprehensions "index.html#list-comprehensions")

- [Q3: WWPD: List Comprehensions](index.html#q3-wwpd-list-comprehensions "index.html#q3-wwpd-list-comprehensions")
- [Q4: Close List](index.html#q4-close-list "index.html#q4-close-list")

+ [Recursion](index.html#recursion "index.html#recursion")

- [Q5: Double Eights](index.html#q5-double-eights "index.html#q5-double-eights")
- [Q6: Making Onions](index.html#q6-making-onions "index.html#q6-making-onions")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Optional Questions](index.html#optional-questions "index.html#optional-questions")

+ [Q7: Function Repeater](index.html#q7-function-repeater "index.html#q7-function-repeater")
+ [Q8: Ten-Pairs](index.html#q8-ten-pairs "index.html#q8-ten-pairs")
