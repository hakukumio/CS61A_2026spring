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

*截止时间为 4 月 23 日（周四）晚上 11:59。*

Instructions
------------

下载 [hw09.zip](hw09.zip "hw09.zip")。在压缩包内，你会找到一个名为 [hw09.scm](hw09.scm "hw09.scm") 的文件，以及一份 `ok` autograder 的副本。

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

### Visualizing Scheme Lists

如果你想获得一些在 Scheme 中可视化 lists 的帮助，请访问 [code.cs61a.org](https://code.cs61a.org/ "https://code.cs61a.org/")，选择 *Start Scheme Interpreter*，然后调用 `(autodraw)`。

Required Questions
==================

Programs as Data: Chef Curry
----------------------------

回想一下，currying 会把一个多参数 function 转变为一系列 higher-order、单参数的 functions。如果想复习这在 Python 中是什么样子，请观看下面这个关于 [Function Currying](https://www.youtube.com/watch?v=6HMa5hfhRVc&list=PL6BsET-8jgYXTuSlJNYQS740YMCRHT79g&index=7 "https://www.youtube.com/watch?v=6HMa5hfhRVc&list=PL6BsET-8jgYXTuSlJNYQS740YMCRHT79g&index=7") 的往期 lecture 视频。在接下来的一组题目中，你将利用“程序即数据”这一概念，创建能够自动 curry 任意长度 function 的 functions！

### Q1: Cooking Curry

实现 `curry-cook` function，它接收一个 Scheme list `formals` 和一个 quoted expression `body`。`curry-cook` 应生成一个以 list 表示的程序，它是某个 lambda function 的 curried 版本。返回的程序应是一个 lambda function 的 curried 版本，其 formal arguments 等于 `formals`，function body 等于 `body`。你可以假设传入的所有 functions 的 `formals` 都多于 0 个；否则它就无法被 curry 了！

例如，如果你想 curry `(lambda (x y) (+ x y))` 这个 function，你会把 `formals` 设为 `'(x y)`，把 `body` 设为 `'(+ x y)`，然后调用 `curry-cook`：`(curry-cook '(x y) '(+ x y))`。

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

使用 Ok 来测试你的代码：

```
python3 ok -q curry-cook

Copy

✂️
```

  

### Q2: Consuming Curry

实现 `curry-consume` function，它接收一个 curried lambda function `curry`，并把该 function 应用到一个 arguments list `args` 上。你可以做以下假设：

1. 如果 `curry` 是一个 `n`-curried function，那么 `args` 中最多有 `n` 个 arguments。
2. **如果有 0 个 arguments**（`args` 是空 list），那么你可以假设 `curry` 已经用相关 arguments 完全应用过了；在这种情况下，`curry` 现在包含一个表示该 lambda function 输出的 value。返回它。

注意，对于对应的 lambda function `curry`，`args` 的数量可能少于 `formals`！在 arguments 较少的情况下，`curry-consume` 应返回一个 curried lambda function，即把 `curry` 部分应用到 `args` 中提供的 arguments 数量所得到的结果。请看下面的 doctests 中的几个例子。

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

使用 Ok 来测试你的代码：

```
python3 ok -q curry-consume

Copy

✂️
```

  

Macros
------

### Q3: Switch to Cond

`switch` 是一个 macro，它接收一个 expression `expr` 和一个 pairs list `options`，其中每个 pair 的第一个 element 是一个 value，第二个 element 是一个单独的 expression。`switch` 会求值 `options` list 中与 `expr` 求值结果相对应的那一项里所包含的 expression。然后它返回 `options` 中与该 expression 绑定的 value。

```
scm> (switch (+ 1 1) ((1 (print 'a))
                      (2 (print 'b)) ; (print 'b) is evaluated because (+ 1 1) evaluates to 2
                      (3 (print 'c))))
b
```

`switch` 在其实现中使用了另一个名为 `switch-to-cond` 的 procedure：

```
scm> (define-macro (switch expr options)
                   (switch-to-cond (list 'switch expr options))
     )
```

  

你的任务是定义 `switch-to-cond`，它是一个 procedure（不是 macro），接收一个 quoted `switch` expression 并把它转换成行为相同的 `cond` expression。示例如下。

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

使用 Ok 来测试你的代码：

```
python3 ok -q switch-to-cond

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
=============

作业中也会包含往年的考题供你尝试。这些题目没有提交要求；如果你想练习一下，可以随意尝试！

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
