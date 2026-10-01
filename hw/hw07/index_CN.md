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

*截止时间为 4 月 9 日（周四）晚上 11:59。*

Instructions
------------

下载 [hw07.zip](hw07.zip "hw07.zip")。在该压缩包中，你会找到一个名为 [hw07.scm](hw07.scm "hw07.scm") 的文件，以及一份 `ok` autograder 的副本。

**提交：** 完成后，请把作业提交到 Gradescope。你可以在截止时间前多次提交；只有最后一次提交会被计分。请检查你是否已经在 Gradescope 上成功提交了你的代码。提交作业的更多说明见 [Lab 0](../../lab/lab00.html "../../lab/lab00.html")。

**使用 Ok：** 如果你对使用 Ok 有任何疑问，请参考[这份指南。](../../articles/using-ok.html "../../articles/using-ok.html")

**阅读材料：** 你可能会觉得以下参考资料很有用：

* [Scheme Specification](../../articles/scheme-spec/index.html "../../articles/scheme-spec/index.html")
* [Scheme Built-in Procedure Reference](../../articles/scheme-builtins/index.html "../../articles/scheme-builtins/index.html")

**评分：** Homework 依据正确性评分。每答错一道题，总分就会减少一分。**这份 homework 满分为 2 分。**

每个 Scheme 作业中都包含 61A Scheme interpreter。要启动它，请在终端中输入 `python3 scheme`。要加载名为 `f.scm` 的 Scheme 文件，请输入 `python3 scheme -i f.scm`。要退出 Scheme interpreter，请输入 `(exit)`。

### Recommended VS Code Extensions

我们建议你安装 [vscode-scheme](https://marketplace.visualstudio.com/items?itemName=sjhuangx.vscode-scheme "https://marketplace.visualstudio.com/items?itemName=sjhuangx.vscode-scheme") 扩展，以便高亮显示括号。

之前：

![](assets/before.png)

之后：

![](assets/after.png)

此外，还有适用于 Scheme homeworks 的 61a-bot（[安装说明](../../articles/61a-bot.html "../../articles/61a-bot.html")）VS Code 扩展。这个 bot 也集成到了 `ok` 中。

Required Questions
==================

### Q1: Pow

实现一个 procedure `pow`，它计算数字 `base` 的非负整数 `exp` 次幂。递归调用 `pow` 的次数应随 `exp` 呈对数增长，而不是线性增长。例如，`(pow 2 32)` 应产生 5 次递归的 `pow` 调用，而不是 32 次。

> *提示：*
>
> 1. x2y = (xy)2
> 2. x2y+1 = x(xy)2
>
> 例如，216 = (28)2，217 = 2 \* (28)2。
>
> 你可以使用内置 predicates `even?` 和 `odd?`。此外，`square` procedure 已经为你定义好了。
>
> Scheme 没有 `while` 或 `for` 语句，所以请使用递归来解决这道题。

```
(define (square n) (* n n))

(define (pow base exp)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```
python3 ok -q pow

Copy

✂️
```

  

### Q2: Repeatedly Cube

实现 `repeatedly-cube`，它接收一个数字 `x`，并对其进行 `n` 次立方。

以下是一些例子，说明 `repeatedly-cube` 应如何表现：

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

使用 Ok 来测试你的代码：

```
python3 ok -q repeatedly-cube

Copy

✂️
```

  

### Q3: Cadr and Caddr

定义 procedure `cadr`，它返回一个 list 的第二个 element。再定义 `caddr`，它返回一个 list 的第三个 element。尝试用 `car` 和 `cdr` 来写 `cadr` 和 `caddr`。

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

使用 Ok 来测试你的代码：

```
python3 ok -q cadr-caddr

Copy

✂️
```

  

Check Your Score Locally
------------------------

你可以通过运行以下命令，在本地检查你在这份作业每道题上的得分：

```
python3 ok --score
```

**这并不会提交作业！** 当你对自己的得分满意后，请把作业提交到 Gradescope 以获得相应的学分。

Submit Assignment
=================

把这份作业提交上去，方法是把 `.scm` 文件上传到**对应的 Pensieve 作业**。[Lab 00](../../lab/lab00.html "../../lab/lab00.html") 中有详细说明。

* [Recommended VS Code Extensions](index.html#recommended-vs-code-extensions "index.html#recommended-vs-code-extensions")
* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Q1: Pow](index.html#q1-pow "index.html#q1-pow")
+ [Q2: Repeatedly Cube](index.html#q2-repeatedly-cube "index.html#q2-repeatedly-cube")
+ [Q3: Cadr and Caddr](index.html#q3-cadr-and-caddr "index.html#q3-cadr-and-caddr")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
