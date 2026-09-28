# 实验 2：高阶函数、Lambda 表达式 - [lab02.zip](https://lr2933.github.io/cs61a-spring-2026/lab/lab02/lab02.zip)

*截止时间：2 月 4 日（周三）晚上 11:59。*

## 起始文件

下载 [lab02.zip](https://lr2933.github.io/cs61a-spring-2026/lab/lab02/lab02.zip)。

# 出勤

如果你参加的是常规 61A 实验课，助教会过来给你签到。除了出勤之外，你还必须提交实验题目才能获得实验课学分。如果你参加的是大实验课（mega lab），那么只需提交实验题目即可获得学分。

如果你因为正当理由（例如生病或时间冲突）缺席实验课，或者由于某种原因没有被签到，只需在两周内填写[这份表单](http://go.cs61a.org/lab-attendance)，即可获得出勤学分。

# 知识点

如果你需要复习本次实验的内容，请查阅本节。直接跳到题目部分也没问题，遇到困难时再回来查阅即可。

## 短路求值

你觉得在 Python 中输入下面的内容会发生什么？

```
1 / 0
```

在 Python 里试一试！你应该会看到 `ZeroDivisionError`。但下面这个表达式呢？

```
True or 1 / 0
```

它求值为 `True`，因为 Python 的 `and` 和 `or` 运算符会*短路*。也就是说，它们不一定会对每个操作数求值。

| 运算符 | 检查 | 从左到右求值直到 | 示例 |
| --- | --- | --- | --- |
| AND | 所有值都为真 | 第一个假值 | `False and 1 / 0` 求值为 `False` |
| OR | 至少有一个值为真 | 第一个真值 | `True or 1 / 0` 求值为 `True` |

当运算符遇到某个操作数、并据此足以对表达式得出结论时，短路就发生了。例如，`and` 一旦遇到第一个假值就会短路，因为它此时知道并非所有值都为真。

如果 `and` 和 `or` *没有*短路，它们就返回最后一个值；换个角度记：无论是否短路，`and` 和 `or` 总是返回它们所求值的最后一个东西。请记住，当使用的值不是 `True` 和 `False` 时，`and` 和 `or` 并不总是返回布尔值。

## 高阶函数

变量是绑定到值的名字，这些值可以是 `3` 或 `'Hello World'` 之类的原始值，但也可以是函数。而由于函数可以接受任意值作为参数，其他函数就可以作为参数传进来。这就是高阶函数的基础。

高阶函数是指通过接受函数作为参数、返回一个函数，或两者兼有来操作其他函数的函数。我们将在本次实验中介绍高阶函数的基础知识，并在下一次实验中探索高阶函数的许多应用。

### 函数作为参数

在 Python 中，函数对象是可以被传来传去的值。我们知道创建函数的一种方式是使用 `def` 语句：

```
def square(x):
    return x * x
```

上面的语句创建了一个内部名（intrinsic name）为 `square` 的函数对象，并将它绑定到当前环境中的名字 `square` 上。现在让我们试着把它作为参数传进去。

首先，我们来写一个接受另一个函数作为参数的函数：

```
def scale(f, x, k):
    """ Returns the result of f(x) scaled by k. """
    return k * f(x)
```

现在我们可以用 `square` 和其他一些参数来调用 `scale`：

```
>>> scale(square, 3, 2) # Double square(3)
18
>>> scale(square, 2, 5) # 5 times 2 squared
20
```

注意，在调用 `scale` 的函数体中，内部名为 `square` 的函数对象被绑定到了参数 `f` 上。然后，我们在 `scale` 的函数体中通过调用 `f(x)` 来调用 `square`。

正如我们在上面关于 `lambda` 表达式的那一节中所看到的，我们也可以把 `lambda` 表达式传入调用表达式！

```
>>> scale(lambda x: x + 10, 5, 2)
30
```

在这个调用表达式的栈帧中，名字 `f` 被绑定到由 `lambda` 表达式 `lambda x: x + 10` 创建的函数上。

### 返回函数的函数

因为函数是值，所以它们也可以作为返回值！下面是一个例子：

```
def multiply_by(m):
    def multiply(n):
        return n * m
    return multiply
```

在这个例子中，我们在 `multiply_by` 的函数体内定义了函数 `multiply`，然后把它返回。让我们看看实际效果：

```
>>> multiply_by(3)
<function multiply_by.<locals>.multiply at ...>
>>> multiply(4)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'multiply' is not defined
```

如预期的那样，调用 `multiply_by` 会返回一个函数。然而，调用 `multiply` 却报错了，尽管这正是我们给内部函数起的名字。这是因为名字 `multiply` 只存在于我们求值 `multiply_by` 函数体的那个栈帧之中。

那么我们要如何真正使用这个内部函数呢？有两种方式：

```
>>> times_three = multiply_by(3) # Assign the result of the call expression to a name
>>> times_three(5) # Call the inner function with its new name
15
>>> multiply_by(3)(10) # Chain together two call expressions
30
```

关键在于，由于 `multiply_by` 返回一个函数，你可以像使用任何其他函数一样使用它的返回值。

> [YouTube 视频：高阶函数](https://youtu.be/UlXvz-34Me0?si=GNpQEGHKoTMBsNOr)

## Lambda 表达式

Lambda 表达式是通过指定两样东西来求值为函数的表达式：参数和一个返回表达式。

```
lambda <parameters>: <return expression>
```

虽然 `lambda` 表达式和 `def` 语句都会创建函数对象，但它们之间有一些显著的区别。`lambda` 表达式与其他表达式一样工作；就像数学表达式只是求值为一个数字、不会改变当前环境一样，`lambda` 表达式求值为一个函数，同样不会改变当前环境。让我们仔细看看。

|  | lambda | def |
| --- | --- | --- |
| 类型 | 求值为一个值的*表达式*。 | 改变环境的*语句*。 |
| 执行结果 | 创建一个没有内部名的匿名 lambda 函数。 | 创建一个带有内部名的函数，并把该名字绑定到当前环境中。 |
| 对环境的影响 | 求值 `lambda` 表达式*不会*创建或修改任何变量。 | 执行 `def` 语句既会创建新的函数对象，*又*会把一个名字绑定到当前环境中。 |
| 用法 | `lambda` 表达式可以用在任何需要表达式的地方，例如赋值语句中，或者调用表达式中的运算符或操作数。 | 执行 `def` 语句后，创建的函数被绑定到一个名字上。你可以在任何需要表达式的地方用这个名字来引用该函数。 |

#### 示例：`lambda`

```
# A lambda expression by itself does not alter
# the environment
lambda x: x * x

# We can assign lambda functions to a name
# with an assignment statement
square = lambda x: x * x
square(3)

# Lambda expressions can be used as an operator
# or operand
negate = lambda f, x: -f(x)
negate(lambda x: x * x, 3)
```

#### 示例：`def`

```
def square(x):
    return x * x

# A function created by a def statement
# can be referred to by its intrinsic name
square(3)
```

> [YouTube 视频：Lambda 表达式](https://youtu.be/vCeNq_P3akI?list=PLx38hZJ5RLZcUPWZ1-3HYsRPgZ8OCrvqz)

## 环境图

环境图是理解 `lambda` 表达式和高阶函数的最佳学习工具之一，因为你可以借此跟踪所有不同的名字、函数对象以及函数的参数。如果你在做下面的 WWPD 题目时卡住了，我们强烈建议你画环境图，或者使用 [Python tutor](https://tutor.cs61a.org)。想了解环境图应该长什么样，可以在 Python tutor 里运行一些代码看看。以下是相应规则：

### 赋值语句

1. 求值 `=` 号右侧的表达式。
2. 如果 `=` 左侧的名字在当前栈帧中还不存在，就把它写进去。如果已经存在，则擦除当前的绑定。把第 1 步得到的*值*绑定到这个名字上。

如果语句中有多个名字/表达式，请先从左到右求值所有表达式，然后再进行任何绑定。

> [Python Tutor 可视化：赋值语句](https://pythontutor.com/iframe-embed.html#code=x%20%3D%2010%0Ay%20%3D%20x%0Ax%20%3D%2020%0Ax,%20y%20%3D%20y%20%2B%201,%20x%20-%201&codeDivHeight=400&codeDivWidth=350&cumulative=true&curInstr=0&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D)

### `def` 语句

1. 画出函数对象，标注它的内部名、形参以及父栈帧。函数的父栈帧就是定义该函数时所在的栈帧。
2. 如果该函数的内部名在当前栈帧中还不存在，就把它写进去。如果已经存在，则擦除当前的绑定。把新创建的函数对象绑定到这个名字上。

> [Python Tutor 可视化：def 语句](https://pythontutor.com/iframe-embed.html#code=def%20f%28x%29%3A%0A%20%20%20%20return%20x%20%2B%201%0A%0Adef%20g%28y%29%3A%0A%20%20%20%20return%20y%20-%201%0A%0Adef%20f%28z%29%3A%0A%20%20%20%20return%20x%20*%202&codeDivHeight=400&codeDivWidth=350&cumulative=true&curInstr=0&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D)

### 调用表达式

> 注意：对于像 `max` 或 `print` 这样的 Python 内置函数，你不需要走这个流程。

1. 求值运算符，它的值应该是一个函数。
2. 从左到右求值操作数。
3. 打开一个新的栈帧。用顺序栈帧编号、函数的内部名以及它的父栈帧来标注它。
4. 把函数的形参绑定到你在第 2 步中求出值的实参上。
5. 在新环境中执行函数的函数体。

> [Python Tutor 可视化：调用表达式](https://pythontutor.com/iframe-embed.html#code=def%20f%28a,%20b,%20c%29%3A%0A%20%20%20%20return%20a%20*%20%28b%20%2B%20c%29%0A%0Adef%20g%28x%29%3A%0A%20%20%20%20return%203%20*%20x%0A%0Af%281%20%2B%202,%20g%282%29,%206%29&codeDivHeight=400&codeDivWidth=350&cumulative=true&curInstr=0&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D)

### Lambda

> *注意：*正如我们在上面的 `lambda` 表达式一节中所看到的，`lambda` 函数没有内部名。在环境图中画 `lambda` 函数时，它们被标注为名字 `lambda` 或者小写希腊字母 λ。当一个环境图中有多个 lambda 函数时，这可能会让人困惑，所以你可以通过给它们编号，或者写上它们被定义所在的行号来加以区分。

1. 画出 lambda 函数对象，用 λ、它的形参以及它的父栈帧来标注它。函数的父栈帧就是定义该函数时所在的栈帧。

这就是唯一的步骤。我们加入这一节，是为了强调 `lambda` 表达式与 `def` 语句之间的区别在于：`lambda` 表达式*不会*在环境中创建任何新的绑定。

> [Python Tutor 可视化：Lambda](https://pythontutor.com/iframe-embed.html#code=lambda%20x%3A%20x%20*%20x%20%23no%20binding%20created%0Asquare%20%3D%20lambda%20x%3A%20x%20*%20x%0Asquare%284%29%20%23calling%20a%20lambda%20function%0A&codeDivHeight=400&codeDivWidth=350&cumulative=true&curInstr=0&heapPrimitives=false&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

> [YouTube 视频：环境图](https://youtu.be/IPec2A7j2bY?list=PLx38hZJ5RLZcUPWZ1-3HYsRPgZ8OCrvqz)

# 必做题

## Python 会显示什么？

> **重要提示：**
> 对于所有 WWPD 题目，如果你认为答案是
> `<function...>`，就填 `Function`；如果会报错，就填 `Error`；如果什么都不显示，就填 `Nothing`。

### Q1: WWPD: 真相终将胜出

> 用 Ok 通过以下“Python 会显示什么？”题目来测试你的知识：
>
> ```
> python3 ok -q short-circuit -u
> ```

```
>>> True and 13
______
13

>>> False or 0
______
0

>>> not 10
______
False

>>> not None
______
True
```

```
>>> True and 1 / 0
______
Error (ZeroDivisionError)

>>> True or 1 / 0
______
True

>>> -1 and 1 > 0
______
True

>>> -1 or 5
______
-1

>>> (1 + 1) and 1
______
1

>>> print(3) or ""
______
3
''
```

```
>>> def f(x):
...     if x == 0:
...         return "zero"
...     elif x > 0:
...         return "positive"
...     else:
...         return ""
>>> 0 or f(1)
______
'positive'

>>> f(0) or f(-1)
______
'zero'

>>> f(0) and f(-1)
______
''
```

### Q2: WWPD: 高阶函数

> 用 Ok 通过以下“Python 会显示什么？”题目来测试你的知识：
>
> ```
> python3 ok -q hof-wwpd -u
> ```

```
>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
______
beets

>>> chocolate
______
Function

>>> chocolate()
______
sweets
'cake'

>>> more_chocolate, more_cake = chocolate(), cake
______
sweets

>>> more_chocolate
______
'cake'

>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
______
Function

>>> snake(10, 20)()
______
30

>>> cake = 'cake'
>>> snake(10, 20)
______
30
```

### Q3: WWPD: Lambda

> 用 Ok 通过以下“Python 会显示什么？”题目来测试你的知识：
>
> ```
> python3 ok -q lambda -u
> ```
>
>
>
> 提醒一下，下面两行代码在交互式 Python 解释器中执行时不会显示任何输出：
>
> ```
> >>> x = None
> >>> x
> >>>
> ```

```
>>> lambda x: x  # A lambda expression with one parameter x
______
<function <lambda> at ...>

>>> a = lambda x: x  # Assigning the lambda function to the name a
>>> a(5)
______
5

>>> (lambda: 3)()  # Using a lambda expression as an operator in a call expression.
______
3

>>> b = lambda x, y: lambda: x + y  # Lambdas can return other lambdas!
>>> c = b(8, 4)
>>> c
______
<function <lambda> at ...

>>> c()
______
12

>>> d = lambda f: f(4)  # They can have functions as arguments as well.
>>> def square(x):
...     return x * x
>>> d(square)
______
16
```

```
>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g)  # Which argument belongs to which function call?
______
Error

>>> higher_order_lambda(g)(2)
______
4

>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
______
3

>>> print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
>>> print_lambda
______
Function

>>> one_thousand = print_lambda(1000)
______
1000

>>> one_thousand # What did the call to print_lambda return?
______
# print_lambda returned None, so nothing gets displayed
```

## 编程练习

### Q4: 复合恒等函数

写一个函数，它接受两个单参数函数 `f` 和 `g`，并返回另一个**函数**，该函数有一个参数 `x`。如果 `f(g(x))` 等于 `g(f(x))`，返回的函数应返回 `True`，否则返回 `False`。你可以假设 `g(x)` 的输出是 `f` 的合法输入，反之亦然。

```
def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
    True
    >>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 测试你的代码：

```
python3 ok -q composite_identity
```

### Q5: Count Cond

考虑下面 `count_fives` 和 `count_primes` 的实现，它们使用了 `sum_digits` 和 `is_prime` 函数，这两个函数在下面给出：

```
def count_fives(n):
    """Return the number of values i from 1 to n (including n)
    where sum_digits(n * i) is 5.

    >>> count_fives(10)  # Among 10, 20, 30, ..., 100, only 50 (10 * 5) has digit sum 5
    1
    >>> count_fives(50)  # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4
    """
    i = 1
    count = 0
    while i <= n:
        if sum_digits(n * i) == 5:
            count += 1
        i += 1
    return count

def count_primes(n):
    """Return the number of prime numbers up to and including n.

    >>> count_primes(6)   # 2, 3, 5
    3
    >>> count_primes(13)  # 2, 3, 5, 7, 11, 13
    6
    """
    i = 1
    count = 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count
```

这两个实现看起来非常相似！通过编写一个函数 `count_cond` 来把这段逻辑泛化，它接受一个双参数的谓词函数 `condition(n, i)`。`count_cond` 返回一个单参数函数，该函数接受 `n`，并统计从 1 到 `n` 中所有在调用时满足 `condition` 的数。

> **注意：**
> 当我们说 `condition` 是谓词函数时，我们的意思是它是一个会返回 `True` 或 `False` 的函数。

```
def sum_digits(y):
    """Return the sum of the digits of non-negative integer y."""
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total

def is_prime(n):
    """Return whether positive integer n is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to n that satisfy the two-argument predicate function Condition, where
    the first argument for condition is n and the second argument is the
    number from 1 to n.

    >>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
    >>> count_fives(10)   # 50 (10 * 5)
    1
    >>> count_fives(50)   # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4

    >>> is_i_prime = lambda n, i: is_prime(i) # need to pass 2-argument function into count_cond
    >>> count_primes = count_cond(is_i_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 测试你的代码：

```
python3 ok -q count_cond
```

# 环境图练习

**这一部分没有 Gradescope 提交。**

不过，我们仍然鼓励你在纸上完成这道题，以熟悉环境图——它可能会以另一种形式出现在考试中。

### Q6: 高阶函数环境图练习

在纸上或白板上画出执行下面代码后得到的环境图。使用 [tutor.cs61a.org](https://tutor.cs61a.org) 来检查你的答案。

```
n = 7

def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)

f = f(g, n)
g = (lambda y: y())(f)
```

## 在本地检查得分

你可以通过运行以下命令，在本地检查你在这份作业每道题上的得分：

```
python3 ok --score
```

**这不会提交作业！** 当你对自己的得分满意后，把作业提交到 Gradescope 以取得相应学分。

# 提交作业

把你编辑过的任何文件上传**到对应的 Gradescope 作业**中来提交这份作业。[Lab 00](https://lr2933.github.io/cs61a-spring-2026/lab/lab00.html#submitting-the-assignment) 中有详细说明。

正确完成所有题目值 1 分。如果你参加的是常规实验课，你还需要助教记录你的出勤才能拿到这 1 分。请在离开前确认助教已经记录了你的出勤。

# 选做题

> 这些题目是选做的。如果你没有完成它们，
> 你仍然会获得这份作业的学分。它们是很好的练习，所以还是做一做吧！

### Q7: Multiple

写一个函数，接受两个正整数，并返回同时是二者倍数的最小正整数。

```
def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 测试你的代码：

```
python3 ok -q multiple
```

### Q8: 我听说你喜欢函数……

定义一个函数 `cycle`，它接受三个函数 `f1`、`f2` 和 `f3` 作为参数。`cycle` 将返回另一个函数 `g`，而 `g` 应接受一个整数参数 `n`，并返回另一个函数 `h`。最终的这个函数 `h` 应接受一个参数 `x`，并根据 `n` 的值，循环地把 `f1`、`f2` 和 `f3` 依次应用到 `x` 上。下面列出了对于几个 `n` 值，最终的函数 `h` 应对 `x` 做什么：

- `n = 0`，返回 `x`
- `n = 1`，把 `f1` 应用到 `x` 上，即返回 `f1(x)`
- `n = 2`，把 `f1` 应用到 `x` 上，再把 `f2` 应用到上一步的结果上，即返回 `f2(f1(x))`
- `n = 3`，把 `f1` 应用到 `x` 上，把 `f2` 应用到应用 `f1` 的结果上，再把 `f3` 应用到应用 `f2` 的结果上，即 `f3(f2(f1(x)))`
- `n = 4`，重新开始循环，依次应用 `f1`、`f2`、`f3`，然后再应用一次 `f1`，即 `f1(f3(f2(f1(x))))`
- 以此类推。

> **提示：** 大部分工作都在最内层的函数里完成。
>
> **提示：** 你如何利用 `%` 运算符来实现循环行为？
> 试着计算所有从 0 到 12 的整数 `n` 的 `n % 3`。你注意到了什么规律？

```
def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
```

用 Ok 测试你的代码：

```
python3 ok -q cycle
```
