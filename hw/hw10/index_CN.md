Homework 10 | CS 61A Spring 2026



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



Homework 10: SQL

* [hw10.zip](hw10.zip "hw10.zip")
===================================================

*截止时间为 5 月 1 日（周五）晚上 11:59。*

Instructions
------------

下载 [hw10.zip](hw10.zip "hw10.zip")。

**提交：** 完成后，请把作业提交到 Gradescope。在截止时间之前你可以多次提交；只以最后一次提交计分。请确认你已在 Gradescope 上成功提交代码。有关提交作业的更多说明，请参见 [Lab 0](../../lab/lab00.html "../../lab/lab00.html")。

**使用 Ok：** 如果你对 Ok 的使用有任何疑问，请参阅[此指南。](../../articles/using-ok.html "../../articles/using-ok.html")

**评分：** 作业根据正确性评分。每答错一道题，总分就会减少 1 分。**这份作业满分为 2 分。**
  

要检查你的进度，你可以直接运行 `sqlite3`：

```
python3 sqlite_shell.py --init hw10.sql
```

你也应该使用 `ok` 检查你的工作：

```
python3 ok
```

Visualizing SQL
---------------

CS61A SQL Web Interpreter 是一个用于可视化和调试 SQL statements 的绝佳工具！

要开始使用，请访问 [code.cs61a.org](https://code.cs61a.org "https://code.cs61a.org")，并在启动界面上点击 `Start SQL interpreter`。

作业中用到的大多数 tables 都已经可供使用，所以让我们试着执行一条 `SELECT` statement：

![](assets/visualize-sql-eg1.png)

除了显示输出 table 的可视化表示之外，“Step-by-step” 按钮还能让我们逐步执行 SQL，并可视化发生的每一次转换。在我们的例子中，点击下一个箭头将产生以下可视化结果，准确展示 SQL 是如何对我们的 rows 进行分组以形成最终输出的！

Show output (enable JavaScript)

![](assets/visualize-sql-eg2.png)

Required Questions
==================

SQL
---

### Dog Data

在下面每道题中，你将基于以下关于狗的 tables 定义一个新的 table。

```
CREATE TABLE parents (parent TEXT, child TEXT);

INSERT INTO parents VALUES
  ('ace', 'bella'),
  ('ace', 'charlie'),
  ('daisy', 'hank'),
  ('finn', 'ace'),
  ('finn', 'daisy'),
  ('finn', 'ginger'),
  ('ellie', 'finn');

CREATE TABLE dogs (name TEXT, fur TEXT, height INTEGER);

INSERT INTO dogs VALUES
  ('ace',     'long',  26),
  ('bella',   'short', 52),
  ('charlie', 'long',  47),
  ('daisy',   'long',  46),
  ('ellie',   'short', 35),
  ('finn',    'curly', 32),
  ('ginger',  'short', 28),
  ('hank',    'curly', 31);

CREATE TABLE sizes (size TEXT, min INTEGER, max INTEGER);

INSERT INTO sizes VALUES
  ('toy',      24, 28),
  ('mini',     28, 35),
  ('medium',   35, 45),
  ('standard', 45, 60);
```

`parents` table 为每个 parent-child relationship 包含一行；例如，第一行描述的是狗 `"ace"` 是狗 `"bella"` 的 parent。`dogs` table 包含每只狗的名字、fur type 和 height。`sizes` table 为每一种狗的 classification 包含一行。如果一只狗的 height 大于 `min` 且小于或等于 `max`，它便符合某个特定的 classification。

你的 queries 应该仍然正确执行，*即使这些 tables 中的 values 发生变化*。例如，如果要求你列出所有名字以 `h` 开头的狗，你应该这样写：

```
SELECT name FROM dogs WHERE name LIKE "h%";
```

`%` 符号匹配任意数量的 characters，而且 `sqlite` 中的 patterns 不区分大小写，所以 pattern `"h%"` 匹配所有以 `h` 或 `H` 开头的 strings。如果添加一行名字为 `harry` 的记录，这个 query 仍然正确。相反，写像 `SELECT "hank";` 这样的 query 就不正确，它只对示例输入有效。

### Q1: By Parent Height

创建一个 table `by_parent_height`，它有一个 column 包含所有有 `parent` 的狗的名字，按照 parent 狗的 height 从最高到最低排序。

```
-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

例如，`finn` 的 parent 是 `ellie`，其 height 为 35，因此应出现在 `ginger` 之前，后者的 parent 是 `finn`，height 为 32。parent height 相同的狗的名字应以任意顺序聚在一起。例如，`bella` 和 `charlie` 都应出现在末尾，但它们两者谁先谁后都可以。

对于我们的示例 tables，`by_parent_height` table 应如下所示：

```
+----------+
| chil     |
+----------+
| hank     |
| finn     |
| ace      |
| daisy    |
| ginger   |
| bella    |
| charlie  |
+----------+
```

使用 Ok 来测试你的代码：

```
python3 ok -q by_parent_height

Copy

✂️
```

  


### Q2: Size of Dogs

Fédération Cynologique Internationale 把 standard poodle 分类为超过 45 cm 且不超过 60 cm。`sizes` table 描述了这一分类以及其他类似分类，其中一只狗的 `height` 必须超过 `min` 且小于或等于 `max` 才符合 `size`。

创建一个 `size_of_dogs` table，包含两个 columns，一个对应每只狗的 `name`，另一个对应它的 `size`。

```
-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

`size_of_dogs` table 应如下所示：

```
+----------+----------+
| name     | size     |
+----------+----------+
| ace      | toy      |
| bella    | standard |
| charlie  | standard |
| daisy    | standard |
| ellie    | mini     |
| finn     | mini     |
| ginger   | toy      |
| hank     | mini     |
+----------+----------+
```

使用 Ok 来测试你的代码：

```
python3 ok -q size_of_dogs

Copy

✂️
```

  


### Q3: Sentences

Siblings 是指拥有相同 parent 的狗组成的 pairs。创建一个 table，为每一对具有相同 size classification 的 siblings 包含一行，其中只有一个 column，包含一句按其 size 描述这对 siblings 的句子。

```
-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

每一对 siblings 在输出中应只出现一次，并且 siblings 应按字母顺序列出（例如 `"bella and charlie..."` 而不是 `"charlie and bella..."`），如下所示：

```
sqlite> SELECT * FROM sentences;
The two siblings, bella and charlie, have the same size: standard
The two siblings, ace and ginger, have the same size: toy
```

> 提示：首先创建一个 helper table，包含每一对 siblings 的名字。这样在构造主 table 时比较 siblings 的 sizes 会更容易。注意不要把 child 与它自己配成 pair，也不要包含重复的 pairs。
>
> 提示：如果你把一个 table 与它自身 join，请在 `FROM` clause 中使用 `AS` 给每个 table 一个 alias。
>
> 提示：要把两个 strings 拼接成一个，请使用 `||` operator，例如 `SELECT "hello" || "world";` 会返回 `helloworld`。

使用 Ok 来测试你的代码：

```
python3 ok -q sentences

Copy

✂️
```

  

### Q4: Low Variance

我们想创建一个 table，包含所有共享同一 `fur` type 的狗的 *height range*（定义为最大 `height` 与最小 `height` 之差）。不过，我们只考虑这样的 `fur` type：具有该 `fur` type 的每只狗的 height 都在所有具有该 `fur` type 的狗的平均 `height` 的 30% 以内；我们称之为 *low variance* 标准。

例如，如果 short-haired 狗的平均 `height` 是 10，那么为了被包含在我们的输出中，所有 short hair 的狗的 `height` 必须至多为 13 且至少为 7（*包含端点*）。

> 提示：`MIN`、`MAX` 和 `AVG` 在这里会很有用。
>
> 提示：你可能想先求出平均 height，并确保：
>
> ```
> * There are no heights smaller than 0.7 (i.e. 70%) of the average.
> * There are no heights greater than 1.3 (i.e. 130%) of the average.
> ```

```
-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

你的输出应有两个 columns，顺序如下：`fur` type 和符合该标准的 `fur` types 的 `height_range`。对于示例 tables，它应如下所示：

```
+------------+--------------+
| fur        | height_range |
+------------+--------------+
| Curly      | 1            |
+------------+--------------+
```

Explanation (enable JavaScript)

long-haired 狗的平均 height 是 39.7，所以 low variance 标准要求每只 long-haired 狗的 height 在 27.8 到 51.6 之间。然而，`ace` 是一只 height 为 26 的 long-haired 狗，超出了这个范围。对于 short-haired 狗，`bella` 落在有效范围之外（你可以验证一下！）。因此，short-haired 和 long-haired 狗都不在输出中。有两只 curly haired 狗：`finn`，height 为 32；`hank`，height 为 31。这给出的 height range 为 1。

使用 Ok 来测试你的代码：

```
python3 ok -q low_variance

Copy

✂️
```

  

Submit Assignment
=================

把这份作业提交上去，方法是把你编辑过的所有文件上传到**对应的 Gradescope 作业**。[Lab 00](../../lab/lab00.html "../../lab/lab00.html") 中有详细说明。

请确保把 `hw10.sql` 提交到 autograder！

Exam Practice
-------------

以下是往几学期的一些 SQL 考题，你可能会觉得它们对额外练习考试有帮助。

1. [Fall 2019 Final, Question 10: Big Game](../../exam/fa19/final/61a-fa19-final.pdf#page=11 "../../exam/fa19/final/61a-fa19-final.pdf#page=11")
2. [Summer 2019 Final, Question 8: The Big SQL](../../exam/su19/final/61a-su19-final.pdf#page=11 "../../exam/su19/final/61a-su19-final.pdf#page=11")
3. [Fall 2018 Final, Question 7: SQL of Course](https://inst.eecs.berkeley.edu/~cs61a/fa18/assets/pdfs/61a-fa18-final.pdf#page=9 "https://inst.eecs.berkeley.edu/~cs61a/fa18/assets/pdfs/61a-fa18-final.pdf#page=9")

* [Visualizing SQL](index.html#visualizing-sql "index.html#visualizing-sql")
* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [SQL](index.html#sql "index.html#sql")

- [Dog Data](index.html#dog-data "index.html#dog-data")
- [Q1: By Parent Height](index.html#q1-by-parent-height "index.html#q1-by-parent-height")
- [Q2: Size of Dogs](index.html#q2-size-of-dogs "index.html#q2-size-of-dogs")
- [Q3: Sentences](index.html#q3-sentences "index.html#q3-sentences")
- [Q4: Low Variance](index.html#q4-low-variance "index.html#q4-low-variance")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")

+ [Exam Practice](index.html#exam-practice "index.html#exam-practice")
