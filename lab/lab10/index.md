Lab 10: Programs as Data, Macros | CS 61A Spring 2026



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



Lab 10: Programs as Data, Macros

* [lab10.zip](lab10.zip "lab10.zip")
======================================================================

*Due by 11:59pm on Wednesday, April 22.*

Starter Files
-------------

Download [lab10.zip](lab10.zip "lab10.zip").




Attendance
==========

If you are in a regular 61A lab, your TA will come around and check you in. You need to submit the lab problems in addition to attending to get credit for lab. If you are in the mega lab, you only need to submit the lab problems to get credit.

If you miss lab for a good reason (such as sickness or a scheduling conflict) or you don't get checked in for some reason, just fill out [this form](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance") within two weeks to receive attendance credit.

Required Questions
==================

Getting Started Videos (enable JavaScript)

Getting Started Videos
----------------------

These videos may provide some helpful direction for tackling the coding
problems on this assignment.

> To see these videos, you should be logged into your berkeley.edu email.

[YouTube link](https://youtu.be/playlist?list=PLx38hZJ5RLZdGRYz2UKK_Nk-SIfc9ZKaS "https://youtu.be/playlist?list=PLx38hZJ5RLZdGRYz2UKK_Nk-SIfc9ZKaS")

Quasiquotation
--------------

Consult the drop-down if you need a refresher on quasiquotation. It's
okay to skip directly to the questions and refer back
here should you get stuck.

Quasiquotation (enable JavaScript)

The normal quote `'` and the quasiquote `` ` `` are both valid ways to quote an
expression. However, the quasiquoted expression can be *unquoted* with the
"unquote" `,` (represented by a comma). When a term in a quasiquoted expression
is *unquoted*, the unquoted term is *evaluated*, instead of being taken as literal text.
This mechanism is somewhat akin to using *f-strings* in Python, where expressions
inside `{}` are evaluated and inserted into the string.

```
scm> (define a 5)
a
scm> (define b 3)
b
scm> `(* a b)  ; Quasiquoted expression
(* a b)
scm> `(* a ,b)  ; Unquoted b, which evaluates to 3
(* a 3)
scm> `(* ,(+ a b) b)  ; Unquoted (+ a b), which evaluates to 8
(* 8 b)
```

### Q1: WWSD: Quasiquote

> Use Ok to test your knowledge with the following "What Would Scheme Display?"
> questions:
>
> ```
> python3 ok -q wwsd-quasiquote -u
> ```

```
scm> '(1 x 3)

______



(1 x 3)

scm> (define x 2)

______



x

scm> `(1 x 3)

______



(1 x 3)

scm> `(1 ,x 3)

______



(1 2 3)

scm> `(1 x ,3)

______



(1 x 3)

scm> `(1 (,x) 3)

______



(1 (2) 3)

scm> `(1 ,(+ x 2) 3)

______



(1 4 3)

scm> (define y 3)

______



y

scm> `(x ,(* y x) y)

______



(x 6 y)

scm> `(1 ,(cons x (list y 4)) 5)

______



(1 (2 3 4) 5)
```

Toggle Solution (enable JavaScript)


Programs as Data
----------------

Consult the drop-down if you need a refresher on Programs as Data. It's
okay to skip directly to the questions and refer back
here should you get stuck.

Programs as Data (enable JavaScript)

All Scheme programs are made up of expressions.
There are two types of expressions: *primitive* (a.k.a *atomic*) expressions and *combinations*.
Here are some examples of each:

* *Primitive/atomic* expression: `#f`, `1.7`, `+`
* *Combinations*: `(factorial 10)`, `(/ 8 3)`, `(not #f)`

Scheme represents combinations as a Scheme list. Therefore, a combination can be constructed through list manipulation.

For example, the expression `(list '+ 2 2)` evaluates to the list `(+ 2 2)`, which is also an expression. If we then call `eval` on this list, it will evaluate to `4`. The `eval` procedure takes in one argument `expr` and evaluates `expr` in the current environment.

```
scm> (define expr (list '+ 2 2))
expr
scm> expr
(+ 2 2)
scm> (eval expr)
4
```

Additionally, *quasiquotation* is very helpful for building procedures that create expressions. Take a look at the following `add-program`:

```
scm> (define (add-program x y)
...>     `(+ ,x ,y))
add-program
scm> (add-program 3 6)
(+ 3 6)
```

`add-program` takes in two inputs `x` and `y` and returns an expression that, if evaluated, evaluates to the result of adding `x` and `y` together.
Within `add-program`, we use a quasiquote to build the addition expression `(+ ...)`, and we unquote `x` and `y` to get their evaluated values in the
addition expression.

### Q2: If Program

In Scheme, the `if` special form allows us to evaluate one of two expressions based on a predicate. Write a program `if-program` that takes in the following parameters:

1. `predicate` : a quoted expression which will evaluate to the condition in our `if`-expression
2. `if-true` : a quoted expression which will evaluate to the value we return if `predicate` evaluates to true (`#t`)
3. `if-false` : a quoted expression which will evaluate to the value we return if `predicate` evaluates to false (`#f`)

The program returns a Scheme list that represents an `if` expression in the form: `(if <predicate> <if-true> <if-false>)`. Note that we don't want to evaluate the expression (in our program at least).

Here are some doctests to show this:

```
scm> (define x 1)
scm> (if-program '(= 0 0) '(+ x 1) 'x)
(if (= 0 0) (+ x 1) x)
scm> (eval (if-program '(= 0 0) '(+ x 1) 'x))
2
scm> (if-program '(= 1 0) '(print 3) '(print 5))
(if (= 1 0) (print 3) (print 5))
scm> (eval (if-program '(= 1 0) '(print 3) '(print 5)))
5
```

  


```
(define (if-program condition if-true if-false)
  'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```
python3 ok -q if-program

Copy

✂️
```

  

### Q3: Exponential Powers

Implement a procedure `(pow-expr base exp)` that returns an expression that,
when evaluated, raises the number `base` to the power of the nonnegative integer
`exp`. The body of `pow-expr` should not perform any multiplication (or
exponentiation). Instead, it should just construct an expression containing only
the symbols `square` and `*` as well as the number `base` and parentheses. The
length of this expression should grow logarithmically with respect to `exp`,
rather than linearly.

Examples:

```
scm> (pow-expr 3 0)
1
scm> (pow-expr 3 1)
(* 3 1)
scm> (pow-expr 3 5)
(* 3 (square (square (* 3 1))))
scm> (pow-expr 3 15)
(* 3 (square (* 3 (square (* 3 (square (* 3 1)))))))
scm> (pow-expr 3 16)
(square (square (square (square (* 3 1)))))
scm> (eval (pow-expr 3 16))
43046721
```

> *Hint:*
>
> 1. x2y = (xy)2
> 2. x2y+1 = x(xy)2
>
> For example, 316 = (38)2 and 317 = 3 \* (38)2.
>
> You may use the built-in predicates `even?` and `odd?`. Also, the `square` procedure is defined for you.

Here's the [solution to a similar homework problem](../../hw/sol-hw07/index.html#q1-pow "../../hw/sol-hw07/index.html#q1-pow").

```
(define (square n) (* n n))

(define (pow-expr base exp)
    'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```
python3 ok -q pow

Copy

✂️
```

  

Macros
------

A macro is a code transformation that is created using `define-macro` and
applied using a call expression. A macro call is evaluated by:

1. Binding the formal parameters of the macro to the **unevaluated** operand expressions of the macro call.
2. Evaluating the body of the macro, which returns an expression.
3. Evaluating the expression returned by the macro in the frame of the original macro call.

```
scm> (define-macro (twice expr) (list 'begin expr expr))
twice
scm> (twice (+ 2 2))  ; evaluates (begin (+ 2 2) (+ 2 2))
4
scm> (twice (print (+ 2 2)))  ; evaluates (begin (print (+ 2 2)) (print (+ 2 2)))
4
4
```

### Q4: Repeat

Define `repeat`, a macro that takes a number `n` and an expression
`expr`. Calling `repeat` evaluates `expr` in a local frame `n` times, and its value is
the final result. You will find the helper function `repeated-call` useful, which
takes a number `n` and a zero-argument procedure `f` and calls `f` `n` number of times.

For example, `(repeat (+ 2 3) (print 1))` is equivalent to:

`(repeated-call (+ 2 3) (lambda () (print 1)))`

and should evaluate `(print 1)` repeatedly 5 times.

The following expression should print `four` four times:

`(repeat 2 (repeat 2 (print 'four)))`

```
(define-macro (repeat n expr)
  `(repeated-call ,n ___))

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1) ___ (begin ___ ___)))
```

Use Ok to test your code:

```
python3 ok -q repeat-lambda

Copy

✂️
```

  

Hint: repeat (enable JavaScript)

The `repeated-call` procedure takes a zero-argument procedure, so
`(lambda () ___)` must appear in the blank. The body of the lambda
is `expr`, which must be unquoted.

Hint: repeated-call (enable JavaScript)

Call `f` on no arguments with `(f)`. If `n` is 1, just call `f`. If `n` is
greater than 1, first call `f` and then call `(repeated-call (- n 1) f)`.

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

+ [Quasiquotation](index.html#quasiquotation "index.html#quasiquotation")

- [Q1: WWSD: Quasiquote](index.html#q1-wwsd-quasiquote "index.html#q1-wwsd-quasiquote")

+ [Programs as Data](index.html#programs-as-data "index.html#programs-as-data")

- [Q2: If Program](index.html#q2-if-program "index.html#q2-if-program")
- [Q3: Exponential Powers](index.html#q3-exponential-powers "index.html#q3-exponential-powers")

+ [Macros](index.html#macros "index.html#macros")

- [Q4: Repeat](index.html#q4-repeat "index.html#q4-repeat")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
