Homework 8 | CS 61A Spring 2026



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



Homework 8: Scheme Lists

* [hw08.zip](hw08.zip "hw08.zip")
===========================================================

*Due by 11:59pm on Thursday, April 16*

Instructions
------------

Download [hw08.zip](hw08.zip "hw08.zip"). Inside the archive, you will find a file called
[hw08.scm](hw08.scm "hw08.scm"), along with a copy of the `ok` autograder.

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

Required Questions
------------------

If you need to reference any scheme syntax, this would help: https://cs61a.org/articles/scheme-spec/

### Q1: Ascending

Implement a procedure called `ascending?`, which takes a list of numbers `s` and
returns `True` if the numbers are in non-descending order, and `False`
otherwise.

A list of numbers is non-descending if each element after the first is
greater than or equal to the previous element. For example...

* `(1 2 3 3 4)` is non-descending.
* `(1 2 3 3 2)` is not.

> **Hint**: The built-in `null?` procedure returns whether its argument is `nil`.

> **Note**: The question mark in `ascending?` is just part of the procedure name and has no special meaning in terms of Scheme syntax. It is a common practice in Scheme to name procedures with a question mark at the end if it returns a boolean value.

```
(define (ascending? s)
  'YOUR-CODE-HERE
)
```

Use Ok to unlock and test your code:

```
python3 ok -q ascending -u
python3 ok -q ascending

Copy

✂️
```

  


### Q2: My Filter

Write a procedure `my-filter`, which takes in a one-argument predicate function `pred` (a function that returns True or False)
and a list `s`. `my-filter` returns a new list containing only elements in list `s` that satisfy the
predicate. The returned list should contain the elements in the same order that they
appeared in the original list `s`.

For example, `(my-filter even? '(1 2 3 4 5))` should return `(2 4)` because only `2` and `4` are even.

> **Note:** You are **not allowed** to use the Scheme built-in `filter` function in this question - we are asking you to re-implement this!

```
(define (my-filter pred s)
  'YOUR-CODE-HERE
)
```



Use Ok to unlock and test your code:

```
python3 ok -q filter -u
python3 ok -q filter

Copy

✂️
```

  


### Q3: Interleave

Implement the function `interleave`, which takes two lists `lst1` and `lst2` as
arguments, and returns a new list that alternates elements from both lists, starting with `lst1`.

If one of the input lists is shorter than the other, `interleave` should include
elements from both lists until the shorter list is exhausted, and
then append the remaining elements of the longer list to the end.
If either `lst1` or `lst2` is empty, the function should return the other non-empty list.

For example:

* `(interleave '(1 2 3) '(4 5 6))` should return `(1 4 2 5 3 6)`.
* `(interleave '(7 8 9 10) '(11 12))` should return `(7 11 8 12 9 10)`.

```
(define (interleave lst1 lst2)
'YOUR-CODE-HERE
)
```

Use Ok to unlock and test your code:

```
python3 ok -q interleave -u
python3 ok -q interleave

Copy

✂️
```

  

### Q4: No Repeats

Implement `no-repeats`, which takes a list of numbers `s`. It returns a list
that has all of the unique elements of `s` in the order that they first appear,
but no repeats. In other words, return a new list with all duplicates removed and order preserved.

For example, `(no-repeats (list 5 4 5 4 2 2))` evaluates to `(5 4 2)`.

> **Hint:** You may find it helpful to use `filter` with a `lambda` procedure to
> filter out repeats. To test if two numbers `a` and `b` are not equal, use
> `(not (= a b))`.

```
(define (no-repeats s)
  'YOUR-CODE-HERE
)
```

Use Ok to test your code:

```
python3 ok -q no_repeats

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
-------------

The following are some Scheme List exam problems from previous semesters that you may find useful as additional exam practice.

1. [Fall 2022 Final, Question 8: A Parentheses Scheme](../../exam/fa22/final/61a-fa22-final.pdf#page=20 "../../exam/fa22/final/61a-fa22-final.pdf#page=20")
2. [Spring 2022 Final, Question 11: Beadazzled, The Scheme-quel](../../exam/sp22/final/61a-sp22-final.pdf#page=23 "../../exam/sp22/final/61a-sp22-final.pdf#page=23")
3. [Fall 2021 Final, Question 4: Spice](../../exam/fa21/final/61a-fa21-final.pdf#page=18 "../../exam/fa21/final/61a-fa21-final.pdf#page=18")

* [Recommended VS Code Extensions](index.html#recommended-vs-code-extensions "index.html#recommended-vs-code-extensions")
* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Required Questions](index.html#required-questions-2 "index.html#required-questions-2")

- [Q1: Ascending](index.html#q1-ascending "index.html#q1-ascending")
- [Q2: My Filter](index.html#q2-my-filter "index.html#q2-my-filter")
- [Q3: Interleave](index.html#q3-interleave "index.html#q3-interleave")
- [Q4: No Repeats](index.html#q4-no-repeats "index.html#q4-no-repeats")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")

+ [Exam Practice](index.html#exam-practice "index.html#exam-practice")
