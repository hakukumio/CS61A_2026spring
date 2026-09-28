Homework 7 | CS 61A Spring 2026



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



Homework 7: Scheme

* [hw07.zip](hw07.zip "hw07.zip")
=====================================================

*Due by 11:59pm on Thursday, April 9*

Instructions
------------

Download [hw07.zip](hw07.zip "hw07.zip"). Inside the archive, you will find a file called
[hw07.scm](hw07.scm "hw07.scm"), along with a copy of the `ok` autograder.

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

Required Questions
==================

### Q1: Pow

Implement a procedure `pow` that raises a number `base` to the power of a nonnegative integer `exp`. The number of recursive `pow` calls should grow logarithmically with respect to `exp`, rather than linearly. For example, `(pow 2 32)` should result in 5 recursive `pow` calls rather than 32 recursive `pow` calls.

> *Hint:*
>
> 1. x2y = (xy)2
> 2. x2y+1 = x(xy)2
>
> For example, 216 = (28)2 and 217 = 2 \* (28)2.
>
> You may use the built-in predicates `even?` and `odd?`. Also, the `square` procedure is defined for you.
>
> Scheme doesn't have `while` or `for` statements, so use recursion to solve this problem.

```
(define (square n) (* n n))

(define (pow base exp)
  'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```
python3 ok -q pow

Copy

✂️
```

  

### Q2: Repeatedly Cube

Implement `repeatedly-cube`, which receives a number `x` and cubes it `n` times.

Here are some examples of how `repeatedly-cube` should behave:

```
scm> (repeatedly-cube 100 1) ; 1 cubed 100 times is still 1
1
scm> (repeatedly-cube 2 2) ; (2^3)^3
512
scm> (repeatedly-cube 3 2) ; ((2^3)^3)^3
134217728
```

```
(define (repeatedly-cube n x)
    (if (zero? n)
        x
        (begin
            (define y ___)
            ___)))
```

Use Ok to test your code:

```
python3 ok -q repeatedly-cube

Copy

✂️
```

  

### Q3: Cadr and Caddr

Define the procedure `cadr`, which returns the second element of a list. Also define `caddr`, which returns the third element of a list.
Try writing `cadr` and `caddr` in terms of `car` and `cdr`.

```
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
)

(define (caddr s)
  'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```
python3 ok -q cadr-caddr

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

* [Recommended VS Code Extensions](index.html#recommended-vs-code-extensions "index.html#recommended-vs-code-extensions")
* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Q1: Pow](index.html#q1-pow "index.html#q1-pow")
+ [Q2: Repeatedly Cube](index.html#q2-repeatedly-cube "index.html#q2-repeatedly-cube")
+ [Q3: Cadr and Caddr](index.html#q3-cadr-and-caddr "index.html#q3-cadr-and-caddr")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
