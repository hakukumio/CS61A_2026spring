Lab 9: Interpreters | CS 61A Spring 2026



[CS 61A](../index.html "../index.html")

* [Lectures](../index.html "../index.html")
* [Syllabus](../articles/about-61a/index.html "../articles/about-61a/index.html")
* [Ed](https://edstem.org/us/courses/93628/discussion "https://edstem.org/us/courses/93628/discussion")
* [Office Hours](../office-hours.html "../office-hours.html")
* [Contact](../articles/contact-61a/index.html "../articles/contact-61a/index.html")
* [Links](lab09.html# "lab09.html#")
  + [Request an Extension](https://go.cs61a.org/extensions "https://go.cs61a.org/extensions")
  + [Request a Regrade](https://go.cs61a.org/regrades "https://go.cs61a.org/regrades")
  + [Office Hours Queue](https://oh.cs61a.org/ "https://oh.cs61a.org/")
  + [Gradescope](https://www.gradescope.com/courses/1229052 "https://www.gradescope.com/courses/1229052")
  + [Add/Change Sections](https://sections.cs61a.org "https://sections.cs61a.org")
  + [Lecture Recordings](https://bcourses.berkeley.edu/courses/1547573/pages "https://bcourses.berkeley.edu/courses/1547573/pages")
  + [Python Tutor](https://pythontutor.com/cp/composingprograms.html "https://pythontutor.com/cp/composingprograms.html")
  + [Code Editors](https://code.cs61a.org/ "https://code.cs61a.org/")
* [Resources](lab09.html# "lab09.html#")
  + [Past Exams & Websites](../resources.html "../resources.html")
  + [Textbook](https://www.composingprograms.com "https://www.composingprograms.com")
  + [Campus Resources](../articles/campus-res/index.html "../articles/campus-res/index.html")
  + [Advice from Students](../articles/advice/index.html "../articles/advice/index.html")
  + [Scheme Specifications](../articles/scheme-spec/index.html "../articles/scheme-spec/index.html")
  + [Scheme Built-In Procedures](../articles/scheme-builtins/index.html "../articles/scheme-builtins/index.html")
* [Guides](lab09.html# "lab09.html#")
  + [Debugging Guide](https://drive.google.com/file/d/1O72u0ml65pibcjz-PXKpqeJDKaVqQ3D8/view "https://drive.google.com/file/d/1O72u0ml65pibcjz-PXKpqeJDKaVqQ3D8/view")
  + [Studying Guide](../articles/studying/index.html "../articles/studying/index.html")
  + [Type Hints](../articles/type-hints.html "../articles/type-hints.html")
  + [Composition Guide](../articles/composition/index.html "../articles/composition/index.html")
  + [MT1 Study Guide](../assets/pdfs/61a-mt1-study-guide.pdf "../assets/pdfs/61a-mt1-study-guide.pdf")
  + [MT2 Study Guide](../assets/pdfs/61a-mt2-study-guide.pdf "../assets/pdfs/61a-mt2-study-guide.pdf")
  + [Final Study Guide](../assets/pdfs/61a-final-study-guide.pdf "../assets/pdfs/61a-final-study-guide.pdf")
* [Staff](lab09.html# "lab09.html#")
  + [Instructors](../instructor.html "../instructor.html")
  + [TAs & Tutors](../staff.html "../staff.html")
  + [Teaching Interns](../teaching-interns.html "../teaching-interns.html")



Lab 9: Interpreters

* [lab09.zip](lab09/lab09.zip "lab09/lab09.zip")
=====================================================================

*Due by 11:59pm on Wednesday, April 15.*

Starter Files
-------------

Download [lab09.zip](lab09/lab09.zip "lab09/lab09.zip").

Attendance
==========

If you are in a regular 61A lab, your TA will come around and check you in. You need to submit the lab problems in addition to attending to get credit for lab. If you are in the mega lab, you only need to submit the lab problems to get credit.

If you miss lab for a good reason (such as sickness or a scheduling conflict) or you don't get checked in for some reason, just fill out [this form](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance") within two weeks to receive attendance credit.

Topics
======

Consult this section if you need a refresher on the material for this lab. It's
okay to skip directly to [the questions](lab09.html#required-questions "lab09.html#required-questions") and refer back
here should you get stuck.

  

Interpreters (enable JavaScript)

Interpreters
------------

An interpreter is a program that allows you to interact with the
computer using a specific language. It takes the code you write,
interprets it, and then executes the corresponding actions, often
using a more fundamental language to communicate with the computer
hardware.

In Project 4, you'll develop an interpreter for the Scheme
programming language using Python. Interestingly, the Python
interpreter you've been using throughout this course is primarily
written in the C programming language. At the lowest level, computers
operate by interpreting machine code, which is a series of ones and
zeros that instructs the computer on performing basic tasks such as
arithmetic operations and data retrieval.

When we talk about an interpreter, there are two languages at work:

1. **The language being interpreted:** For Project 4, this is the Scheme language.
2. **The implementation language:** This is the language used to create
   the interpreter itself, which, for Project 4, will be Python.

  

**REPL**

A common feature of interpreters is the Read-Eval-Print Loop (REPL), which processes user inputs in a cyclic fashion through three stages:

* **Read:** The interpreter first reads the input string provided by the user.
  This input goes through a parsing process that involves two key steps:

  + The *lexical analysis* step breaks down the input string into tokens,
    which are the basic elements or "words" of the language you're
    interpreting. These tokens represent the smallest units of meaning within the input.
  + The *syntactic analysis* step takes the tokens from the previous step and organizes
    them into a data structure that the underlying language can understand. For our
    Scheme interpreter, we assemble the tokens into a `Link` object (similar to a
    `Link`), to represent the structure of the original call expression.

    - The first item in the `Link` represents the operator of the call expression, while the subsequent elements are the operands or arguments upon which the operation will act. Note that these operands can also be call expressions themselves (nested expressions).

Below is a summary of the read process for a Scheme expression input:

![](lab09/assets/parser.png)

* **Eval:** This step evaluates the expressions you've written in that programming
  language to obtain a value. It involves the following two functions:

  + `eval` takes an expression and evaluates it based on the language's rules.
    When the expression is a call expression, `eval` uses the `apply` function to obtain the result.
    It will evaluate the operator and its operands in order. For example, in `(add 1 2)`,
    `eval` would identify `add` as the operator and `1` and `2` as the operands.
    It evaluates `add` to ensure it's a valid function and then evaluates `1` and
    `2` to ensure they're valid arguments.
  + `apply` takes the evaluated operator (the function) and applies it to the
    evaluated operands (the arguments). Note that it's possible that, during this process, `apply` needs to evaluate more expressions (like those found within the function body). This is where `apply` may call back to `eval`, and thus these two stages are *mutually recursive*.
* **Print:** Display the result of evaluating the user input.

  
Here's how all the pieces fit together:  

![](lab09/assets/repl.png)

  

Interpreters (enable JavaScript)

Evaluation
----------

To evaluate the expression `(+ (* 3 4) 5)` using the interpreter,
`scheme_eval` is called on the following expressions (in this order):

1. `(+ (* 3 4) 5)`
2. `+`
3. `(* 3 4)`
4. `*`
5. `3`
6. `4`
7. `5`

The `*` is evaluated because it is the operator sub-expression of `(* 3 4)`,
which is an operand sub-expression of `(+ (* 3 4) 5)`.

By default, `*` evaluates to a procedure that multiplies its arguments together.
But `*` could be redefined at any time, and so the symbol `*` must be evaluated
each time it is used in order to look up its current value.

```
scm> (* 2 3)  ; Now it multiplies
6
scm> (define * +)
*
scm> (* 2 3)  ; Now it adds
5
```

  

Required Questions
==================

Calculator
----------

An interpreter is a program that executes programs. Today, we will extend the interpreter for Calculator, a simple made-up language that is a subset of Scheme. This lab is like the Scheme Project in miniature.

The Calculator language includes only the four basic arithmetic operations: `+`, `-`, `*`, and `/`. These operations can be nested and can take various numbers of arguments, just like in Scheme. A few examples of calculator expressions and their corresponding values are shown below.

```
 calc> (+ 2 2 2)
 6

 calc> (- 5)
 -5

 calc> (* (+ 1 2) (+ 2 3 4))
 27
```

Calculator expressions are represented as Python objects:

* Numbers are represented using Python numbers.
* The symbols for arithmetic operations are represented using Python strings (e.g. `'+'`).
* Call expressions are represented using the `Link` class below.

Link Class
----------

To represent Scheme lists in Python, we will use the `Link` class (in both this lab and the Scheme project). A `Link` instance has two attributes: `first` and `rest`. `Link` is always called on two arguments. To make a list, nest calls to `Link` and pass in `nil` as the second argument of the last Link.

> **Note:** In the Python code, `nil` is bound to `Link.empty`.
> Similarly, `nil` in Scheme evaluates to an empty list.

For example, once our interpreter reads in the Scheme expression `(+ 2 3)`, it is represented as `Link('+', Link(2, Link(3, nil)))`.

```
>>> p = Link('+', Link(2, Link(3, nil)))
>>> p.first
'+'
>>> p.rest
Link(2, Link(3, nil))
>>> p.rest.first
2
>>> print(p)
(+ 2 3)
```

There is a `map_link` function that takes a one-argument Python function `f` and a linked list `s`. It returns the Scheme list that results from applying `f` to each element of the Scheme list.

```
>>> map_link(lambda x: 2 * x, p.rest)
Link(4, Link(6, nil))
```

  

Here is the `Link` class and `map_link` function (`__str__` and `__repr__` methods not
shown).

```
class Link:
    """Represents the built-in Link data structure in Scheme."""
    empty = ()
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

nil = Link.empty

def map_link(f, s):
    """Map function f over linked list s.
    >>> square = lambda x: x * x
    >>> map_link(square, Link(1, Link(2, Link(3))))
    Link(1, Link(4, Link(9, nil)))
    """
    if s is Link.empty:
        return s
    return Link(f(s.first), map_link(f, s.rest))
```

  


### Q1: Using Link

Answer the following questions about a `Link` instance
representing the Calculator expression `(+ (- 2 4) 6 8)`.

Use Ok to test your understanding:

```
python3 ok -q using_link -u

Copy

✂️
```

  

Calculator Evaluation
---------------------

For Question 2 (New Procedure) and Question 4 (Saving Values), you'll need to update the `calc_eval` function below, which evaluates a Calculator expression. For Question 2, you'll determine what the `operator` and `operands` are for a call expression in Scheme as well as how to apply a procedure to arguments in the `calc_apply` line. For Question 4, you'll determine how to look up the value of symbols that have been previously defined.

```
def calc_eval(exp):
    """
    >>> calc_eval(Link("define", Link("a", Link(1, nil))))
    'a'
    >>> calc_eval("a")
    1
    >>> calc_eval(Link("+", Link(1, Link(2, nil))))
    3
    """
    if isinstance(exp, Link):
        operator = ____________ # UPDATE THIS FOR Q2, e.g (+ 1 2), + is the operator
        operands = ____________ # UPDATE THIS FOR Q2, e.g (+ 1 2), 1 and 2 are operands
        if operator == 'and': # and expressions
            return eval_and(operands)
        elif operator == 'define': # define expressions
            return eval_define(operands)
        else: # Call expressions
            return calc_apply(___________, ___________) # UPDATE THIS FOR Q2, what is type(operator)?
    elif exp in OPERATORS:   # Looking up procedures
        return OPERATORS[exp]
    elif isinstance(exp, int) or isinstance(exp, bool):   # Numbers and booleans
        return exp
    elif _________________: # CHANGE THIS CONDITION FOR Q4, where are variables stored?
        return _________________ # UPDATE THIS FOR Q4, how do you access a variable?
```

### Q2: New Procedure

Add the `//` operation to Calculator, a floor-division procedure such that `(// dividend divisor)` returns the result of dividing `dividend` by `divisor`, ignoring the remainder (`dividend // divisor` in Python). Handle multiple inputs as illustrated in the following example: `(// dividend divisor1 divisor2 divisor3)` evaluates to `(((dividend // divisor1) // divisor2) // divisor3)` in Python. Assume every call to `//` has at least two arguments.

> *Hint:* You will need to modify both the `calc_eval` and `floor_div` methods for this question!

```
calc> (// 1 1)
1
calc> (// 5 2)
2
calc> (// 28 (+ 1 1) 1)
14
```

> *Hint:* Make sure that every element in a `Link` (the operator and all operands) will be `calc_eval`-uated once so that we can correctly apply the relevant Python operator to operands!



```
def floor_div(args):
    """
    >>> floor_div(Link(100, Link(10, nil)))
    10
    >>> floor_div(Link(5, Link(3, nil)))
    1
    >>> floor_div(Link(1, Link(1, nil)))
    1
    >>> floor_div(Link(5, Link(2, nil)))
    2
    >>> floor_div(Link(23, Link(2, Link(5, nil))))
    2
    >>> calc_eval(Link("//", Link(4, Link(2, nil))))
    2
    >>> calc_eval(Link("//", Link(100, Link(2, Link(2, Link(2, Link(2, Link(2, nil))))))))
    3
    >>> calc_eval(Link("//", Link(100, Link(Link("+", Link(2, Link(3, nil))), nil))))
    20
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q floor_div

Copy

✂️
```

  

### Q3: New Form

Add `and` expressions to our
Calculator interpreter as well as introduce the Scheme boolean values
`#t` and `#f`, represented as Python `True` and `False`.
The examples below assumes conditional operators (e.g. `<`, `>`, `=`, etc) have already been implemented,
but you do not have to worry about them for this question.

```
calc> (and (= 1 1) 3)
3
calc> (and (+ 1 0) (< 1 0) (/ 1 0))
#f
calc> (and #f (+ 1 0))
#f
calc> (and 0 1 (+ 5 1)) ; 0 is a true value in Scheme!
6
```

In a call expression, we first evaluate the operator, then evaluate the operands, and finally apply the procedure to its arguments (just like you did for `floor_div` in the previous question).
However, we cannot evaluate `and` expressions the same way we evaluate call expressions. Since `and` is a special form that short circuits on the first false argument, we need to add special logic so that we don't always evaluate all of the sub-expressions.

> **Important**: To check whether some `val` is a false value in Scheme, use
> `val is scheme_f` rather than `val == scheme_f` because in Python `0 == False`
> but `0 is not False` (crazy, right!).

```
scheme_t = True   # Scheme's #t
scheme_f = False  # Scheme's #f

def eval_and(expressions):
    """
    >>> calc_eval(Link("and", Link(1, nil)))
    1
    >>> calc_eval(Link("and", Link(False, Link("1", nil))))
    False
    >>> calc_eval(Link("and", Link(1, Link(Link("//", Link(5, Link(2, nil))), nil))))
    2
    >>> calc_eval(Link("and", Link(Link('+', Link(1, Link(1, nil))), Link(3, nil))))
    3
    >>> calc_eval(Link("and", Link(Link('-', Link(1, Link(0, nil))), Link(Link('/', Link(5, Link(2, nil))), nil))))
    2.5
    >>> calc_eval(Link("and", Link(0, Link(1, nil))))
    1
    >>> calc_eval(Link("and", nil))
    True
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q eval_and

Copy

✂️
```

  

### Q4: Saving Values

Implement a `define` special form that binds values to symbols. This should work like `define` in Scheme: `(define <symbol> <expression>)` first evaluates the `expression`, then binds the `symbol` to the value of `expression`. The whole `define` expression evaluates to the `symbol`. Here's an example to illustrate:

```
calc> (define a 1)
a
calc> a
1
```

This is a more involved change. Here are the 4 steps involved:

1. Add a `bindings` dictionary that will store the symbols and correspondings values (done for you).
2. Identify when the define form is given to `calc_eval` (done for you).
3. Modify `calc_eval` to allow the lookup of symbols in `bindings` and get their values.
4. Write the function `eval_define` which adds the defined symbol and its value to the bindings dictionary.

```
bindings = {}

def eval_define(expressions):
    """
    >>> eval_define(Link("a", Link(1, nil)))
    'a'
    >>> eval_define(Link("b", Link(3, nil)))
    'b'
    >>> eval_define(Link("c", Link("a", nil)))
    'c'
    >>> calc_eval("c")
    1
    >>> calc_eval(Link("define", Link("d", Link("//", nil))))
    'd'
    >>> calc_eval(Link("d", Link(4, Link(2, nil))))
    2
    """
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:

```
python3 ok -q eval_define

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

Submit this assignment by uploading any files you've edited **to the appropriate Gradescope assignment.** [Lab 00](lab00.html#submitting-the-assignment "lab00.html#submitting-the-assignment") has detailed instructions.

Correctly completing all questions is worth one point. If you are in the regular lab, you will need your attendance from your TA to receive that one point. Please ensure your TA has taken your attendance before leaving.

* [Attendance](lab09.html#attendance "lab09.html#attendance")
* [Topics](lab09.html#topics "lab09.html#topics")
* [Required Questions](lab09.html#required-questions "lab09.html#required-questions")

+ [Calculator](lab09.html#calculator "lab09.html#calculator")
+ [Link Class](lab09.html#link-class "lab09.html#link-class")

- [Q1: Using Link](lab09.html#q1-using-link "lab09.html#q1-using-link")

+ [Calculator Evaluation](lab09.html#calculator-evaluation "lab09.html#calculator-evaluation")

- [Q2: New Procedure](lab09.html#q2-new-procedure "lab09.html#q2-new-procedure")
- [Q3: New Form](lab09.html#q3-new-form "lab09.html#q3-new-form")
- [Q4: Saving Values](lab09.html#q4-saving-values "lab09.html#q4-saving-values")

+ [Check Your Score Locally](lab09.html#check-your-score-locally "lab09.html#check-your-score-locally")

* [Submit Assignment](lab09.html#submit-assignment "lab09.html#submit-assignment")
