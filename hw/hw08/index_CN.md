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

*截止时间为 4 月 16 日（周四）晚上 11:59。*

Instructions
------------

下载 [hw08.zip](hw08.zip "hw08.zip")。在压缩包内，你会找到一个名为 [hw08.scm](hw08.scm "hw08.scm") 的文件，以及一份 `ok` autograder 的副本。

**提交：** 完成后，请把作业提交到 Gradescope。在截止时间之前你可以多次提交；只以最后一次提交计分。请确认你已在 Gradescope 上成功提交代码。有关提交作业的更多说明，请参见 [Lab 0](../../lab/lab00.html "../../lab/lab00.html")。

**使用 Ok：** 如果你对 Ok 的使用有任何疑问，请参阅[此指南。](../../articles/using-ok.html "../../articles/using-ok.html")

**阅读材料：** 你可能会发现以下参考资料很有用：

* [Scheme Specification](../../articles/scheme-spec/index.html "../../articles/scheme-spec/index.html")
* [Scheme Built-in Procedure Reference](../../articles/scheme-builtins/index.html "../../articles/scheme-builtins/index.html")

**评分：** 作业根据正确性评分。每答错一道题，总分就会减少 1 分。**这份作业满分为 2 分。**

每个 Scheme 作业中都包含 61A Scheme interpreter。要启动它，请在终端中输入 `python3 scheme`。要加载一个名为 `f.scm` 的 Scheme 文件，请输入 `python3 scheme -i f.scm`。要退出 Scheme interpreter，请输入 `(exit)`。

### Recommended VS Code Extensions

我们建议你安装 [vscode-scheme](https://marketplace.visualstudio.com/items?itemName=sjhuangx.vscode-scheme "https://marketplace.visualstudio.com/items?itemName=sjhuangx.vscode-scheme") extension，这样括号就会被高亮显示。

之前：

![](assets/before.png)

之后：

![](assets/after.png)

此外，61a-bot（[安装说明](../../articles/61a-bot.html "../../articles/61a-bot.html")）VS Code extension 也可用于 Scheme 作业。这个 bot 同样集成在 `ok` 中。

Required Questions
==================

Required Questions
------------------

如果你需要参考任何 scheme syntax，这会很有帮助：https://cs61a.org/articles/scheme-spec/

### Q1: Ascending

实现一个名为 `ascending?` 的 procedure，它接收一个 numbers list `s`，如果这些数字按非降序排列则返回 `True`，否则返回 `False`。

如果 numbers list 中除第一个之外的每个 element 都大于或等于前一个 element，那么这个 numbers list 就是非降序的。例如……

* `(1 2 3 3 4)` 是非降序的。
* `(1 2 3 3 2)` 不是。

> 提示：内置的 `null?` procedure 返回其参数是否为 `nil`。

> **注意**：`ascending?` 中的问号只是 procedure 名称的一部分，在 Scheme syntax 中没有任何特殊含义。在 Scheme 中，如果一个 procedure 返回 boolean value，那么以问号结尾来命名它是一种常见做法。

```
(define (ascending? s)
  'YOUR-CODE-HERE
)
```

使用 Ok 来解锁并测试你的代码：

```
python3 ok -q ascending -u
python3 ok -q ascending

Copy

✂️
```

  


### Q2: My Filter

编写一个 procedure `my-filter`，它接收一个单参数 predicate function `pred`（一个返回 True 或 False 的 function）和一个 list `s`。`my-filter` 返回一个新 list，其中只包含 list `s` 中满足该 predicate 的 elements。返回的 list 中各 element 的顺序应与它们在原 list `s` 中出现的顺序相同。

例如，`(my-filter even? '(1 2 3 4 5))` 应该返回 `(2 4)`，因为只有 `2` 和 `4` 是偶数。

> **注意**：在这道题中你**不允许**使用 Scheme 内置的 `filter` function —— 我们是要你重新实现它！

```
(define (my-filter pred s)
  'YOUR-CODE-HERE
)
```



使用 Ok 来解锁并测试你的代码：

```
python3 ok -q filter -u
python3 ok -q filter

Copy

✂️
```

  


### Q3: Interleave

实现 `interleave` function，它接收两个 lists `lst1` 和 `lst2` 作为参数，返回一个新 list，其中的 elements 交替来自这两个 lists，并以 `lst1` 开头。

如果其中一个输入 list 比另一个短，`interleave` 应一直交替包含两个 lists 的 elements，直到较短的 list 用完，然后把较长 list 中剩余的 elements 追加到末尾。如果 `lst1` 或 `lst2` 中有任意一个为空，该 function 应返回另一个非空 list。

例如：

* `(interleave '(1 2 3) '(4 5 6))` 应该返回 `(1 4 2 5 3 6)`。
* `(interleave '(7 8 9 10) '(11 12))` 应该返回 `(7 11 8 12 9 10)`。

```
(define (interleave lst1 lst2)
'YOUR-CODE-HERE
)
```

使用 Ok 来解锁并测试你的代码：

```
python3 ok -q interleave -u
python3 ok -q interleave

Copy

✂️
```

  

### Q4: No Repeats

实现 `no-repeats`，它接收一个 numbers list `s`。它返回一个 list，其中包含 `s` 的所有 unique elements，按照它们首次出现的顺序排列，但没有重复。换句话说，返回一个移除了所有重复项且保持顺序的新 list。

例如，`(no-repeats (list 5 4 5 4 2 2))` 求值为 `(5 4 2)`。

> 提示：用 `filter` 配合 `lambda` procedure 来过滤掉重复项可能会很有帮助。要测试两个数字 `a` 和 `b` 是否不相等，请使用 `(not (= a b))`。

```
(define (no-repeats s)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```
python3 ok -q no_repeats

Copy

✂️
```

  

Check Your Score Locally
------------------------

你可以通过运行以下命令，在本地检查你在这份作业每道题上的得分

```
python3 ok --score
```

**这并不会提交作业！** 当你对自己的得分满意后，请把作业提交到 Gradescope 以获得相应的学分。

Submit Assignment
=================

把这份作业提交上去，方法是把 `.scm` 文件上传到**对应的 Pensieve 作业**。[Lab 00](../../lab/lab00.html "../../lab/lab00.html") 中有详细说明。

Exam Practice
-------------

以下是往几学期的一些 Scheme List 考题，你可能会觉得它们对额外练习考试有帮助。

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
