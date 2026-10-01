Lab 4: Tree Recursion, Data Abstraction | CS 61A Spring 2026



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



Lab 4: Tree Recursion, Data Abstraction

* [lab04.zip](lab04.zip "lab04.zip")
=============================================================================

*截止时间为 2 月 25 日（周三）晚上 11:59。*

Starter Files
-------------

下载 [lab04.zip](lab04.zip "lab04.zip")。

Attendance
==========

如果你参加的是常规 61A lab，你的 TA 会过来为你 check in。你除了到场之外，还需要提交 lab problems，才能获得本次 lab 的学分。如果你参加的是 mega lab，那么只需提交 lab problems 即可获得学分。

如果你因为正当理由（例如生病或时间冲突）缺席 lab，或者因为某些原因没有被 check in，只需在两周内填写[此表单](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance")即可获得 attendance 学分。

Required Questions
==================

Dictionaries
------------

如果你需要复习 dictionaries，请查阅下拉框。你也可以直接跳到题目部分，遇到困难时再回到这里查阅。

Dictionaries (enable JavaScript)

A dictionary 包含 key-value pairs，并允许通过方括号用 key 来查找 value。每个 key 必须是唯一的。

```
>>> d = {2: 4, 'two': ['four'], (1, 1): 4}
>>> d[2]
4
>>> d['two']
['four']
>>> d[(1, 1)]
4
```

keys、values 或 key-value pairs 的 sequence 可以分别用 `.keys()`、`.values()` 或 `.items()` 访问。

```
>>> for k in d.keys():
...     print(k)
...
2
two
(1, 1)
>>> for v in d.values():
...     print(v)
...
4
['four']
4
>>> for k, v in d.items():
...     print(k, v)
...
2 4
two ['four']
(1, 1) 4
```

默认情况下，遍历一个 dictionary 就是遍历它的 keys。

```
>>> for x in d:
...     print(x)
...
2
two
(1, 1)
```

你可以用 `in` 检查一个 dictionary 是否包含某个 key：

```
>>> 'two' in d
True
>>> 4 in d
False
```

试图访问 dictionary 中不存在的 key 会导致错误。你可以使用 `.get(<key>, <default>)`，它返回 dictionary 中 `<key>` 对应的 value，如果不存在则返回 `<default>`。

```
>>> d[3]
KeyError: 3
>>> d.get(3, "fun")
"fun"
>>> d.get(2, "fun")
4
```

dictionary 的内容可以用 `=` 修改：

```
>>> d
{2: 4, 'two': ['four'], (1, 1): 4}
>>> d[(1, 1)] = "61a"
>>> d[(1, 1)]
'61a'
```

A dictionary comprehension 是一个求值为新 dictionary 的表达式。

```
>>> {3*x: 3*x + 1 for x in range(2, 5)}
{6: 7, 9: 10, 12: 13}
```

  
> **重要：**
> 对于所有 WWPD 题目，如果你认为答案是
> `<function...>`，请输入 `Function`；如果会报错，请输入 `Error`；如果没有显示任何内容，请输入 `Nothing`。
>
> ### Q1: Dictionaries
>
> 使用 Ok 来通过以下 "What Would Python Display?" 题目检验你的理解：
>
> ```
> python3 ok -q pokemon -u
>
> Copy
>
> ✂️
> ```

```
>>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
>>> pokemon['pikachu']

______



25

>>> len(pokemon)

______



3

>>> 'mewtwo' in pokemon

______



False

>>> 'pikachu' in pokemon

______



True

>>> 25 in pokemon

______



False

>>> 148 in pokemon.values()

______



True

>>> 151 in pokemon.keys()

______



False

>>> 'mew' in pokemon.keys()

______



True
```

Toggle Solution (enable JavaScript)

### Q2: Divide

实现 `divide`，它接收两个正整数 list `quotients` 和 `divisors`。它返回一个 dictionary，其 keys 是 `quotients` 的 elements。对于每个 key `q`，其对应的 value 是所有能被 `q` 整除的 `divisors` elements 组成的 list。

> 提示：每个 key 的 value 需要是一个 list，所以这里 list comprehension 可能很有用。

```
def divide(quotients: list[int], divisors: list[int]) -> dict[int, list[int]]:
    """Return a dictonary in which each quotient q is a key for the list of
    divisors that it divides evenly.

    >>> divide([3, 4, 5], [8, 9, 10, 11, 12])
    {3: [9, 12], 4: [8, 12], 5: [10]}
    >>> divide(list(range(1, 5)), list(range(20, 25)))
    {1: [20, 21, 22, 23, 24], 2: [20, 22, 24], 3: [21, 24], 4: [20, 24]}
    """
    return {____: ____ for ____ in ____}
```

使用 Ok 来测试你的代码：

```
python3 ok -q divide

Copy

✂️
```

  

### Q3: Buying Fruit

实现 `buy` function，它接收三个参数：

1. `fruits_to_buy`：一个 strings list，表示你需要买的水果。*每种水果至少必须买一个。*
2. `prices`：一个 dictionary，keys 是水果名（strings），values 是表示每种水果价格的正整数。
3. `total_amount`：一个 integer，表示可用于购买水果的总金额。
   关于输入结构的更多细节，请查看 docstring。

这个 function 应打印出购买所需水果的**所有可能方式**，使得总价正好等于 `total_amount`。你只能选择 `fruits_to_buy` list 中提到的水果。

> **注意**：你可以使用 `display` function 来格式化输出。对每种水果及其对应数量调用 `display(fruit, count)`，即可生成一个表示所购水果种类和数量的 string。

> **提示**：如何确保每一种组合都至少包含 `fruits_to_buy` 中列出的每种水果各一个？

```
def buy(fruits_to_buy: list[str], prices: dict[str, int], total_amount: int) -> None:
    """Print ways to buy some of each fruit so that the sum of prices is amount.

    >>> prices = {'oranges': 4, 'apples': 3, 'bananas': 2, 'kiwis': 9}
    >>> buy(['apples', 'oranges', 'bananas'], prices, 12)  # We can only buy apple, orange, and banana, but not kiwi
    [2 apples][1 orange][1 banana]
    >>> buy(['apples', 'oranges', 'bananas'], prices, 16)
    [2 apples][1 orange][3 bananas]
    [2 apples][2 oranges][1 banana]
    >>> buy(['apples', 'kiwis'], prices, 36)
    [3 apples][3 kiwis]
    [6 apples][2 kiwis]
    [9 apples][1 kiwi]
    """
    def add(fruits: list[str], amount: int, cart: str) -> None:
        if fruits == [] and amount == 0:
            print(cart)
        elif fruits and amount > 0:
            fruit = fruits[0]
            price = ____
            for k in ____:
                # Hint: The display function will help you add fruit to the cart.
                add(____, ____, ____)
    add(fruits_to_buy, total_amount, '')

def display(fruit: str, count: int) -> str:
    """Display a count of a fruit in square brackets.

    >>> display('apples', 3)
    '[3 apples]'
    >>> display('apples', 1)
    '[1 apple]'
    >>> print(display('apples', 3) + display('kiwis', 3))
    [3 apples][3 kiwis]
    """
    assert count >= 1 and fruit[-1] == 's'
    if count == 1:
        fruit = fruit[:-1]  # get rid of the plural s
    return '[' + str(count) + ' ' + fruit + ']'
```

使用 Ok 来测试你的代码：

```
python3 ok -q buy

Copy

✂️
```

  

Data Abstraction
----------------

如果你需要复习 data abstraction，请查阅下拉框。你也可以直接跳到题目部分，遇到困难时再回到这里查阅。

Data Abstraction (enable JavaScript)

A *data abstraction* 是一组用于组合和分解 compound values 的 functions。其中一个称为 *constructor* 的 function 把两个或多个部分组合成一个整体（例如一个 rational number；也叫 fraction），其他称为 *selectors* 的 functions 则返回这个整体的各个部分（例如 numerator 或 denominator）。

```
def rational(n, d):
    "Return a fraction n / d for integers n and d."

def numer(r):
    "Return the numerator of rational number r."

def denom(r):
    "Return the denominator of rational number r."
```

关键在于，人们可以在不知道这些 functions 如何实现的情况下使用一个 data abstraction。例如，我们（人类）只要知道 `rational`、`numer` 和 `denom` 做什么，而不必知道它们如何实现，就能验证 `mul_rationals` 实现得是否正确。

```
def mul_rationals(r1, r2):
    "Return the rational number r1 * r2."
    return rational(numer(r1) * numer(r2), denom(r1) * denom(r2))
```

然而，要让 Python 运行程序，data abstraction 需要一个实现。使用关于实现的知识就是跨越 abstraction barrier，这道屏障把程序中依赖于 data abstraction 实现的部分与不依赖于它的部分隔开。一个写得好的程序通常会尽量减少依赖于实现的代码量，这样以后修改实现时就不需要重写太多代码。

在使用别人提供的 data abstraction 时，请让你的程序即使在该 data abstraction 的实现发生变化时也依然正确。

### Cities

假设我们有一个针对 cities 的 data abstraction。一个 city 有名字、latitude 坐标和 longitude 坐标。

我们的 data abstraction 有一个 **constructor**：

* `make_city(name, lat, lon)`：用给定的 name、latitude 和 longitude 创建一个 city object。

我们还有以下 **selectors**，用于获取每个 city 的信息：

* `get_name(city)`：返回该 city 的 name
* `get_lat(city)`：返回该 city 的 latitude
* `get_lon(city)`：返回该 city 的 longitude

下面是我们如何使用 constructor 和 selectors 来创建 cities 并提取它们的信息：

```
>>> berkeley = make_city('Berkeley', 122, 37)
>>> get_name(berkeley)
'Berkeley'
>>> get_lat(berkeley)
122
>>> new_york = make_city('New York City', 74, 40)
>>> get_lon(new_york)
40
```

如果你好奇所有这些 selector 和 constructor functions 是如何实现的，可以在 lab 文件里找到。不过，data abstraction 的意义就在于，在编写关于 cities 的程序时，我们并不需要知道其实现。

### Q4: Distance

我们现在来实现 `distance` function，它计算两个 city objects 之间的距离。回想一下，两个坐标对 `(x1, y1)` 和 `(x2, y2)` 之间的距离可以通过计算 `(x1 - x2)**2 + (y1 - y2)**2` 的 `sqrt` 得到。为了方便，我们已经为你 import 了 `sqrt`。把 city 的 latitude 和 longitude 当作它的坐标；你需要用 selectors 来获取这些信息！

```
from math import sqrt
def distance(city_a, city_b):
    """
    Returns the distance between city_a and city_b according to their
    coordinates.

    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q distance

Copy

✂️
```

  

### Q5: Closer City

接下来实现 `closer_city`，这个 function 接收一个 latitude、一个 longitude 和两个 cities，并返回距离给定 latitude 和 longitude 更近的那个 city 的 *name*。

在这道题中，你只可以使用 selectors `get_name`、`get_lat`、`get_lon`，constructor `make_city`，以及你刚刚定义的 `distance` function。

> **提示**：你如何用 `distance` function 求出给定位置与各个给定 city 之间的距离？

```
def closer_city(lat, lon, city_a, city_b):
    """
    Returns the name of either city_a or city_b, whichever is closest to
    coordinate (lat, lon). If the two cities are the same distance away
    from the coordinate, consider city_b to be the closer city.

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"
```

使用 Ok 来测试你的代码：

```
python3 ok -q closer_city

Copy

✂️
```

  

### Q6: Don't violate the abstraction barrier!

> 注意：
> 这道题没有需要写代码的部分
> （前提是你前两道题实现正确）。

在编写使用 data abstraction 的 functions 时，我们应尽可能使用 constructor(s) 和 selector(s)，而不是假定 data abstraction 的实现。依赖 data abstraction 的底层实现被称为*违反 abstraction barrier*。

即使你违反了 abstraction barrier，也有可能通过了前几道题的 doctests。要检查你是否违反了，请运行以下命令：

使用 Ok 来测试你的代码：

```
python3 ok -q check_city_abstraction

Copy

✂️
```

  

`check_city_abstraction` function 只存在于这个 doctest 中，它把原 abstraction 的实现换成别的东西，运行前两部分中的测试，然后恢复原来的 abstraction。

abstraction barrier 的本质保证了：只要 constructors 和 selectors 使用得当，改变一个 data abstraction 的实现不应影响任何使用该 data abstraction 的程序的功能。

如果你通过了前几道题的 Ok 测试，但没通过这道题，修复很简单！只要把任何违反 abstraction barrier 的代码替换成合适的 constructor 或 selector 即可。

在继续之前，请确保你的 functions 在 data abstraction 的第一种和第二种实现下都能通过测试，并且你理解为什么它们在两种实现下都应该能工作。

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

+ [Dictionaries](index.html#dictionaries "index.html#dictionaries")

- [Q1: Dictionaries](index.html#q1-dictionaries "index.html#q1-dictionaries")
- [Q2: Divide](index.html#q2-divide "index.html#q2-divide")
- [Q3: Buying Fruit](index.html#q3-buying-fruit "index.html#q3-buying-fruit")

+ [Data Abstraction](index.html#data-abstraction "index.html#data-abstraction")

- [Cities](index.html#cities "index.html#cities")
- [Q4: Distance](index.html#q4-distance "index.html#q4-distance")
- [Q5: Closer City](index.html#q5-closer-city "index.html#q5-closer-city")
- [Q6: Don't violate the abstraction barrier!](index.html#q6-don-t-violate-the-abstraction-barrier "index.html#q6-don-t-violate-the-abstraction-barrier")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
