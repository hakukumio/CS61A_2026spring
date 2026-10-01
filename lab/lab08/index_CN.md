Lab 8: Scheme | CS 61A Spring 2026



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



Lab 8: Scheme

* [lab08.zip](lab08.zip "lab08.zip")
===================================================

*截止时间为 4 月 8 日（周三）晚上 11:59。*

Starter Files
-------------

下载 [lab08.zip](lab08.zip "lab08.zip")。

Attendance
==========

如果你参加的是常规 61A lab，你的 TA 会过来为你 check in。你除了到场之外，还需要提交 lab problems，才能获得本次 lab 的学分。如果你参加的是 mega lab，那么只需提交 lab problems 即可获得学分。

如果你因为正当理由（例如生病或时间冲突）缺席 lab，或者因为某些原因没有被 check in，只需在两周内填写[此表单](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance")即可获得 attendance 学分。

Scheme Introduction
===================

每个 Scheme 作业中都包含 61A Scheme 解释器。要启动它，请在终端中输入 `python3 scheme`。要加载名为 `f.scm` 的 Scheme 文件，请输入 `python3 scheme -i f.scm`。要退出 Scheme 解释器，请输入 `(exit)`。

### Recommended VS Code Extensions

如果你选择使用 VS Code 作为文本编辑器（而不是基于网页的编辑器），请安装 [vscode-scheme](https://marketplace.visualstudio.com/items?itemName=sjhuangx.vscode-scheme "https://marketplace.visualstudio.com/items?itemName=sjhuangx.vscode-scheme") 扩展，以便括号能够高亮显示。

之前：

![](assets/before.png)

之后：

![](assets/after.png)
> **提示：**
> 在 VS Code 中，你可以按 **Control + `**（Tab 上方的那个键）来打开终端。

Required Questions
==================

Scheme
------

如果你需要复习 Scheme，请查阅下面的下拉框。你也可以直接跳到题目部分，遇到困难时再回到这里查阅。

Primitive Expressions (enable JavaScript)

Atomic expressions（也称为 *atoms*）是没有 sub-expressions 的 expression，例如 numbers、boolean values 和 symbols。

```
scm> 1234    ; integer
1234
scm> 123.4   ; real number
123.4
scm> #f      ; the Scheme equivalent of False in Python
#f
```

Scheme 的 *symbol* 等价于 Python 的 name。一个 symbol 求值为当前 environment 中绑定到该 symbol 的 value。（它们被称为 symbols 而不是 names，是因为它们包含 `+` 以及其他算术 symbols。）

```
scm> quotient      ; A symbol bound to a built-in procedure
#[quotient]
scm> +             ; A symbol bound to a built-in procedure
#[+]
```

在 Scheme 中，除了 `#f`（等价于 Python 中的 `False`）之外，*所有* values 都是 true values（不像 Python 还有其他 false values，例如 `0`）。

```
scm> #t
#t
scm> #f
#f
```

Call Expressions (enable JavaScript)

Scheme 使用 Polish prefix notation，其中 operator expression 位于 operand expressions 之前。例如，要计算 `3 * (4 + 2)`，我们写成：

```
scm> (* 3 (+ 4 2))
18
```

和 Python 中一样，求值一个 call expression 时：

1. 求值 operator。它应当求值为一个 procedure。
2. 从左到右求值 operands。
3. 把 procedure 应用到求值后的 operands 上。

以下是一些使用 built-in procedures 的例子：

```
scm> (+ 1 2)
3
scm> (- 10 (/ 6 2))
7
scm> (modulo 35 4)
3
scm> (even? (quotient 45 2))
#t
```

Special Forms (enable JavaScript)

**Define:**
`define` form 用于把 values 赋给 symbols。它的语法如下：

```
(define <symbol> <expression>)
```

```
scm> (define pi (+ 3 0.14))
pi
scm> pi
3.14
```

求值 `define` expression 时：

1. 求值最后一个 sub-expression（`<expression>`），在本例中它求值为 `3.14`。
2. 把那个 value 绑定到 symbol（`symbol`），在本例中是 `pi`。
3. 返回该 symbol。

`define` form 也可以定义新的 procedures，具体描述见 "Defining Functions" 一节。

**If Expressions:**
`if` special form 根据一个 predicate 求值两个 expressions 中的一个。

```
(if <predicate> <if-true> <if-false>)
```

求值一个 `if` special form expression 的规则如下：

1. 求值 `<predicate>`。
2. 如果 `<predicate>` 求值为一个 true value（除 `#f` 之外的任何值），则求值并返回 `<if-true>` expression 的 value。否则，求值并返回 `<if-false>` expression 的 value。

例如，即使 sub-expression `(/ 1 (- x 3))` 一旦被求值就会报错，这个 expression 也不会报错，并且求值为 5。

```
scm> (define x 3)
x
scm> (if (> (- x 3) 0) (/ 1 (- x 3)) (+ x 2))
5
```

`<if-false>` expression 是可选的。

```
scm> (if (= x 3) (print x))
3
```

让我们把 Scheme 的 `if` expression 与 Python 的 `if` statement 比较一下：

* 在 Scheme 中：

```
    (if (> x 3) 1 2)
```

* 在 Python 中：

```
    if x > 3:
        1
    else:
        2
```

Scheme 的 `if` expression 求值为一个 number（是 1 还是 2 取决于 `x`）。Python 的 statement 不会求值出任何东西，因此其中的 1 和 2 无法被使用或访问。

两者的另一个区别是：你可以在 Python `if` statement 的 suite 中添加更多行代码，而 Scheme 的 `if` expression 在 `<if-true>` 和 `<if-false>` 这两个位置各自只期望一个 expression。

最后一点区别是，在 Scheme 中你无法编写 `elif` clauses。

**Cond Expressions:**
`cond` special form 可以包含多个 predicates（类似于 Python 中的 if/elif）：

```
(cond
    (<p1> <e1>)
    (<p2> <e2>)
    ...
    (<pn> <en>)
    (else <else-expression>))
```

每个 clause 中的第一个 expression 是 predicate。clause 中的第二个 expression 是对应于其 predicate 的 return expression。`else` clause 是可选的；如果没有任何 predicate 为 true，那么它的 `<else-expression>` 就是 return expression。

求值规则如下：

1. 按顺序求值 predicates `<p1>`、`<p2>`、…、`<pn>`，直到其中一个求值为 true value（除 `#f` 之外的任何值）。
2. 求值并返回第一个求值为 true value 的 predicate expression 所对应的 return expression 的 value。
3. 如果没有任何 predicate 求值为 true value，并且存在 `else` clause，则求值并返回 `<else-expression>`。

例如，这个 `cond` expression 返回最接近 `x` 的 3 的倍数：

```
scm> (define x 5)
x
scm> (cond ((= (modulo x 3) 0) x)
            ((= (modulo x 3) 1) (- x 1))
            ((= (modulo x 3) 2) (+ x 1)))
6
```

  
  

**Lambdas:**
`lambda` special form 创建一个 procedure。

```
(lambda (<param1> <param2> ...) <body>)
```

这个 expression 会创建并返回一个带有给定 formal parameters 和 body 的 procedure，类似于 Python 中的 `lambda` expression。

```
scm> (lambda (x y) (+ x y))        ; Returns a lambda procedure, but doesn't assign it to a name
(lambda (x y) (+ x y))
scm> ((lambda (x y) (+ x y)) 3 4)  ; Create and call a lambda procedure in one line
7
```

以下是 Python 中与之等价的 expressions：

```
>>> lambda x, y: x + y
<function <lambda> at ...>
>>> (lambda x, y: x + y)(3, 4)
7
```

`<body>` 可以包含多个 expressions。一个 scheme procedure 返回其 body 中最后一个 expression 的 value。

Defining Functions (enable JavaScript)

`define` form 可以创建一个 procedure 并给它命名：

```
(define (<symbol> <param1> <param2> ...) <body>)
```

例如，下面是我们定义 `double` procedure 的方式：

```
scm> (define (double x) (* x 2))
double
scm> (double 3)
6
```

下面是一个带有三个 arguments 的例子：

```
scm> (define (add-then-mul x y z)
        (* (+ x y) z))
scm> (add-then-mul 3 4 5)
35
```

当一个 `define` expression 被求值时，会依次发生以下事情：

1. 用给定的 parameters 和 `<body>` 创建一个 procedure。
2. 在当前 frame 中把该 procedure 绑定到 `<symbol>`。
3. 返回 `<symbol>`。

下面两个 expressions 是等价的：

```
scm> (define add (lambda (x y) (+ x y)))
add
scm> (define (add x y) (+ x y))
add
```

Lists (enable JavaScript)

> 在阅读本节时，你可能很难理解 Scheme 各种容器的不同表示之间的区别。我们建议你使用[我们的在线 Scheme 解释器](http://scheme.cs61a.org "http://scheme.cs61a.org")，来查看那些你难以想象的 pairs 和 lists 的 box-and-pointer diagrams！（使用命令 `(autodraw)` 可以切换自动绘制 diagrams。）

### Lists

Scheme lists 与我们在 Python 中一直使用的 linked lists 非常相似。就像 linked list 是由一系列 `Link` objects 构成的一样，Scheme list 也是由一系列 pairs 构成的，而 pairs 由 constructor `cons` 创建。

Scheme lists 要求 `cdr` 要么是另一个 list，要么是 `nil`，即空 list。在解释器中，一个 list 会显示为 values 的 sequence（类似于 `Link` object 的 `__str__` 表示）。例如，

```
scm> (cons 1 (cons 2 (cons 3 nil)))
(1 2 3)
```

这里，我们确保了每个 `cons` expression 的第二个 argument 都是另一个 `cons` expression 或 `nil`。

![list](assets/list1.png)

我们可以用 `car` 和 `cdr` procedures 从 list 中取出 values，它们现在的作用类似于 Python 中 `Link` 的 `first` 和 `rest` attributes。（好奇这些古怪的名字从何而来吗？[看看它们的词源。](https://en.wikipedia.org/wiki/CAR_and_CDR "https://en.wikipedia.org/wiki/CAR_and_CDR")）

```
scm> (define a (cons 1 (cons 2 (cons 3 nil))))  ; Assign the list to the name a
a
scm> a
(1 2 3)
scm> (car a)
1
scm> (cdr a)
(2 3)
scm> (car (cdr (cdr a)))
3
```

如果你传给 `cons` 的第二个 argument 不是 pair 也不是 nil，它就会报错：

```
scm> (cons 1 2)
Error
```

### `list` Procedure

还有其他几种创建 lists 的方式。`list` procedure 接受任意数量的 arguments，并用这些 arguments 的 values 构造出一个 list：

```
scm> (list 1 2 3)
(1 2 3)
scm> (list 1 (list 2 3) 4)
(1 (2 3) 4)
scm> (list (cons 1 (cons 2 nil)) 3 4)
((1 2) 3 4)
```

注意，这个 expression 中的所有 operands 都会先被求值，然后才被放进所得的 list 中。

### Quote Form

我们也可以使用 quote form 来创建 list，它会原样构造出所给的 list。与 `list` procedure 不同，`'` 的 argument *不会*被求值。

```
scm> '(1 2 3)
(1 2 3)
scm> '(cons 1 2)           ; Argument to quote is not evaluated
(cons 1 2)
scm> '(1 (2 3 4))
(1 (2 3 4))
```

### Built-In Procedures for Lists

Scheme 中还有一些其他用于 lists 的 built-in procedures。在解释器中试试它们吧！

```
scm> (null? nil)                ; Checks if a value is the empty list
True
scm> (append '(1 2 3) '(4 5 6)) ; Concatenates two lists
(1 2 3 4 5 6)
scm> (length '(1 2 3 4 5))      ; Returns the number of elements in a list
5
```

### Q1: Over or Under

定义一个 procedure `over-or-under`，它接收一个 number `num1` 和一个 number `num2`，并返回以下结果：

* 如果 `num1` 小于 `num2`，返回 -1
* 如果 `num1` 等于 `num2`，返回 0
* 如果 `num1` 大于 `num2`，返回 1

> **注意：** 记住，Scheme 中每一对括号都构成一次 function call。例如，在 Scheme 解释器中只输入 `0` 会返回 `0`。然而，输入 `(0)` 会导致 Error，因为 `0` 不是 function。

*挑战：分别使用 `if` 和 `cond` 以 2 种不同的方式实现它！*

```
(define (over-or-under num1 num2)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```
python3 ok -q over_or_under

Copy

✂️
```

  

### Q2: Compose

编写 procedure `composed`，它接收 procedures `f` 和 `g`，并返回一个新的 procedure。这个新 procedure 接收一个 number `x`，并返回对 `g(x)` 调用 `f` 所得到的结果。

> **注意：** 调用 functions 时记得使用 *Scheme syntax*。形式是 `(func arg)`，而不是 `func(arg)`。

```
(define (composed f g)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```
python3 ok -q composed

Copy

✂️
```

  

### Q3: Repeat

编写 procedure `repeat`，它接收一个 procedure `f` 和一个 number `n`，并输出一个新的 procedure。这个新 procedure 接收一个 number `x`，并返回对 `x` 总共调用 `f` `n` 次的结果。例如：

```
scm> (define (square x) (* x x))
square
scm> ((repeat square 2) 5) ; (square (square 5))
625
scm> ((repeat square 3) 3) ; (square (square (square 3)))
6561
scm> ((repeat square 1) 7) ; (square 7)
49
```

> **提示：** 你在上一题中编写的 `composed` function 可能会很有用。

```
(define (repeat f n)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```
python3 ok -q repeat

Copy

✂️
```

  

### Q4: Greatest Common Divisor

最大公约数（GCD）是能同时整除两个正整数的最大整数。

编写 procedure `gcd`，它使用 Euclid's algorithm 计算 numbers `a` 和 `b` 的 GCD，该算法递归地利用这样一个事实：两个 values 的 GCD 是以下二者之一：

* 如果较小的 value 能整除较大的 value，则为较小的那个 value，或者
* 较小的 value 与（较大的 value 除以较小的 value 所得余数）的 greatest common divisor

换句话说，如果 `a` 大于 `b`，且 `a` 不能被 `b` 整除，那么

```
gcd(a, b) = gcd(b, a % b)  # please note that this is Python syntax
```

> 你可能会发现提供的 procedures `min` 和 `max` 很有用。也可以使用 built-in 的 `modulo` 和 `zero?` procedures。
>
> ```
> scm> (modulo 10 4)
> 2
> scm> (zero? (- 3 3))
> #t
> scm> (zero? 3)
> #f
> ```

```
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```
python3 ok -q gcd

Copy

✂️
```

  

Tail Calls
----------

Tail Calls (enable JavaScript)

在编写递归 procedure 时，可以把它写成 **tail recursive** 的方式，即所有递归调用都是 tail calls。**tail call** 发生在 function 把调用另一个 function 作为当前 frame 的最后一个动作时。

考虑下面这个 *不是* tail recursive 的 `factorial` 实现：

```
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))
```

递归调用出现在最后一行，但它并不是最后一个被求值的 expression。调用 `(factorial (- n 1))` 之后，function 还需要把该结果与 `n` 相乘。最后被求值的 expression 是对乘法 function 的调用，而不是 `factorial` 本身。因此，这个递归调用*不是* tail call。

下面是计算 `(factorial 6)` 的递归过程的可视化：

```
(factorial 6)
(* 6 (factorial 5))
(* 6 (* 5 (factorial 4)))
(* 6 (* 5 (* 4 (factorial 3))))
(* 6 (* 5 (* 4 (* 3 (factorial 2)))))
(* 6 (* 5 (* 4 (* 3 (* 2 (factorial 1))))))
(* 6 (* 5 (* 4 (* 3 (* 2 1)))))
(* 6 (* 5 (* 4 (* 3 2))))
(* 6 (* 5 (* 4 6)))
(* 6 (* 5 24))
(* 6 120)
720
```

解释器必须先到达 base case，然后才能开始计算之前各个 frame 中的乘积。

我们可以用一个 helper function 来重写这个 function，让它在每一步递归中记住目前已经计算出的临时乘积。

```
(define (factorial n)
  (define (fact-tail n result)
    (if (= n 0)
        result
        (fact-tail (- n 1) (* n result))))
  (fact-tail n 1))
```

`fact-tail` 对 `fact-tail` 做一次递归调用，而这次递归调用是最后一个被求值的 expression，所以它是一次 tail call。因此，`fact-tail` 是一个 tail recursive process。

下面是计算 `(factorial 6)` 的 tail recursive 过程的可视化：

```
(factorial 6)
(fact-tail 6 1)
(fact-tail 5 6)
(fact-tail 4 30)
(fact-tail 3 120)
(fact-tail 2 360)
(fact-tail 1 720)
(fact-tail 0 720)
720
```

解释器用更少的步骤就得出了结果，也不必回头访问之前的 frames 就能得出最终乘积。

在这个例子中，我们使用了实现 tail-recursive procedures 的一个常见策略：把我们正在累积的结果（例如一个 list、count、sum、product 等）作为 argument 传给 procedure，并在各次递归调用之间改变它。这样做，我们就不必在当前 frame 的递归调用之后再做任何计算来累积结果；相反，所有计算都在递归调用*之前*完成，结果被传给下一个 frame 以进一步修改。通常我们的 procedure 中并没有可以存储这个结果的 parameter，但在这些情况下，我们可以定义一个带有额外 parameter(s) 的 helper procedure，并在这个 helper 上递归。上面的 `factorial` procedure 中我们就是这么做的，其中 `fact-tail` 带有额外的 parameter `result`。

Tail Call Optimization
----------------------

当一个递归 procedure 不是以 tail recursive 的方式编写时，解释器必须有足够的内存来存储之前所有的递归调用。

例如，在非 tail-recursive 版本中调用 `(factorial 3)` 时，必须保留从 3 一直到 base case 的所有 numbers 的 frames，直到最终能够计算中间乘积并忘掉这些 frames：

![](assets/factorial_stack.svg)

对于非 tail-recursive 的 procedures，活跃 frames 的数量与递归调用的数量成正比增长。对于小的 inputs 这可能没问题，但想象一下对 10000 这样大的 number 调用 `factorial`，解释器将需要足够的内存来容纳全部 1000 次调用！

幸运的是，合格的 Scheme 解释器会按照语言规范的要求实现 **tail-call optimization**。TCO 保证 tail recursive procedures 能以常数数量的 active frames 执行，所以程序员可以在大的 inputs 上调用它们，而不必担心超出可用内存。

当 tail recursive 的 `factorial` 在支持 tail-call optimization 的解释器中运行时，解释器知道自己不需要保留之前的 frames，因此它永远不必在内存中存储整个 frames 的 stack：

![](assets/factorial_optimized.svg)

Tail-call optimization 可以通过以下几种方式实现：

1. 解释器可以不创建新的 frame，而是只更新当前 frame 中相关 variables 的 values（例如 `fact-tail` procedure 中的 `n` 和 `result`）。它在整个计算过程中复用同一个 frame，不断改变 bindings 以匹配下一组 parameters。
2. 我们的 61A Scheme 解释器采用的方式是：解释器照常构建一个新的 frame，然后用新 frame *替换*掉当前 frame。旧的 frame 依然存在，但解释器再也无法访问到它。当这种情况发生时，Python 解释器会做一件很聪明的事：它*回收*旧的 frame，这样下次需要新 frame 时，系统只需从回收的空间中分配即可。技术术语是：旧的 frame 变成了 "garbage"，系统在程序员背后对它进行 "garbage collect"。

Tail Context
------------

在判断一个 function body 中的某个 function call 是否是 tail call 时，我们要看这个 call expression 是否处于 **tail context**。

假设以下每个 expression 都是 function body 中的最后一个 expression，那么以下这些位置都是 tail context：

1. `if` expression 中的第二个或第三个 operand
2. `cond` expression 中任何非 predicate 的 sub-expressions（即每个 clause 的第二个 expression）
3. `and` 或 `or` expression 中的最后一个 operand
4. `begin` expression body 中的最后一个 operand
5. `let` expression body 中的最后一个 operand

例如，在 expression `(begin (+ 2 3) (- 2 3) (* 2 3))` 中，`(* 2 3)` 是 tail call，因为它是最后一个被求值的 operand expression。

### Q5: Exp

我们想实现 `exp` procedure。于是，我们编写了下面这个递归 procedure：

```
(define (exp-recursive b n)
  (if (= n 0)
      1
      (* b (exp-recursive b (- n 1)))))
```

试着求值

```
(exp-recursive 2 (exp-recursive 2 10))
```

你会发现这会导致 maximum recursion depth error。要解决这个问题，我们需要使用 tail recursion！请使用 tail recursion 实现 `exp` procedure：

```
(define (exp b n)
  ;; Computes b^n.
  ;; b is any number, n must be a non-negative integer.
  (define (helper n so-far) ;; since b never changes, we can use the b from the outer function
    ;; YOUR CODE HERE
  (helper n 1)
)
```

使用 Ok 来测试你的代码：

```
python3 ok -q exp

Copy

✂️
```

  

### Q6: Swap

编写一个 tail-recursive function `swap`，它接收一个 Scheme list `s`，并返回一个新的 Scheme list，其中 `s` 里每两个 elements 都被交换。

```
(define (swap s)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```
python3 ok -q swap

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

把这份作业提交上去，方法是把你编辑过的所有文件上传到**对应的 Gradescope 作业**。[Lab 00](../lab00.html#submitting-the-assignment "../lab00.html#submitting-the-assignment") 中有详细说明。

正确完成所有题目值 1 分。如果你参加的是常规 lab，你还需要 TA 记录的 attendance 才能拿到这 1 分。请在离开前确认你的 TA 已经记录了你的 attendance。

Optional Questions
==================

### Q7: Make Adder

编写一个 procedure `make-adder`，它接收一个 number `num` 作为输入，并返回一个新的 procedure。这个返回的 procedure 应接受另一个 number `inc`，并返回 `num` 与 `inc` 的和。

> **提示**：要返回一个 procedure，你可以返回一个 `lambda` expression，或者 `define` 另一个嵌套的 procedure。
>
> **注意**：`define` 不会返回 function，但 `lambda` 会。
>
> **提示**：Scheme 会自动返回你 procedure 中的最后一个 clause。
>
> 你可以在 [61A scheme 规范！](../../articles/scheme-spec/index.html#lambda "../../articles/scheme-spec/index.html#lambda") 中找到关于 `lambda` expressions 语法的文档。

```
(define (make-adder num)
  'YOUR-CODE-HERE
)
```

使用 Ok 来测试你的代码：

```
python3 ok -q make_adder

Copy

✂️
```

* [Attendance](index.html#attendance "index.html#attendance")
* [Scheme Introduction](index.html#scheme-introduction "index.html#scheme-introduction")

+ [Recommended VS Code Extensions](index.html#recommended-vs-code-extensions "index.html#recommended-vs-code-extensions")

* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Scheme](index.html#scheme "index.html#scheme")

- [Q1: Over or Under](index.html#q1-over-or-under "index.html#q1-over-or-under")
- [Q2: Compose](index.html#q2-compose "index.html#q2-compose")
- [Q3: Repeat](index.html#q3-repeat "index.html#q3-repeat")
- [Q4: Greatest Common Divisor](index.html#q4-greatest-common-divisor "index.html#q4-greatest-common-divisor")

+ [Tail Calls](index.html#tail-calls "index.html#tail-calls")

- [Q5: Exp](index.html#q5-exp "index.html#q5-exp")
- [Q6: Swap](index.html#q6-swap "index.html#q6-swap")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Optional Questions](index.html#optional-questions "index.html#optional-questions")

+ [Q7: Make Adder](index.html#q7-make-adder "index.html#q7-make-adder")
