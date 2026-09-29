Computer Aided Typing Software | CS 61A Spring 2026



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



Computer Aided Typing Software

* [cats.zip](cats.zip "cats.zip")
=================================================================

![](images/cats_typing_still.gif)
> 程序员梦寐以求：  
> Abstraction、recursion，还有  
> 打字飞快。

Introduction
------------

> **重要的提交说明：** 要拿到全部学分：
>
> * 在 **02/26（周四）** 之前提交，Phase 1 和 Phase 2 完成，值 1 分。
> * 在 **03/05（周四）** 之前提交，所有 phase 完成。
>
> 请尽量按顺序尝试题目并运行 `ok` 测试，因为后面的一些题目会依赖于前面题目的正确实现。
>
> 整个 project 可以和一位 partner 一起完成。这里有关于
> [pair programming](https://c88c.org/sp25/articles/pair-programming "https://c88c.org/sp25/articles/pair-programming") 以及
> 使用 [VS Code](https://c88c.org/sp25/articles/vscode/#pair-programming "https://c88c.org/sp25/articles/vscode/#pair-programming")
> 进行远程协作的指引。
>
> 如果在 **03/04（周三）** 之前提交整个 project，可以获得 1 个 bonus point。

在这个 project 中，你将编写一个测量打字速度的程序。此外，你还会实现 typing autocorrect，这是一个在用户打完一个单词后尝试纠正其拼写的功能。这个 project 的灵感来自 [typeracer](https://play.typeracer.com/ "https://play.typeracer.com/")。

Final Product
-------------

我们的 staff solution 可以在这里交互体验：
[cats.cs61a.org](https://cats.cs61a.org "https://cats.cs61a.org")。
现在就可以随意试试。
当你完成这个 project 时，你将亲手实现其中相当大的一部分，包括 multiplayer 模式！

Download Starter Files
----------------------

你可以把项目所有代码作为 [zip archive](cats.zip "cats.zip") 下载。这个 project 包含若干文件，*但你只需要修改* `cats.py`。以下是压缩包中包含的文件：

* `cats.py`：typing test 的逻辑。
* `utils.py`：用于处理文件和字符串的 utility functions。
* `ucb.py`：CS 61A projects 的 utility functions。
* `data/sample_paragraphs.txt`：用于打字的文本样本。
  这些是从 Wikipedia 上
  [抓取](https://github.com/kavigupta/wikivideos/blob/626de521e04ca643751ed85d549faca6ea528b1d/get_corpus.py "https://github.com/kavigupta/wikivideos/blob/626de521e04ca643751ed85d549faca6ea528b1d/get_corpus.py")
  来的、关于各种主题的文章。
* `data/common_words.txt`：常见的
  [按词频排序的英语单词](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears.txt "https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears.txt")。
* `data/words.txt`：更多
  [按词频排序的英语单词](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears.txt "https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears.txt")。
* `data/final_diff_words.txt`：还要更多的英语单词！
* `data/testcases.out`：可选的 Final Diff 扩展的测试用例。
* `cats_gui.py`：用于基于网页的图形用户界面（GUI）的 web server。
* `gui_files`：图形用户界面（GUI）所需的文件目录。
* `multiplayer`：支持 multiplayer 模式所需的文件目录。
* `favicons`：图标目录。
* `images`：图片目录。
* `ok`、`cats.ok`、`tests`：测试文件。
* `score.py`：可选的 Final Diff 扩展的一部分。

Logistics
---------

这个 project 值 20 分。
其中 19 分是 correctness，
1 分是在 checkpoint 截止日期前提交 Phase 1 & 2。

你需要交以下文件：

* `cats.py`

完成这个 project 不需要修改或提交任何其他文件。要提交 project，**请把所需文件提交到对应的 Gradescope 作业。**

你不可以使用人工智能工具来帮助完成这个 project，也不可以参考网上找到的解答。

对于要求你完成的 functions，我们可能提供了一些初始代码。如果你不想用这些代码，可以随意删除并从头开始。你也可以按需添加新的 function 定义。

**但是，请不要修改任何其他 functions，也不要编辑上面未列出的任何文件**。这样做可能会导致你的代码无法通过我们的 autograder 测试。另外，请不要更改任何 function 签名（名字、参数顺序或参数个数）。

在整个 project 中，你应该测试代码的正确性。经常测试是好习惯，这样更容易定位问题。不过，也不要测试得*太*频繁，要给自己留出思考问题的时间。

我们提供了一个名为 `ok` 的 **autograder**，帮助你测试代码并跟踪进度。第一次运行 autograder 时，它会要求你**用浏览器登录你的 Ok 账号**。请照做。每次运行 `ok` 时，它都会把你的工作和进度备份到我们的服务器上。

`ok` 的主要用途是测试你的实现。




















如果你想交互式地测试代码，可以运行

```
 python3 ok -q [question number] -i
```

把相应的题号（例如 `01`）填进去。
这会运行该题的测试，直到你失败的第一题为止，然后给你机会交互式地测试你写的 functions。

你也可以使用 OK 的调试打印功能，只要在 print 语句前加上 "DEBUG:" 前缀即可。例如，如果你想查看变量 `x` 的值，可以写：

```
 print(f"DEBUG: x is {x}")
```

这样会在终端产生输出，而不会因为多余的输出导致 OK 测试失败。


Phase 1: Typing
===============

> **提醒**：在整个 project 中，我们只会修改 `cats.py` 里的 functions。
>
> **Type Checking**
> 开始 project 之前，请确认你已启用 type checking！参见[这里](../../lab/lab03/index.html#type-checking "../../lab/lab03/index.html#type-checking")。

### Problem 1 (1 pt)

实现 `pick`。这个 function 选择用户在 typing test 中要打的段落。它接收三个参数：

* `paragraphs`：潜在段落（strings）的 list
* `select`：一个 function，对某个段落求值，若满足某些条件返回 `True`，否则返回 `False`
* `k`：一个非负 integer，表示在所有满足条件的段落中、想要的那个段落的 index

`pick` function 返回 `paragraphs` 中第 `k` 个使 `select` function 返回 `True` 的段落。如果不存在这样的段落（因为 `k` 大于或等于满足条件的段落数量），那么 `pick` 返回空字符串。

> **提示**：
> 不用担心 `select` function 的具体实现。只需假设它接收一个段落作为输入，并
> 返回 `True` 或 `False`。
> **提醒**：Indexing 从 0 开始。如果 `k` 是 0，我们要选的是*第一个*满足条件的段落。

在写任何代码之前，先解锁测试以验证你对题目的理解：

```
python3 ok -q 01 -u

Copy

✂️
```

  

解锁完成后，开始实现你的解法。你可以用以下命令检查正确性：

```
python3 ok -q 01

Copy

✂️
```

  

### Problem 2 (1 pt)

实现 `about` function，它接收一个名为 `keywords` 的 words list。它返回一个 function，该 function 在给定一个段落时，检查该段落是否包含 `keywords` 中的任何 words。如果 `keywords` list 中有任何 words 出现在该段落中，返回的 function 返回 `True`，否则返回 `False`。

一旦实现了 `about`，我们就可以把它返回的 function 作为 `pick` 中的 `select` 参数使用。这很有用，因为它让我们可以根据段落是否包含传给 `about` function 的 keywords list 中的任何 words 来筛选段落。随着我们继续开发 typing test，这个功能会很有用。

为了确保比较准确，你需要：

1. 忽略大小写（把大写字母和小写字母视为等同）。
2. 忽略段落中的标点。
3. 只检查 `keywords` list 中的 words 的精确匹配，而不是子串。
   例如，`paragraph` 中出现的 "dogs" 不应匹配 `keywords` 中的 "dog"。

> **提示**：
> 使用 `utils.py` 中的 `split`、`lower` 和 `remove_punctuation` functions。

在写任何代码之前，先解锁测试以验证你对题目的理解：

```
python3 ok -q 02 -u

Copy

✂️
```

  

解锁完成后，开始实现你的解法。你可以用以下命令检查正确性：

```
python3 ok -q 02

Copy

✂️
```

  

### Problem 3 (2 pts)

实现 `accuracy`，它接收一个 `entered` 段落和一个 `source` 段落。它返回 `entered` 中与 `source` 中对应 words 完全匹配的 words 的百分比。大小写和标点也须匹配。"对应" 意味着 `entered` 中的每个 word 必须出现在与 `source` 中匹配 word 相同的位置。换句话说，`entered` 中的第一个 word 必须匹配 `source` 中的第一个 word，`entered` 中的第二个 word 必须匹配 `source` 中的第二个 word，依此类推。

在此语境下，一个 *word* 是由空白字符与其他 words 分隔开的任意字符序列。因此，把像 "dog;" 这样的序列当作一个 word。

在实际的 typing test 中，`entered` 表示玩家打出的内容，`source` 是他们试图复制的段落。

* 如果 `entered` 比 `source` 长，那么 `entered` 中那些在 `source` 里没有对应 word 的多余 words 全都*不正确*。
* 如果 `entered` 比 `source` 短，且 `entered` 中的所有 words 到目前为止都与 `source` 对应，那么 accuracy 是 100.0。
* 如果 `entered` 为空且 `source` 为空，那么 accuracy 是 100.0。
* 如果 `entered` 为空但 `source` 不为空，那么 accuracy 是 0.0。
* 如果 `entered` 不为空但 `source` 为空，那么 accuracy 是 0.0。

在写任何代码之前，先解锁测试以验证你对题目的理解：

```
python3 ok -q 03 -u

Copy

✂️
```

  

解锁完成后，开始实现你的解法。你可以用以下命令检查正确性：

```
python3 ok -q 03

Copy

✂️
```

  

### Problem 4 (1 pt)

实现 `wpm`，它计算 *words per minute*，一个衡量打字速度的指标，给定一个 string `entered` 和以**秒**为单位的 `elapsed` 时间。尽管名字如此，*words per minute* 并不是基于打出的 words 数量，而是基于 5 个字符一组的组数，这样 typing test 就不会因为 words 的长度而产生偏差。*words per minute* 的计算公式是：把打出的字符总数（包括空格）除以 5（平均 word 长度），然后把结果除以以**分钟**为单位的 elapsed time。

例如，string `"I am glad!"` 包含十个字符（不包括引号）。words per minute 的计算使用 2 作为输入的 words 数（因为 10 / 5 = 2）。如果某人在 30 秒（半分钟）内打出这个 string，他们的速度就是 4 words per minute。

在写任何代码之前，先解锁测试以验证你对题目的理解：

```
python3 ok -q 04 -u

Copy

✂️
```

  

解锁完成后，开始实现你的解法。你可以用以下命令检查正确性：

```
python3 ok -q 04

Copy

✂️
```

  

**是时候测试你的打字速度了！** 你可以用命令行在关于某个特定主题的段落上测试你的打字速度。例如，下面的命令会加载关于 cats 或 kittens 的段落。如果你好奇，可以去看 `run_typing_test` function 的实现（不过它是已经为你写好的）。

```
python3 cats.py -t cats kittens
```

你也可以用下面的命令试试基于网页的图形用户界面（GUI）。（在浏览器里关闭标签页之后，你可能需要在终端用 `Ctrl+C` 或 `Cmd+C` 退出 GUI）。

```
python3 cats_gui.py
```

Phase 2: Autocorrect
====================

在基于网页的 GUI 中，有一个 "Enable Auto-Correct" 选项，但现在它还什么都不做。让我们来实现自动拼写纠正。每当用户按下空格键时，如果用户打出的最后一个 word 在 dictionary 中找不到匹配，但与其中某个 word 很接近，那么那个相似的 word 会被替换为用户打出的内容。

### Problem 5 (2 pts)

实现 `autocorrect`，它接收一个 `entered_word`、一个 `word_list`、一个 `diff_function` 和一个 `limit`。`autocorrect` 的目标是返回 `word_list` 中与给定的 `entered_word` 最接近的 word，接近程度由 `diff_function` 判定。

具体来说，`autocorrect` 做以下事情：

* 如果 `entered_word` 包含在 `word_list` 中，`autocorrect`
  返回那个 word。
* 否则，`autocorrect` 返回 `word_list` 中与给定的 `entered_word`
  差异最小的 word。
  这个差异就是 `diff_function` 返回的数字。
* 然而，如果 `entered_word` 与 `word_list` 中任何 word 的最小差异
  大于 `limit`，那么就改为返回 `entered_word`。
  换句话说，`limit` 设置了一个阈值上限，规定一个 typo 要多严重才仍然可以被纠正。

假设 `entered_word` 和 `word_list` 的所有 elements 都是小写且没有标点。

> **重要**：
> 如果 `word_list` 中有多个 strings 与 `entered_word` 的差异并列最小，
> `autocorrect` 应返回在 `word_list` 中出现
> 最早（index 最小）的那个 string。

一个 diff function 接收三个参数。第一个是 `entered_word`，第二个是 source word（在这里就是 `word_list` 中的一个 word），第三个参数是 `limit`。diff function 的输出是一个数字，表示两个 strings 之间的差异程度。

下面是一个 diff function 的例子，它计算 `1 + limit` 和两个输入 strings 的长度差中的较小值：

```
>>> def length_diff(w1, w2, limit):
...     return min(limit + 1, abs(len(w2) - len(w1)))
>>> length_diff('mellow', 'cello', 10)
1
>>> length_diff('hippo', 'hippopotamus', 5)
6
```

> **注意**：
> 为了简洁，一些解锁测试在定义 lambda function 时使用了 ternary operator。ternary operator 就是 `if` statement 的单行版本。
>
> 例如，在其中一个 ok 测试中，我们把 diff function 定义为 `first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0`。
> 这里，如果 `w1` 和 `w2` 的第一个字符不同，lambda function 返回 1，否则返回 0。

下面是实现 `autocorrect` 的一个有用提示：

> **注意**：
> 可选地，如果想写一行解法，可以试试使用带可选 `key` 参数（它接收一个单参数 function）的 `max` 或 `min`。
> 例如，`max([-7, 2, -1], key=abs)` 会返回 `-7`，因为 `abs(-7)` 大于 `abs(2)` 和 `abs(-1)`。

在写任何代码之前，先解锁测试以验证你对题目的理解：

```
python3 ok -q 05 -u

Copy

✂️
```

  

解锁完成后，开始实现你的解法。你可以用以下命令检查正确性：

```
python3 ok -q 05

Copy

✂️
```

  

### Problem 6 (3 pts)

实现 `furry_fixes`，一个可以传给 `autocorrect` 中 `diff_function` 参数的 diff function。这个 function 接收两个 strings，并返回为了把 `entered` word 转换成 `source` word 所需修改的最少字符数。如果两个 strings 长度不相等，长度差会被加到总修改数上。

以下是一些例子：

```
>>> big_limit = 10
>>> furry_fixes("nice", "rice", big_limit)    # Substitute: n -> r
1
>>> furry_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
2
>>> furry_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
3
>>> furry_fixes("goodbye", "good", big_limit) # Don't substitute anything, length difference of 3.
3
>>> furry_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
5
>>> furry_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
5
```

> **重要**：
> 你的实现中不可以使用 `while`、`for` 或 list comprehensions。
> 请使用 recursion。

如果必须修改的字符数大于 `limit`，那么 `furry_fixes` 应返回任何大于 `limit` 的数字，并且应尽量减少为此所需的计算量。

> 为什么要有 limit？从 Problem 5 我们知道，`autocorrect` 会拒绝任何与 `entered` word
> 差异大于 `limit` 的 `source` word。差异比 `limit` 大 1 还是大 100
> 都无所谓；autocorrect 一样会拒绝它。因此，一旦我们知道差异超过 `limit`，
> 停止递归调用就是合理的，这样可以节省时间，
> 即使返回的差异不会完全准确。
>
> 以下两次 `furry_fixes` 调用求值所需的时间应该差不多：
>
> ```
> >>> limit = 4
> >>> furry_fixes("roses", "arose", limit) > limit
> True
> >>> furry_fixes("rosesabcdefghijklm", "arosenopqrstuvwxyz", limit) > limit
> True
> ```

为了确保你确实通过到达 `limit` 后停止递归来节省时间，有一个 autograder 测试会根据你的解法所做的 function 调用次数来衡量其性能。如果你没通过这个测试，考虑添加一个与 `limit` 相关的 base case。

> **提示**：解决这道题你需要不止一个 base case。

String Slicing (enable JavaScript)

A string 是字符的 sequence。（字母、数字和标点都是字符。）A string 的 slice 是另一个 string，包含原 string 的部分字符。以下是一些例子：

```
>>> a = 'strap'
>>> a[0]
's'
>>> a[1:]
'trap'
>>> a[2:]
'rap'
>>> a[1:][1:]
'rap'
```

在写任何代码之前，先解锁测试以验证你对题目的理解：

```
python3 ok -q 06 -u

Copy

✂️
```

  

解锁完成后，开始实现你的解法。你可以用以下命令检查正确性：

```
python3 ok -q 06

Copy

✂️
```

  

试试在 GUI 中启用 auto-correct。它是否帮你打得更快？纠正是否准确？

### Problem 7 (3 pts)

实现 `minimum_mewtations`，一个更高级的 diff function，可用于 `autocorrect`，它返回把 `entered` word 转换成 `source` word 所需的*最少*编辑操作数。

有三种编辑操作，举例如下：

1. 向 `entered` 添加一个字母。

   * 向 `"itten"` 添加 `"k"` 得到 `"kitten"`。
2. 从 `entered` 中删除一个字母。

   * 从 `"scat"` 中删除 `"s"` 得到 `"cat"`。
3. 把 `entered` 中的一个字母替换为另一个。

   * 把 `"zaguar"` 中的 `"z"` 替换为 `"j"` 得到 `"jaguar"`。

每次编辑操作会使两个 words 之间的差异增加 1。

```
>>> big_limit = 10
>>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
2
>>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
2
>>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
3
```

我们在 `cats.py` 中提供了一个实现模板。你可以随意修改这个模板，也可以完全删掉它。

> **提示：**
> `minimum_mewtations` 中的其中一个 recursive call 会和 `furry_fixes` 类似。
> 不过，因为 `minimum_mewtations` 考虑三种*具体*类型的编辑（add、remove、substitute），
> 所以需要有额外的 recursive calls 来分别处理这些情况。

如果所需的编辑次数大于 `limit`，那么 `minimum_mewtations` 应返回**任何**大于 `limit` 的数字（例如 `limit + 1`），并且一旦到达 limit 就应停止递归调用以节省时间。

> 以下两次 `minimum_mewtations` 调用求值所需的时间应该差不多：
>
> ```
> >>> limit = 2
> >>> minimum_mewtations("ckiteus", "kittens", limit) > limit
> True
> >>> minimum_mewtations("ckiteusabcdefghijklm", "kittensnopqrstuvwxyz", limit) > limit
> True
> ```

为了确保你的代码在到达 `limit` 后停止递归调用，有一个 autograder 测试会根据你的解法所做的 function 调用次数来衡量其性能。

> **重要**：
> 在你的 `minimum_mewtations` 实现中，*不应该*使用任何 helper functions。否则 autograder 测试可能会失败。
>
> **重要**：
> 当你准备好测试你的实现时，记得删除下面这行代码：
>
> ```
> assert False, 'Remove this line'
> ```

在写任何代码之前，先解锁测试以验证你对题目的理解：

```
python3 ok -q 07 -u

Copy

✂️
```

  

解锁完成后，开始实现你的解法。你可以用以下命令检查正确性：

```
python3 ok -q 07

Copy

✂️
```

  

试着启用 auto-correct 再打一次字。纠正是否更准确了？

```
python3 cats_gui.py
```

### (Optional) Extension: Final Diff (0 pts)

你可以选择设计自己的 diff function，名为 `final_diff`。以下是一些让纠正更准确的想法：

* 考虑哪些 additions 和 deletions 比其他更可能出现。
  例如，如果一个字母连续出现两次，你就更有可能不小心漏掉它。
* 把两个位置互换的相邻字母视为一次修改，而不是两次。
* 尝试把常见的拼写错误纳入考虑。
* 键盘上位置相近的字母更常被替换。

你也可以通过修改 `cats.py` 中变量 `FINAL_DIFF_LIMIT` 的值来设置你希望 diff function 使用的 limit。

你可以通过运行以下命令，在提供的常见拼写错误数据集上检查你的 `final_diff` 的成功率：

```
 python3 score.py
```

如果你不知道从何入手，可以试着把 `furry_fixes` 和 `minimum_mewtations` 的代码复制粘贴到 `final_diff` 中并给它们打分。看看它们修正（以及没修正）的 typos，也许能给你一些灵感！

Checkpoint Submission
=====================

检查确认你完成了 Phase 1 和 Phase 2 的所有题目：

```
python3 ok --score
```

运行 `ok` 命令时，你仍然会看到一些测试是锁定的，因为你还没有完成整个 project。如果你正确完成了到目前为止的所有题目，就能拿到 checkpoint 的满分。

满意之后，把 `cats.py` 上传到 **Gradescope 上的** Cats Checkpoint 作业来提交 checkpoint。请确保在 02/26（周四）的 checkpoint 截止时间之前提交。想复习如何提交到 Gradescope，请参考 [Lab 00](../../lab/lab00.html#3-running-tests "../../lab/lab00.html#3-running-tests")。

你可以点击 **Edit Group** 并输入 partner 的邮箱地址，把 partner 加到你的 Gradescope 提交中。只需要一位 partner 在 Gradescope 上提交。

Phase 3: Multiplayer
====================

和朋友一起打字更有趣！你现在要实现 multiplayer 功能，这样当你在自己的电脑上运行 `cats_gui.py` 时，它会连接到课程服务器
[cats.cs61a.org](https://cats.cs61a.org "https://cats.cs61a.org")
并寻找其他人来比赛。

要和一位朋友比赛，会有 5 个不同的程序在运行：

* 你的 GUI，它是一个处理你浏览器中所有文本着色和显示的程序。
* 你的 `cats_gui.py`，它是一个 web server，用你在 `cats.py` 中写的代码与你的 GUI 通信。
* 你对手的 `cats_gui.py`。
* 你对手的 GUI。
* CS 61A multiplayer server，它把玩家配对并传递消息。

当你打字时，你的 GUI 会把你打的内容上传到你的 `cats_gui.py` server，由它计算你取得了多少进度并返回一个进度更新。这个 server 也会把进度更新上传到 CS 61A multiplayer server，这样你对手的 GUI 也能显示你的进度。

与此同时，你的 GUI 显示会不断尝试通过从 `cats_gui.py` 请求你对手的进度更新来保持最新，而 `cats_gui.py` 又会从 multiplayer server 取回这些信息。

每位玩家都有一个 `id` 号，server 用它来跟踪打字进度。

### Problem 8 (2 pts)

实现 `report_progress`，每当用户打完一个 word 时它就会被调用。它接收目前已经输入的 words list `entered`、`source` 文本中的 words list、用户的 `user_id`，以及一个用于把进度报告上传到 multiplayer server 的 `upload` function。`entered` 中的 words 永远不会比 `source` 中多。

你的 progress 是 `source` 中你正确输入的 words（直到第一个不正确的 word 为止）与 `source` words 总数之比。例如，下面这个例子的 progress 是 `0.25`：

```
report_progress(["Hello", "ths", "is"], ["Hello", "this", "is", "wrong"], ...)
```

你的 `report_progress` function 应该：

1. 通过用包含两个键 `'id'` 和 `'progress'` 的 dictionary 调用 `upload` function，向 multiplayer server 上传一条消息。`'id'` 键应设为用户的 `user_id`，`'progress'` 键应存上面定义的、为该用户计算出的 progress。
2. 返回为该用户计算出的 progress。

> **提示：**
> 参见下面的 dictionary，它展示了 `upload` function 可能的一种输入。
> 这个 dictionary 表示一位 `user_id` 为 4、`progress` 为 0.6 的玩家。
>
> `{'id': 4, 'progress': 0.6}`

在写任何代码之前，先解锁测试以验证你对题目的理解：

```
python3 ok -q 08 -u

Copy

✂️
```

  

解锁完成后，开始实现你的解法。你可以用以下命令检查正确性：

```
python3 ok -q 08

Copy

✂️
```

  

### Problem 9 (1 pt)

实现 `time_per_word`，它接收两个参数：

1. `words`：玩家们正在打的 words list。
2. `timestamps_per_player`：一个 list of lists，其中每个内层 list 包含表示每位玩家打完 `words` 中每个 word 的时间的 timestamps。

这个 function 应返回一个具有以下结构的 dictionary：

* `'words'`：玩家们正在打的 words list。
* `'times'`：一个 list of lists `times`，保存每位玩家打每个 word 所用的时长。具体来说，`times[i][j]`处的值应表示玩家 `i` 打 `words[j]` 这个 word 所花的时间。它等于该玩家打完 `words[j]` 的时间与打完 `words[j-1]` 的时间之差。对于 `words[0]`，它等于该玩家打完 `words[0]` 的时间与开始打字的时间之差。

参数 `timestamps_per_player` 中的 timestamps 是累积的且总是递增的，而 `times` 中的值是**每位玩家相邻 timestamps 之间的差值**。

这里有个例子：如果 `timestamps_per_player = [[1, 3, 5], [2, 5, 6]]`，那么 `times` 会是 `[[2, 2], [3, 1]]`。

这是因为第一位玩家分别在 timestamps `1`、`3`、`5` 打完每个 word，而第二位玩家分别在 timestamps `2`、`5`、`6` 打完每个 word。所以 timestamps 的差值是
`(3-1)`、`(5-3)`（第一位玩家）以及
`(5-2)`、`(6-5)`（第二位玩家）。
`timestamps_per_player` 中每个 list 的第一个值表示每位玩家的初始开始时间。

在写任何代码之前，先解锁测试以验证你对题目的理解：

```
python3 ok -q 09 -u

Copy

✂️
```

  

解锁完成后，开始实现你的解法。你可以用以下命令检查正确性：

```
python3 ok -q 09

Copy

✂️
```

  

### Problem 10 (3 pts)

实现 `fastest_words`，它返回每位玩家输入最快的 words。这个 function 在所有玩家都打完时被调用。它接收一个由 `time_per_word` 返回的 dictionary。

`fastest_words` function 返回一个 words 的 list of lists，每位玩家一个 list。嵌套 list 的 index 表示玩家。每位玩家的 list 包含他们比所有其他玩家都输得更快的 words。在并列的情况下，index 最小的玩家被视为输入最快的那个。

例如，考虑两位打了 `Just have fun` 的玩家。Player 0 最快打出 `'fun'`（3 秒），Player 1 最快打出 `'Just'`（4 秒），他们在 word `'have'` 上并列（都用了 1 秒）。在这种情况下，Player 0 被视为 `'have'` 的最快者，因为他们的 index 更小。

```
>>> player_0 = [5, 1, 3]
>>> player_1 = [4, 1, 6]
>>> fastest_words({'words': ['Just', 'have', 'fun'], 'times': [player_0, player_1]}) # player 0 -> ['have', 'fun'], player 1 -> ['Just']
[['have', 'fun'], ['Just']]
```

使用（已提供的）helper function `get_time` 从 `times` 中获取单个时间。当你试图访问一个不存在的时间时，它会提供有用的错误信息。

```
def get_time(times, player_num, word_index):
    """Return the time it took player_num to type the word at word_index,
    given a list of lists of times returned by time_per_word."""
```

> **重要**：
> 确保你的实现不会修改给定的玩家输入 lists。
> 对于上面的例子，对 `[player_0, player_1]` 调用 `fastest_words`
> **不应该**修改 `player_0` 或 `player_1`。
>
> 玩家不一定总是两位，所以请以能处理不确定数量玩家的方式
> 泛化这个 function。

在写任何代码之前，先解锁测试以验证你对题目的理解：

```
python3 ok -q 10 -u

Copy

✂️
```

  

解锁完成后，开始实现你的解法。你可以用以下命令检查正确性：

```
python3 ok -q 10

Copy

✂️
```

  

恭喜！现在你可以和课程里的其他同学比赛了。把 `cats.py` 底部的 `enable_multiplayer` 设为 `True`，然后飞快地打字吧！

```
python3 cats_gui.py
```

Project Submission
==================

对所有题目运行 `ok`，确保所有测试都已解锁并通过：

```
python3 ok
```

你也可以检查你在 project 每一部分的得分：

```
python3 ok --score
```

满意之后，把 `cats.py` 上传到 **Gradescope** 上的 **Cats** 作业来提交这份作业。想复习如何操作，请参考 [Lab 00](../../lab/lab00.html#task-c-submitting-the-assignment "../../lab/lab00.html#task-c-submitting-the-assignment")。

你可以点击 **Edit Group** 并输入 partner 的邮箱地址，把 partner 加到你的 Gradescope 提交中。只需要一位 partner 在 Gradescope 上提交。

Phase 4: Efficiency (Extra Challenge)
=====================================

### (Optional) Problem EC (0 pt)

> **注意**：
> 这道题是**可选的**，而且**不计任何分**。它是为那些有兴趣提升自己代码效率的同学准备的额外挑战。**只有在你完成了 project 中所有其他题目之后，才去尝试这道题。**

> 在 Office Hours 和 Project Parties 期间，staff 会优先帮助同学们解答必做题目。除非
> [queue](https://oh.cs61a.org/ "https://oh.cs61a.org/") 为空，否则我们不会为这道题提供帮助。
> 在这道题中，你将实现 memoization decorators，通过 "记住" 特别耗资源的操作的结果，来提升我们程序的效率。

请确保你熟悉 decorators 和 memoization。如果你想复习，请展开下面的下拉框获取更多信息。

Decorators (enable JavaScript)

A Python decorator 允许你在不改变 function 结构的情况下修改一个已有的 function。

具体来说，一个 decorator function 是一个 higher-order function，它……

* 把原 function 作为输入
* 返回一个功能被修改过的新 function
* 这个新 function **必须**包含与原 function 相同的参数

下面是一个 decorator 的例子，它把一个单输入 function 执行两次：

```
>>> def do_twice(original_function):
...     def repeat(x):
...             original_function(x)
...             original_function(x)
...     return repeat
```

我们可以在多种场景中应用这个 function：

```
# Printing a value twice
>>> @do_twice
... def print_value(x):
...     print(x)
...
>>> print_value(5)
5
5
# Adding an item to a list twice
>>> lst = []
>>> @do_twice
... def add_to_list(item):
...     lst.append(item)
...
>>> add_to_list(5)
>>> lst
[5, 5]
```

此外，注意我们也可以直接调用 decorator function，而不使用 `@` 记法（即 `print_value = do_twice(print_value)`）。不过，把 decorators 直接放在我们要修改的 function 上方通常更实用，因为它们能更好地说明这些 functions 在我们的代码中是如何被改变的。

Memoization (enable JavaScript)

注意我们在前面几题中写的 diff functions 效率非常低：你可能会发现计算机多次做同一个 recursive call。对于一个有多个参数、还有三个 recursive calls 的 function 来说，这可能不容易看出来。先用一个 lecture 中定义过的、像 `fib` 这样的 function 来观察会更容易。

![Fib Tree](images/fib_tree.png)

注意上面的树状图中有多少多余的 recursive calls。我们的目标是让程序存储过去已求值的 recursive calls 的结果，这样如果将来出现同样的 recursive call，我们就可以复用它们。例如，`fib(5)` 的第一个分支调用了 `fib(3)`，而它当时还没有被求值过。所以我们必须走完它后续的所有 recursive calls 才能得到它的返回值。但是，当我们遇到作为 `fib(4)` 一个分支的那个 `fib(3)` 调用时，我们之前已经得到过它的返回值了！所以如果我们有办法把这一信息存储到所谓的 cache 中并从中取回，就可以避免不必要的计算。我们不再需要对它的分支 `fib(1)` 和 `fib(2)` 做任何后续的 recursive calls。这就是 **memoization** 的概念：把昂贵计算的结果存入 cache，并在执行重复操作时从 cache 中取回信息。

  

我们将使用两个 memoization decorators。`memo` 是一个通用的、万能的 decorator，它会把它所标注的 function 进行 memoize。如果 `memo` 遇到一个它没见过的输入，它会把计算出的结果存入它的 `cache`。如果 `memo` 收到一个它已经见过的输入，它会取出 `cache` 中存的值并直接返回，不做任何额外的计算。我们已经为你提供了 `memo` 的完整实现。

你的任务是实现 `memo_diff`。`memo_diff` 是一个 higher-order function，它接收一个 `diff_function`，并返回另一个名为 `memoized` 的 diff function，它和所有 diff functions 一样，接收 `entered`、`source` 和 `limit`。`memoized` 应该做以下事情：

* 当 `memoized` 第一次见到一个 (`entered`, `source`) 对时，它应该用 `diff_function` 计算
  差异，并把该值和所用的 `limit` 作为 (`value`, `limit`) tuple 一起缓存。
* 如果 `memoized` 再次遇到该 (`entered`, `source`) 对，若提供的 `limit` 小于或等于
  缓存的 limit，它应返回记忆化的 `value`。否则，
  应重新计算差异、重新缓存并返回。

> **重要：** 实现这个 function 时，请确保用 tuple 而不是 list 来在 cache 中存储这些值对。
> 在 dictionaries 中，keys 必须*不可变*（这就是用 tuple 可以、而用 list 不行的原因）。
> 如果你好奇为什么 `memo_diff` 与 `memo` 不同、并且要这样实现，请参考下面的下拉框：

More Information (enable JavaScript)

`memo` 和 `memo_diff` 有何不同？虽然 `memo` 只存储 function 调用的结果，但 `memo_diff` 还要考虑一个额外的约束 `limit`，它会影响缓存的结果是否可以使用。当 `memo_diff` function 以一个 (`entered`, `source`) 对被调用时，它不只是检查这个对之前是否见过；它还会检查 `limit` 是否小于或等于缓存的 `limit`。这是 `memo` 不会做的一项额外检查。

为什么要这样处理 `limit`？我们已经知道 `limit` 表示 diff function 所关心的最大差异——也就是说，超过 `limit` 的差异都可以视为相同。所以 diff functions 在差异低于 limit 时会给出准确的差异值，在高于 limit 时会给出不准确的值。因此，如果某个缓存的差异值是在更高的 limit 下算出来的，我们可以信任它；但在更低 limit 下算出来的就不能信任。

例如，下面第一次调用的结果可以让我们预测第二次调用的结果。更高的 limit 为我们提供了更多信息。然而，第二次调用并不能让我们预测第一次调用。

```
>>> minimum_mewtations("hello", "hasldfasdfsffsfasdf", 100)
17
>>> minimum_mewtations("hello", "hasldfasdfsffsfasdf", 2)
3
```

  

实现 `memo_diff` 后，最后完成：

1. 用 `memo` 装饰 `autocorrect`。
2. 用 `memo_diff` 装饰 `minimum_mewtations`。

现在运行 `autocorrect` 和 `minimum_mewtations` 应该会快得多！

> **注意**：
> 如果你在涉及 `call_count` 的 autograder 测试上失败，很可能是你（Q7 中的）`minimum_mewtations` 实现没有做到*尽可能紧的 base cases*，还需要一些优化。
> Q7 的测试并不严格，所以即使你通过了 Q7 的测试，你的 base cases 也可能仍然不够紧。
> 确保你没有做不必要的 recursive calls。
> 我们在这里之所以严格，是因为尽可能紧的 base cases 对你代码的效率至关重要。
>
> **重要**：
> 请先自己尝试！只有在某个测试用例上卡了很久之后，再去参考下面的常见错误部分。否则，你可能无法从这个 project 中学到那么多。

Common Mistakes (enable JavaScript)

* 考虑 `minimum_mewtations(entered = "maooo", source = "mao", limit = 0)` 这个情况：既然不允许任何变换，而这两个 words 又不相同，你的 function 能多快地判断出结果是不可能的？
* 考虑 `minimum_mewtations(entered = "habc", source = "hmao", limit = 某个大于零的 limit)` 这个情况：既然两个 strings 都以同一个字符 `h` 开头，在这种情况下最有效的做法是什么？这个 function 到底应不应该尝试 "add"（得到 `habc` 和 `mao`）或 "remove"（得到 `abc` 和 `hmao`）？你的实现是否利用了这项优化？

> 注意：autograder 运行需要一点时间，但应该不会超过 10 秒。

在写任何代码之前，先解锁测试以验证你对题目的理解：

```
python3 ok -q EC -u

Copy

✂️
```

  

解锁完成后，开始实现你的解法。你可以用以下命令检查正确性：

```
python3 ok -q EC

Copy

✂️
```

* [Introduction](index.html#introduction "index.html#introduction")
* [Final Product](index.html#final-product "index.html#final-product")
* [Download Starter Files](index.html#download-starter-files "index.html#download-starter-files")
* [Logistics](index.html#logistics "index.html#logistics")
* [Phase 1: Typing](index.html#phase-1-typing "index.html#phase-1-typing")

+ [Problem 1 (1 pt)](index.html#problem-1-1-pt "index.html#problem-1-1-pt")
+ [Problem 2 (1 pt)](index.html#problem-2-1-pt "index.html#problem-2-1-pt")
+ [Problem 3 (2 pts)](index.html#problem-3-2-pts "index.html#problem-3-2-pts")
+ [Problem 4 (1 pt)](index.html#problem-4-1-pt "index.html#problem-4-1-pt")

* [Phase 2: Autocorrect](index.html#phase-2-autocorrect "index.html#phase-2-autocorrect")

+ [Problem 5 (2 pts)](index.html#problem-5-2-pts "index.html#problem-5-2-pts")
+ [Problem 6 (3 pts)](index.html#problem-6-3-pts "index.html#problem-6-3-pts")
+ [Problem 7 (3 pts)](index.html#problem-7-3-pts "index.html#problem-7-3-pts")
+ [(Optional) Extension: Final Diff (0 pts)](index.html#optional-extension-final-diff-0-pts "index.html#optional-extension-final-diff-0-pts")

* [Checkpoint Submission](index.html#checkpoint-submission "index.html#checkpoint-submission")
* [Phase 3: Multiplayer](index.html#phase-3-multiplayer "index.html#phase-3-multiplayer")

+ [Problem 8 (2 pts)](index.html#problem-8-2-pts "index.html#problem-8-2-pts")
+ [Problem 9 (1 pt)](index.html#problem-9-1-pt "index.html#problem-9-1-pt")
+ [Problem 10 (3 pts)](index.html#problem-10-3-pts "index.html#problem-10-3-pts")

* [Project Submission](index.html#project-submission "index.html#project-submission")
* [Phase 4: Efficiency (Extra Challenge)](index.html#phase-4-efficiency-extra-challenge "index.html#phase-4-efficiency-extra-challenge")

+ [(Optional) Problem EC (0 pt)](index.html#optional-problem-ec-0-pt "index.html#optional-problem-ec-0-pt")
