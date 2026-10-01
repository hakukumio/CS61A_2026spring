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

*截止时间为 4 月 22 日（周三）晚上 11:59。*

Starter Files
-------------

下载 [lab10.zip](lab10.zip "lab10.zip")。




Attendance
==========

如果你参加的是常规 61A lab，你的 TA 会过来为你 check in。你除了到场之外，还需要提交 lab problems，才能获得本次 lab 的学分。如果你参加的是 mega lab，那么只需提交 lab problems 即可获得学分。

如果你因为正当理由（例如生病或时间冲突）缺席 lab，或者因为某些原因没有被 check in，只需在两周内填写[此表单](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance")即可获得 attendance 学分。

Required Questions
==================

Getting Started Videos (enable JavaScript)

Getting Started Videos
----------------------

这些视频可能会为解答这份作业中的编程题提供一些有用的指引。

> 要观看这些视频，你需要登录你的 berkeley.edu 邮箱。

[YouTube 链接](https://youtu.be/playlist?list=PLx38hZJ5RLZdGRYz2UKK_Nk-SIfc9ZKaS "https://youtu.be/playlist?list=PLx38hZJ5RLZdGRYz2UKK_Nk-SIfc9ZKaS")

Quasiquotation
--------------

如果你需要复习 quasiquotation，请查阅下拉框。你也可以直接跳到题目部分，遇到困难时再回到这里查阅。

Quasiquotation (enable JavaScript)

普通 quote `'` 和 quasiquote `` ` `` 都是引用一个 expression 的有效方式。不过，被 quasiquote 的 expression 可以用 "unquote" `,`（用逗号表示）来*取消引用*。当 quasiquoted expression 中的某个项被*取消引用*时，该项会被*求值*，而不是被当作字面文本。这个机制有些类似于 Python 中的 *f-strings*，其中 `{}` 内的 expressions 会被求值并插入到 string 中。

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

> 使用 Ok 来通过以下 "What Would Scheme Display?" 题目检验你的理解：
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

如果你需要复习 Programs as Data，请查阅下拉框。你也可以直接跳到题目部分，遇到困难时再回到这里查阅。

Programs as Data (enable JavaScript)

所有 Scheme 程序都由 expressions 组成。expressions 有两种类型：*primitive*（也叫 *atomic*）expressions 和 *combinations*。下面是每种类型的一些例子：

* *Primitive/atomic* expression: `#f`, `1.7`, `+`
* *Combinations*: `(factorial 10)`, `(/ 8 3)`, `(not #f)`

Scheme 把 combinations 表示为一个 Scheme list。因此，combination 可以通过 list manipulation 构造出来。

例如，expression `(list '+ 2 2)` 求值为 list `(+ 2 2)`，它本身也是一个 expression。如果我们随后对这个 list 调用 `eval`，它将求值为 `4`。`eval` procedure 接收一个参数 `expr`，并在当前环境中对 `expr` 求值。

```
scm> (define expr (list '+ 2 2))
expr
scm> expr
(+ 2 2)
scm> (eval expr)
4
```

此外，*quasiquotation* 对于构建能创建 expressions 的 procedures 非常有帮助。看看下面的 `add-program`：

```
scm> (define (add-program x y)
...>     `(+ ,x ,y))
add-program
scm> (add-program 3 6)
(+ 3 6)
```

`add-program` 接收两个输入 `x` 和 `y`，并返回一个 expression：如果对它求值，会得到把 `x` 和 `y` 相加的结果。在 `add-program` 内部，我们用 quasiquote 构建加法 expression `(+ ...)`，并对 `x` 和 `y` 进行 unquote，以在加法 expression 中取得它们求值后的值。

### Q2: If Program

在 Scheme 中，`if` special form 允许我们根据一个 predicate，求值两个 expressions 中的一个。编写一个 program `if-program`，它接收以下参数：

1. `predicate`：一个 quoted expression，它将求值为我们 `if`-expression 中的条件
2. `if-true`：一个 quoted expression，它将求值为当 `predicate` 求值为 true（`#t`）时我们返回的值
3. `if-false`：一个 quoted expression，它将求值为当 `predicate` 求值为 false（`#f`）时我们返回的值

这个 program 返回一个 Scheme list，表示一个形式为 `(if <predicate> <if-true> <if-false>)` 的 `if` expression。注意我们不想对该 expression 求值（至少在我们的 program 中不想）。

下面是一些展示这一点的 doctests：

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

使用 Ok 来测试你的代码：

```
python3 ok -q if-program

Copy

✂️
```

  

### Q3: Exponential Powers

实现一个 procedure `(pow-expr base exp)`，它返回一个 expression：求值该 expression 会把数字 `base` 提升到非负整数 `exp` 次幂。`pow-expr` 的主体不应执行任何乘法（或幂运算）。相反，它应只构造一个 expression，其中仅包含符号 `square` 和 `*`、数字 `base` 以及括号。这个 expression 的长度应随 `exp` 对数增长，而不是线性增长。

示例：

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

> *提示：*
>
> 1. x2y = (xy)2
> 2. x2y+1 = x(xy)2
>
> 例如，316 = (38)2，317 = 3 \* (38)2。
>
> 你可以使用内置 predicates `even?` 和 `odd?`。另外，`square` procedure 已经为你定义好了。

这里是[一道类似作业题的解答](../../hw/sol-hw07/index.html#q1-pow "../../hw/sol-hw07/index.html#q1-pow")。

```
(define (square n) (* n n))

(define (pow-expr base exp)
    'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```
python3 ok -q pow

Copy

✂️
```

  

Macros
------

A macro 是一种代码变换，用 `define-macro` 创建，并通过 call expression 应用。macro call 的求值过程是：

1. 把 macro 的 formal parameters 绑定到 macro call 中**未求值**的操作数 expressions 上。
2. 对 macro 的主体求值，它返回一个 expression。
3. 在原始 macro call 的 frame 中对 macro 返回的 expression 求值。

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

定义 `repeat`，一个 macro，它接收一个数字 `n` 和一个 expression `expr`。调用 `repeat` 会在 local frame 中对 `expr` 求值 `n` 次，其值就是最终结果。你会发现 helper function `repeated-call` 很有用，它接收一个数字 `n` 和一个 zero-argument procedure `f`，并调用 `f` `n` 次。

例如，`(repeat (+ 2 3) (print 1))` 等价于：

`(repeated-call (+ 2 3) (lambda () (print 1)))`

并且应重复求值 `(print 1)` 5 次。

下面的 expression 应打印 `four` 四次：

`(repeat 2 (repeat 2 (print 'four)))`

```
(define-macro (repeat n expr)
  `(repeated-call ,n ___))

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1) ___ (begin ___ ___)))
```

使用 Ok 来测试你的代码：

```
python3 ok -q repeat-lambda

Copy

✂️
```

  

Hint: repeat (enable JavaScript)

`repeated-call` procedure 接收一个 zero-argument procedure，所以空格处必须填 `(lambda () ___)`。lambda 的主体是 `expr`，它必须被 unquote。

Hint: repeated-call (enable JavaScript)

用 `(f)` 以无参数方式调用 `f`。如果 `n` 是 1，只需调用 `f`。如果 `n` 大于 1，先调用 `f`，然后调用 `(repeated-call (- n 1) f)`。

Check Your Score Locally
------------------------

你可以通过运行以下命令，在本地检查你在这份作业每道题上的得分：

```
python3 ok --score
```

**这并不会提交作业！** 当你对自己的得分满意后，请把作业提交到 Gradescope 以获得相应的学分。

Submit Assignment
=================

把这份作业提交上去，方法是把你编辑过的所有文件上传到**对应的 Gradescope 作业**。[Lab 00](../lab00.html#submitting-the-assignment "../lab00.html#submitting-the-assignment") 中有详细说明。

正确完成所有题目值 1 分。如果你参加的是常规 lab，你还需要 TA 记录的 attendance 才能拿到这 1 分。请在离开前确认你的 TA 已经记录了你的 attendance。

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
