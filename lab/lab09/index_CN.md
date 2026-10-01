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

*截止时间为 4 月 15 日（周三）晚上 11:59。*

Starter Files
-------------

下载 [lab09.zip](lab09/lab09.zip "lab09/lab09.zip")。

Attendance
==========

如果你参加的是常规 61A lab，你的 TA 会过来为你 check in。你除了到场之外，还需要提交 lab problems，才能获得本次 lab 的学分。如果你参加的是 mega lab，那么只需提交 lab problems 即可获得学分。

如果你因为正当理由（例如生病或时间冲突）缺席 lab，或者因为某些原因没有被 check in，只需在两周内填写[此表单](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance")即可获得 attendance 学分。

Topics
======

如果你需要复习本次 lab 的材料，请查阅本节。你也可以直接跳到[题目部分](lab09.html#required-questions "lab09.html#required-questions")，遇到困难时再回到这里查阅。

  

Interpreters (enable JavaScript)

Interpreters
------------

解释器是一个程序，它让你能够使用某种特定的语言与计算机交互。它接收你编写的代码，把它解释出来，然后执行相应的动作，通常使用一种更底层的语言来与计算机硬件通信。

在 Project 4 中，你将使用 Python 开发一个用于 Scheme 编程语言的解释器。有趣的是，你在这门课中一直使用的 Python 解释器主要是用 C 编程语言编写的。在最底层，计算机通过解释 machine code 来运作，machine code 是一系列 1 和 0，指示计算机执行算术运算、数据读取等基本任务。

当我们谈论解释器时，有两种语言在起作用：

1. **被解释的语言：** 对于 Project 4，这就是 Scheme 语言。
2. **实现语言：** 这是用来创建解释器本身的语言，对于 Project 4 来说就是 Python。

  

**REPL**

解释器的一个常见特性是 Read-Eval-Print Loop（REPL），它循环地通过三个阶段处理用户输入：

* **Read:** 解释器首先读取用户提供的 input string。这个 input 会经历一个 parsing 过程，其中包含两个关键步骤：

  + *lexical analysis* 步骤把 input string 分解成 tokens，tokens 是你所解释的语言的基本 elements 或 "words"。这些 tokens 表示 input 中最小的意义单位。
  + *syntactic analysis* 步骤接收上一步得到的 tokens，并把它们组织成底层语言能够理解的数据结构。对于我们的 Scheme 解释器，我们把 tokens 组装成一个 `Link` object（类似于 `Link`），以表示原始 call expression 的结构。

    - `Link` 中的第一个 item 表示 call expression 的 operator，而后续 elements 则是这次运算将要作用的 operands 或 arguments。注意，这些 operands 本身也可以是 call expressions（嵌套的 expressions）。

下面是对 Scheme expression 输入的 read 过程的总结：

![](lab09/assets/parser.png)

* **Eval:** 这一步求值你用该编程语言写下的 expressions，以获得一个 value。它涉及以下两个 functions：

  + `eval` 接收一个 expression，并依据语言的规则对它求值。当这个 expression 是 call expression 时，`eval` 使用 `apply` function 来获得结果。它会按顺序求值 operator 及其 operands。例如，在 `(add 1 2)` 中，`eval` 会把 `add` 识别为 operator，把 `1` 和 `2` 识别为 operands。它先求值 `add`，确保它是一个有效的 function，然后求值 `1` 和 `2`，确保它们是有效的 arguments。
  + `apply` 接收求值后的 operator（即 function），并把它应用到求值后的 operands（即 arguments）上。注意，在这个过程中，`apply` 可能需要求值更多的 expressions（比如 function body 中的那些）。这时 `apply` 可能会回调 `eval`，因此这两个阶段是*相互递归*的。
* **Print:** 显示对用户输入求值的结果。

  
下面展示所有这些部分是如何组合起来的：  

![](lab09/assets/repl.png)

  

Interpreters (enable JavaScript)

Evaluation
----------

要使用解释器求值 expression `(+ (* 3 4) 5)`，会按以下顺序对下列 expressions 调用 `scheme_eval`：

1. `(+ (* 3 4) 5)`
2. `+`
3. `(* 3 4)`
4. `*`
5. `3`
6. `4`
7. `5`

`*` 会被求值，因为它是 `(* 3 4)` 的 operator sub-expression，而 `(* 3 4)` 是 `(+ (* 3 4) 5)` 的 operand sub-expression。

默认情况下，`*` 求值为一个把其 arguments 相乘的 procedure。但 `*` 随时可能被重新定义，因此 symbol `*` 每次被使用时都必须求值，以查找它的当前 value。

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

解释器是一个执行程序的程序。今天，我们将扩展 Calculator 的解释器，Calculator 是一种简单的自创语言，它是 Scheme 的一个子集。这次 lab 就像是缩小版的 Scheme Project。

Calculator 语言只包含四种基本算术运算：`+`、`-`、`*` 和 `/`。这些运算可以嵌套，并且可以接受不同数量的 arguments，就像在 Scheme 中一样。下面展示了几个 calculator expressions 及其对应 values 的例子。

```
 calc> (+ 2 2 2)
 6

 calc> (- 5)
 -5

 calc> (* (+ 1 2) (+ 2 3 4))
 27
```

Calculator expressions 用 Python objects 表示：

* Numbers 用 Python numbers 表示。
* 算术运算的 symbols 用 Python strings 表示（例如 `'+'`）。
* Call expressions 用下面的 `Link` class 表示。

Link Class
----------

为了在 Python 中表示 Scheme lists，我们将使用 `Link` class（本次 lab 和 Scheme project 都是如此）。一个 `Link` instance 有两个 attributes：`first` 和 `rest`。`Link` 总是以两个 arguments 被调用。要构造一个 list，请嵌套调用 `Link`，并把 `nil` 作为最后一个 Link 的第二个 argument 传入。

> **注意：** 在 Python 代码中，`nil` 绑定到 `Link.empty`。类似地，Scheme 中的 `nil` 求值为一个空 list。

例如，当我们的解释器读入 Scheme expression `(+ 2 3)` 后，它被表示为 `Link('+', Link(2, Link(3, nil)))`。

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

有一个 `map_link` function，它接收一个单参数的 Python function `f` 和一个 linked list `s`。它返回把 `f` 应用到 Scheme list 的每个 element 上所得的 Scheme list。

```
>>> map_link(lambda x: 2 * x, p.rest)
Link(4, Link(6, nil))
```

  

下面是 `Link` class 和 `map_link` function（未展示 `__str__` 和 `__repr__` methods）。

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

回答以下关于表示 Calculator expression `(+ (- 2 4) 6 8)` 的 `Link` instance 的问题。

使用 Ok 来检验你的理解：

```
python3 ok -q using_link -u

Copy

✂️
```

  

Calculator Evaluation
---------------------

对于 Question 2（New Procedure）和 Question 4（Saving Values），你需要更新下面这个负责求值 Calculator expression 的 `calc_eval` function。对于 Question 2，你要确定 Scheme 中 call expression 的 `operator` 和 `operands` 分别是什么，以及在 `calc_apply` 那一行中如何把 procedure 应用到 arguments 上。对于 Question 4，你要确定如何查找之前已定义的 symbols 的 value。

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

向 Calculator 添加 `//` 运算，它是一个 floor-division procedure：`(// dividend divisor)` 返回 `dividend` 除以 `divisor` 的结果，忽略余数（在 Python 中即 `dividend // divisor`）。按下面的例子处理多个输入：`(// dividend divisor1 divisor2 divisor3)` 在 Python 中求值为 `(((dividend // divisor1) // divisor2) // divisor3)`。假设每次调用 `//` 都至少有 2 个 arguments。

> *提示：* 这道题中你需要同时修改 `calc_eval` 和 `floor_div` 这两个 methods！

```
calc> (// 1 1)
1
calc> (// 5 2)
2
calc> (// 28 (+ 1 1) 1)
14
```

> *提示：* 确保 `Link` 中的每个 element（operator 和所有 operands）都会被 `calc_eval` 一次，这样我们才能正确地把相应的 Python operator 应用到 operands 上！



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

使用 Ok 来测试你的代码：

```
python3 ok -q floor_div

Copy

✂️
```

  

### Q3: New Form

向我们的 Calculator 解释器添加 `and` expressions，并引入 Scheme 的 boolean values `#t` 和 `#f`，它们分别用 Python 的 `True` 和 `False` 表示。下面的例子假设条件运算符（例如 `<`、`>`、`=` 等）已经实现，但对于这道题你无需关心它们。

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

在一个 call expression 中，我们先求值 operator，再求值 operands，最后把 procedure 应用到它的 arguments 上（就像你在上一题中对 `floor_div` 所做的那样）。然而，我们不能用求值 call expressions 的同样方式来求值 `and` expressions。由于 `and` 是一个在第一个 false argument 处短路的 special form，我们需要添加特殊逻辑，以免总是求值所有 sub-expressions。

> **重要**：要检查某个 `val` 在 Scheme 中是否是 false value，请使用 `val is scheme_f` 而不是 `val == scheme_f`，因为在 Python 中 `0 == False`，但 `0 is not False`（很疯狂，对吧！）。

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

使用 Ok 来测试你的代码：

```
python3 ok -q eval_and

Copy

✂️
```

  

### Q4: Saving Values

实现一个把 values 绑定到 symbols 的 `define` special form。它的工作方式应与 Scheme 中的 `define` 相同：`(define <symbol> <expression>)` 先求值 `expression`，再把 `symbol` 绑定到 `expression` 的 value。整个 `define` expression 求值为 `symbol`。下面用一个例子来说明：

```
calc> (define a 1)
a
calc> a
1
```

这是一个比较复杂的改动。涉及以下 4 个步骤：

1. 添加一个 `bindings` dictionary，用来存储 symbols 及其对应的 values（已为你完成）。
2. 识别 define form 何时被传给 `calc_eval`（已为你完成）。
3. 修改 `calc_eval`，使其能够在 `bindings` 中查找 symbols 并取到它们的 values。
4. 编写 function `eval_define`，把所定义的 symbol 及其 value 添加到 bindings dictionary 中。

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

使用 Ok 来测试你的代码：

```
python3 ok -q eval_define

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

把这份作业提交上去，方法是把你编辑过的所有文件上传到**对应的 Gradescope 作业**。[Lab 00](lab00.html#submitting-the-assignment "lab00.html#submitting-the-assignment") 中有详细说明。

正确完成所有题目值 1 分。如果你参加的是常规 lab，你还需要 TA 记录的 attendance 才能拿到这 1 分。请在离开前确认你的 TA 已经记录了你的 attendance。

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
