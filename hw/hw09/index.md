Homework 9 | CS 61A Spring 2026



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



Homework 9: Programs as Data, Macros

* [hw09.zip](hw09.zip "hw09.zip")
=======================================================================

*Due by 11:59pm on Thursday, April 23*

Instructions
------------

Download [hw09.zip](hw09.zip "hw09.zip"). Inside the archive, you will find a file called
[hw09.scm](hw09.scm "hw09.scm"), along with a copy of the `ok` autograder.

**Submission:** When you are done, submit the assignment to Gradescope. You may submit more than once before the deadline; only the
final submission will be scored. Check that you have successfully submitted
your code on Gradescope.
See [Lab 0](../../lab/lab00.html "../../lab/lab00.html") for more instructions on submitting assignments.

**Using Ok:** If you have any questions about using Ok, please
refer to [this guide.](../../articles/using-ok.html "../../articles/using-ok.html")

**Readings:** You might find the following references
useful:

* [Scheme Specification](../../articles/scheme-spec/index.html "../../articles/scheme-spec/index.html")
* [Scheme Built-in Procedure Reference](../../articles/scheme-builtins/index.html "../../articles/scheme-builtins/index.html")

**Grading:** Homework is graded based on
correctness. Each incorrect problem will decrease the total score by one point.
**This homework is out of 2 points.**

The 61A Scheme interpreter is included in each Scheme assignment. To start it,
type `python3 scheme` in a terminal. To load a Scheme file called `f.scm`, type `python3 scheme -i f.scm`. To exit the Scheme interpreter, type
`(exit)`.

### Recommended VS Code Extensions

We recommend that you install the [vscode-scheme](https://marketplace.visualstudio.com/items?itemName=sjhuangx.vscode-scheme "https://marketplace.visualstudio.com/items?itemName=sjhuangx.vscode-scheme")
extension so that parentheses are highlighted.

Before:

![](assets/before.png)

After:

![](assets/after.png)

In addition, the 61a-bot ([installation instructions](../../articles/61a-bot.html "../../articles/61a-bot.html")) VS Code extension is available for Scheme homeworks. The bot is also integrated into `ok`.

### Visualizing Scheme Lists

If you would like some support with visualizing lists in Scheme, please navigate
to [code.cs61a.org](https://code.cs61a.org/ "https://code.cs61a.org/"), select *Start Scheme Interpreter*,
and call `(autodraw)`.

Required Questions
==================

Programs as Data: Chef Curry
----------------------------

Recall that currying transforms a multiple argument function into a series of higher-order, one argument functions. For a review of how this looks in Python, please see the following previous lecture video on [Function Currying](https://www.youtube.com/watch?v=6HMa5hfhRVc&list=PL6BsET-8jgYXTuSlJNYQS740YMCRHT79g&index=7 "https://www.youtube.com/watch?v=6HMa5hfhRVc&list=PL6BsET-8jgYXTuSlJNYQS740YMCRHT79g&index=7"). In the next set of questions, you will be creating functions that can automatically curry a function of any length using the notion that programs are data!

### Q1: Cooking Curry

Implement the function `curry-cook`, which takes in a Scheme list `formals` and a quoted expression `body`. `curry-cook` should generate a program as a list that is a curried version of a lambda function. The returned program should be a curried version of a lambda function with formal arguments equal to `formals`, and a function body equal to `body`. You may assume that all functions passed in will have more than 0 `formals`; otherwise, it would not be curry-able!

For example, if you wanted to curry the function `(lambda (x y) (+ x y))`, you would set `formals` equal to `'(x y)`, the `body` equal to `'(+ x y)`, and make a call to `curry-cook`: `(curry-cook '(x y) '(+ x y))`.

```
scm> (curry-cook '(a) 'a)
(lambda (a) a)
scm> (curry-cook '(x y) '(+ x y))
(lambda (x) (lambda (y) (+ x y)))
```

```
(define (curry-cook formals body)
    'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```
python3 ok -q curry-cook

Copy

✂️
```

  

### Q2: Consuming Curry

Implement the function `curry-consume`, which takes in a curried lambda function `curry` and applies the function to a list of arguments `args`. You may make the following assumptions:

1. If `curry` is an `n`-curried function, then there will be at most `n` arguments in `args`.
2. **If there are 0 arguments** (`args` is an empty list), then you may assume that `curry` has been fully applied with relevant arguments; in this case, `curry` now contains a value representing the output of the lambda function. Return it.

Note that there can be fewer `args` than `formals` for the corresponding lambda function `curry`! In the case that there are fewer arguments, `curry-consume` should return a curried lambda function, which is the result of partially applying `curry` up to the number of `args` provdied. See the doctests below for a few examples.

```
scm> (define three-curry (lambda (x) (lambda (y) (lambda (z) (+ x (* y z)))) ))
three-curry
scm> (define eat-two (curry-consume three-curry '(1 2))) ; pass in only two arguments, return should be a one-arg lambda function!
eat-two
scm> eat-two
(lambda (z) (+ x (* y z)))
scm> (eat-two 3) ; pass in the last argument; 1 + (2 * 3)
7
scm> (curry-consume three-curry '(1 2 3)) ; all three arguments at once
7
```

```
(define (curry-consume curry args)
    'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```
python3 ok -q curry-consume

Copy

✂️
```

  

Macros
------

### Q3: Switch to Cond

`switch` is a macro that takes in an expression `expr` and a list of pairs `options`, where the first element of each pair is a value and the second element is a single expression. `switch` evaluates the expression contained in the list of `options` that corresponds to the value that `expr` evaluates to. It then returns the value tied to that expression in `options`.

```
scm> (switch (+ 1 1) ((1 (print 'a))
                      (2 (print 'b)) ; (print 'b) is evaluated because (+ 1 1) evaluates to 2
                      (3 (print 'c))))
b
```

`switch` uses another procedure called `switch-to-cond` in its implementation:

```
scm> (define-macro (switch expr options)
                   (switch-to-cond (list 'switch expr options))
     )
```

  

Your task is to define `switch-to-cond`, a procedure (not a macro) that takes in a quoted `switch` expression and converts it into a `cond` expression with the same behavior. An example is shown below.

```
scm> (switch-to-cond `(switch (+ 1 1) ((1 2) (2 4) (3 6))))
(cond ((equal? (+ 1 1) 1) 2) ((equal? (+ 1 1) 2) 4) ((equal? (+ 1 1) 3) 6))
```

```
(define-macro (switch expr options) (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons _________
    (map
	  (lambda (option) (cons _______________ (cdr option)))
	  (car (cdr (cdr switch-expr))))))
```

Use Ok to test your code:

```
python3 ok -q switch-to-cond

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

Submit this assignment by uploading the `.scm` file **to the appropriate Pensieve assignment.** [Lab 00](../../lab/lab00.html "../../lab/lab00.html") has detailed instructions.

Exam Practice
=============

Homework assignments will also contain prior exam questions for you to try.
These questions have no submission component; feel free to attempt them if you'd like some practice!

Macros

1. Fall 2019 Final Q9: [Macro Lens](../../exam/fa19/final/61a-fa19-final.pdf#page=10 "../../exam/fa19/final/61a-fa19-final.pdf#page=10")
2. Summer 2019 Final Q10c: [Slice](../../exam/su19/final/61a-su19-final.pdf#page=10 "../../exam/su19/final/61a-su19-final.pdf#page=10")
3. Spring 2019 Final Q8: [Macros](../../exam/sp19/final/61a-sp19-final.pdf#page=8 "../../exam/sp19/final/61a-sp19-final.pdf#page=8")

* [Recommended VS Code Extensions](index.html#recommended-vs-code-extensions "index.html#recommended-vs-code-extensions")
* [Visualizing Scheme Lists](index.html#visualizing-scheme-lists "index.html#visualizing-scheme-lists")
* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Programs as Data: Chef Curry](index.html#programs-as-data-chef-curry "index.html#programs-as-data-chef-curry")

- [Q1: Cooking Curry](index.html#q1-cooking-curry "index.html#q1-cooking-curry")
- [Q2: Consuming Curry](index.html#q2-consuming-curry "index.html#q2-consuming-curry")

+ [Macros](index.html#macros "index.html#macros")

- [Q3: Switch to Cond](index.html#q3-switch-to-cond "index.html#q3-switch-to-cond")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Exam Practice](index.html#exam-practice "index.html#exam-practice")
