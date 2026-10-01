Lab 11: SQL | CS 61A Spring 2026



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



Lab 11: SQL

* [lab11.zip](lab11.zip "lab11.zip")
=================================================

*截止时间为 4 月 29 日（周三）晚上 11:59。*

Starter Files
-------------

下载 [lab11.zip](lab11.zip "lab11.zip")。

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

[YouTube 链接](https://youtu.be/playlist?list=PLx38hZJ5RLZcT96fbelbvVGg1I8D2jRjp "https://youtu.be/playlist?list=PLx38hZJ5RLZcT96fbelbvVGg1I8D2jRjp")

  

SQL
---

一条 `SELECT` statement 根据 input rows 描述一个输出 table。要编写这样一条 statement：

1. 使用 `FROM` 和 `WHERE` clauses 描述 **input rows**。
2. 使用 `GROUP BY` 和 `HAVING` clauses **分组**这些 rows，并确定哪些 groups 应作为 output rows 出现。
3. 使用 `SELECT` 和 `ORDER BY` clauses 格式化并排序 **output rows** 和 columns。

`SELECT` *(Step 3)* `FROM` *(Step 1)* `WHERE` *(Step 1)* `GROUP BY` *(Step 2)* `HAVING` *(Step 2)* `ORDER BY` *(Step 3)*;

Step 1 可能涉及连接 tables（用逗号），以形成由现有 tables 中两行或多行组成的 input rows。

`WHERE`、`GROUP BY`、`HAVING` 和 `ORDER BY` clauses 是可选的。

如果你需要复习 SQL，请查阅下拉框。你也可以直接跳到题目部分，遇到困难时再回到这里查阅。

SQL (enable JavaScript)

SQL Basics
----------

### Example Table

下面是一个名为 `big_game` 的 table，用于下文的示例，它记录了每年 Big Game 的比分。这个 table 有三列：`berkeley`、`stanford` 和 `year`。

![](assets/big-game.png)

```
CREATE TABLE big_game (
    berkeley INTEGER, stanford INTEGER, year INTEGER);

INSERT INTO big_game (berkeley, stanford, year) VALUES
    (30, 7, 2002),
    (28, 16, 2003),
    (17, 38, 2014);
```

你可以像这样在 sqlite 中查看它：

```
sqlite> .mode column
sqlite> SELECT * FROM big_game;
berkeley  stanford  year
--------  --------  ----
30        7         2002
28        16        2003
17        38        2014
```

如果你所用版本的 sqlite 中 `.mode column` 命令不起作用，没关系，忽略它即可。

### Selecting From Tables

通常，我们会用一条 `SELECT` statement 从现有 tables 创建新 table：

```
SELECT [columns] FROM [tables] WHERE [condition] ORDER BY [columns] LIMIT [limit];
```

我们来分解这条 statement：

* `SELECT [columns]` 告诉 SQL 我们希望在输出 table 中包含给定的 columns；`[columns]` 是一个以逗号分隔的 column 名 list，可以用 `*` 选择所有 columns
* `FROM [table]` 告诉 SQL 我们要选择的 columns 来自给定的 table
* `WHERE [condition]` 过滤输出 table，只包含 values 满足给定 `[condition]`（一个 boolean expression）的 rows
* `ORDER BY [columns]` 按给定的以逗号分隔的 columns list 对输出 table 中的 rows 排序；默认情况下 values 按升序（ASC）排序，但你可以用 DESC 按降序排序
* `LIMIT [limit]` 用整数 `[limit]` 限制输出 table 中的 rows 数量

下面是一些示例：

从 `big_game` table 中选择 Berkeley 的所有比分，但只包括 2002 年之后的比分：

```
sqlite> SELECT berkeley FROM big_game WHERE year > 2002;
28
17
```

选择 Berkeley 获胜年份中两所学校的比分：

```
sqlite> SELECT berkeley, stanford FROM big_game WHERE berkeley > stanford;
30|7
28|16
```

选择 Stanford 得分超过 15 分的年份：

```
sqlite> SELECT year FROM big_game WHERE stanford > 15;
2003
2014
```

### SQL operators

`SELECT`、`WHERE` 和 `ORDER BY` clauses 中的 expressions 可以包含以下一个或多个 operators：

* comparison operators：`=`, `>`, `<`, `<=`, `>=`, `<>` 或 `!=`（"not equal"）
* boolean operators：`AND`、`OR`
* arithmetic operators：`+`, `-`, `*`, `/`
* concatenation operator：`||`

输出每年 Berkeley 比分与 Stanford 比分之比：

```
sqlite> select berkeley * 1.0 / stanford from big_game;
0.447368421052632
1.75
4.28571428571429
```

输出两队得分都超过 10 分的年份的比分总和：

```
sqlite> select berkeley + stanford from big_game where berkeley > 10 and stanford > 10;
55
44
```

输出一个只有单个 column、单个 row、包含值 "hello world" 的 table：

```
sqlite> SELECT "hello" || " " || "world";
hello world
```

Joins
-----

要从多个 tables 中选择数据，我们可以使用 joins。joins 有很多类型，但我们唯一需要关心的是 inner join。要对两个或多个 tables 执行 inner join，只需把它们都列在 `SELECT` statement 的 `FROM` clause 中：

```
SELECT [columns] FROM [table1], [table2], ... WHERE [condition] ORDER BY [columns] LIMIT [limit];
```

我们可以从多个不同的 tables 中选择，也可以多次从同一个 table 中选择。

假设我们有下面这个 table，它包含 2002 年以来 Cal 的美式橄榄球主教练的名字：

```
CREATE TABLE coaches (
    name TEXT,
    start INTEGER,
    end INTEGER
);

INSERT INTO coaches (name, start, end)
VALUES
    ('Jeff Tedford', 2002, 2012),
    ('Sonny Dykes', 2013, 2016),
    ('Justin Wilcox', 2017, 2025);
```

当我们连接两个或多个 tables 时，默认输出是一个 [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product "https://en.wikipedia.org/wiki/Cartesian_product")。例如，如果我们把 `big_game` 与 `coaches` 连接，会得到以下结果：

```
sqlite> SELECT * FROM big_game JOIN coaches;
berkeley  stanford  year  name           start  end
--------  --------  ----  -------------  -----  ----
30        7         2002  Jeff Tedford   2002   2012
30        7         2002  Sonny Dykes    2013   2016
30        7         2002  Justin Wilcox  2017   2025
28        16        2003  Jeff Tedford   2002   2012
28        16        2003  Sonny Dykes    2013   2016
28        16        2003  Justin Wilcox  2017   2025
17        38        2014  Jeff Tedford   2002   2012
17        38        2014  Sonny Dykes    2013   2016
17        38        2014  Justin Wilcox  2017   2025
```

如果我们想把每场比赛与那个赛季的教练对应起来，就必须在 `WHERE` clause 中比较两个 tables 的 columns：

```
sqlite> SELECT * FROM big_game JOIN coaches ON year >= start AND year <= end
   ...> ;
berkeley  stanford  year  name          start  end
--------  --------  ----  ------------  -----  ----
30        7         2002  Jeff Tedford  2002   2012
28        16        2003  Jeff Tedford  2002   2012
17        38        2014  Sonny Dykes   2013   2016
```

在上面的 query 中，没有 column 名是有歧义的。例如，`start` column 显然来自 `coaches` table，因为 `big_game` table 中没有同名的 column。然而，如果某个 column 名存在于多个被连接的 tables 中，或者我们把一个 table 与自身连接，就必须用 dot notation 和 aliases 来消除 column 名的歧义。

举例来说，让我们找出 `big_game` 中每场比赛与之前任何一场比赛相比，每支球队的比分差是多少。由于这个 table 中的每一 row 代表一场比赛，为了比较两场比赛，我们必须把 `big_game` 与自身连接：

```
sqlite> SELECT b.Berkeley - a.Berkeley, b.Stanford - a.Stanford, a.Year, b.Year
   ...>   FROM big_game AS a, big_game AS b WHERE a.Year < b.Year;
b.Berkeley - a.Berkeley  b.Stanford - a.Stanford  year  year
-----------------------  -----------------------  ----  ----
-2                       9                        2002  2003
-13                      31                       2002  2014
-11                      22                       2003  2014
```

在上面的 query 中，我们给第一个 `big_game` table 起别名 `a`，给第二个 `big_game` table 起别名 `b`。然后我们就可以用 aliases 配合 dot notation 引用每个 table 的 columns，例如用 `a.Berkeley`、`a.Stanford` 和 `a.Year` 从第一个 table 中选择。

SQL Aggregation
---------------

下面是另一个示例 table，这次是关于航班的：

```
CREATE TABLE flights (
    departure TEXT, arrival TEXT, price INTEGER);

INSERT INTO flights (departure, arrival, price) VALUES
    ('SFO', 'LAX', 97),
    ('SFO', 'AUH', 848),
    ('LAX', 'SLC', 115),
    ('SFO', 'PDX', 192),
    ('AUH', 'SEA', 932),
    ('SLC', 'PDX', 79),
    ('SFO', 'LAS', 40),
    ('SLC', 'LAX', 117),
    ('SEA', 'PDX', 32),
    ('SLC', 'SEA', 42),
    ('SFO', 'SLC', 97),
    ('LAS', 'SLC', 50),
    ('LAX', 'PDX', 89);
```

应用一个 [aggregate function](http://www.sqlite.org/lang_aggfunc.html "http://www.sqlite.org/lang_aggfunc.html")（例如 `MAX(column)`）会把多个 rows 的 values 合并成一个 output row。

默认情况下，我们合并 table 中所有 rows 的 values。例如，如果我们想数一数 `flights` table 中有多少 rows，可以用：

```
sqlite> SELECT COUNT(*) from FLIGHTS;
13
```

如果我们想按相似的 rows 把 values 分组，并在这些 groups 内执行聚合操作，该怎么办呢？我们使用 `GROUP BY` clause。

再看一个例子。对于每个唯一的 departure，把所有 departure 机场相同的 rows 收集为一个 group。然后选择 `price` column 并应用 `MIN` 聚合，得到该 group 中最便宜的出发航班的价格。最终结果是一个包含 departure 机场和最便宜出发航班的 table。

```
sqlite> SELECT departure, MIN(price) FROM flights GROUP BY departure;
departure  MIN(price)
---------  ----------
AUH        932
LAS        50
LAX        89
SEA        32
SFO        40
SLC        42
```

就像我们可以用 `WHERE` 过滤 rows 一样，我们也可以用 `HAVING` 过滤 groups。通常，`HAVING` clause 应该使用 aggregation function。假设我们想查看所有至少有两次出发航班的机场：

```
sqlite> SELECT departure FROM flights GROUP BY departure HAVING COUNT(*) >= 2;
departure
---------
LAX
SFO
SLC
```

注意，`COUNT(*)` 聚合只是统计每个 group 中的 rows 数量。假设我们想改为统计*不同*机场的数量，那么可以用以下 query：

```
sqlite> SELECT COUNT(DISTINCT departure) AS destinations FROM flights;
destinations
------------
6
```

这列举了 `flights` table 中所有不同的 departure 机场（此处为：SFO、LAX、AUH、SLC、SEA 和 LAS）。

Usage
-----

首先，检查作业文件旁边是否存在名为 `sqlite_shell.py` 的文件。如果没有看到它，或者使用它时遇到问题，请向下滚动到 Troubleshooting 部分，了解在继续之前如何下载官方预编译的 SQLite 二进制文件。

你可以在 Terminal 或 Git Bash 中用以下命令启动一个交互式 SQLite session：

```
python3 sqlite_shell.py
```

当 interpreter 运行时，你可以输入 `.help` 查看一些可以运行的命令。

要退出 SQLite interpreter，输入 `.exit` 或 `.quit`，或者按 `Ctrl-C`。记住，如果按下回车后看到 `...>`，你很可能忘了 `;`。

你也可以通过以下方式运行 `.sql` 文件中的所有 statements：（这里我们以 `lab11.sql` 文件为例。）

1. 运行你的代码，然后立即退出 SQLite。

   ```
   python3 sqlite_shell.py < lab11.sql
   ```
2. 运行你的代码，然后打开一个交互式 SQLite session，这类似于用交互式 `-i` flag 运行 Python 代码。

   ```
   python3 sqlite_shell.py --init lab11.sql
   ```

Visualizing SQL
---------------

CS61A SQL Web Interpreter 是可视化并调试 SQL statements 的绝佳工具！

要开始使用，请访问 [code.cs61a.org](https://code.cs61a.org "https://code.cs61a.org") 并在启动界面上点击 `Start SQL interpreter`。

作业中使用的大多数 tables 都已经可以直接使用，所以让我们试着执行一条 `SELECT` statement：

![](assets/visualize-sql-names.png)

除了显示输出 table 的可视化表示外，"Step-by-step" 按钮还可以让我们逐步执行 SQL，并将发生的每一次变换可视化。这种可视化通常对较小的 datasets 有用，因为可以查看 table 中的所有 rows。对于 movies dataset 来说，这种可视化就没那么有用了，因为每个 table 都有成千上万行。

  

IMDb
----

IMDb 1000 dataset 包含来自 [Internet Movie Database](https://developer.imdb.com/non-commercial-datasets/ "https://developer.imdb.com/non-commercial-datasets/") 的 1000 部评分最高的热门电影（得票数前 0.2%）。

这个 dataset 中的 tables 相当大，所以用 `LIMIT` 只查看某个 table 中的几行通常很有用。要查看 `titles` table（包含每部电影的信息）中的几行示例：

```
    % sqlite3
    sqlite> .read imdb1000.sql
    sqlite> .tables
    crew        names       principals  ratings     titles
```

以 `.read` 开头的命令会读入 `imdb1000.sql` 中的 SQL commands，后者用 movie dataset 创建新的 tables。`.tables` 命令列出所有 tables。

以下是这个 lab 中你需要的 tables 和 columns。`.mode column` 命令可以改善格式，但它在 `sqlite_shell.py` 中不起作用，而且是可选的。

```
sqlite> .mode column
sqlite> SELECT tconst, title, year, runtime FROM titles LIMIT 3;
tconst     title                            year  runtime
---------  -------------------------------  ----  -------
tt0012349  The Kid                          1921  68
tt0013442  Nosferatu: A Symphony of Horror  1922  94
tt0015864  The Gold Rush                    1925  95

sqlite> SELECT tconst, ordering, nconst, character FROM principals LIMIT 3;
tconst     ordering  nconst     character
---------  --------  ---------  ---------
tt0012349  1         nm0000122  A Tramp
tt0012349  2         nm0701012  The Woman
tt0012349  3         nm0001067  The Child

sqlite> SELECT nconst, name, birth, death FROM names LIMIT 3;
nconst     name            birth  death
---------  --------------  -----  -----
nm0000002  Lauren Bacall   1924   2014
nm0000004  John Belushi    1949   1982
nm0000005  Ingmar Bergman  1918   2007
```

`tconst` 是每部电影的唯一标识符（`t` 代表 title），`nconst` 是每个人的唯一标识符。这些标识符对于连接不同 tables 的 rows 很有用，例如，要确定某部电影的 rating，我们可以在 titles table 中找到该电影的 `nconst`，然后在 ratings table 中查找这个 `nconst`。

### Q1: Newest Movies

创建一个 `newest` table，包含 dataset 中最新（年份最大）的 10 部电影，它有两列：

* `title`：电影的名字
* `year`：电影拍摄的年份

如果愿意，你可以猜猜结果中会有哪些电影。

Hint: Template (enable JavaScript)

```
  SELECT ____, ____
  FROM ____
  ORDER BY ____
  LIMIT ____;
```

1. 用 `FROM` 指定从哪个 table 读取数据。
2. 用 `ORDER BY` 按电影的新旧排序。
3. 用 `LIMIT` 只选出最新的 10 部电影。
4. 用 `SELECT` 把电影 title 和 year 放入输出。



```
CREATE table newest AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

使用 Ok 来测试你的代码：

```
python3 ok -q newest

Copy

✂️
```

  

### Q2: Movies with Dogs

创建一个 `dog_movies` table，为每个名字中带有 "dog" 一词的电影角色包含一行，它有两列：

* `title`（text）：电影的名字
* `character`（text）：狗角色的名字

如果一部电影有多个狗角色，它可能会出现多次。

Hint: Template (enable JavaScript)

```
SELECT _____, _____
FROM _____ JOIN _____ ON _____
WHERE ____ LIKE "%dog%";
```

1. 用 `FROM`、`JOIN` 和 `ON` 合并 `titles` 和 `principals` tables 中的信息。
2. 用 `WHERE` 只选择包含 "dog" 的角色。
3. 用 `SELECT` 把电影 title 和 character 放入输出。



```
CREATE table dog_movies AS 
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

使用 Ok 来测试你的代码：

```
python3 ok -q dog_movies

Copy

✂️
```

  

### Q3: Leads of Leads

创建一个 `leads` table，它有两列：

* `name`（text）：演员的名字
* `lead_roles`（integer）：该演员担任主角的电影数量

你可以在 `principals` table 中查找 `ordering` 为 1 的 rows 来找到主角角色。只选择担任主角**超过 10** 部电影的演员。

Hint: Template (enable JavaScript)

```
  SELECT ____, ____ AS lead_roles
  FROM ____ JOIN ____ ON ____
  WHERE ____
  GROUP BY names.nconst
  HAVING count(*) > 10;
```

1. 用 `FROM` 和 `ON` 合并 `principals` 和 `names` tables 中的信息。
2. 用 `WHERE` 只选择主角角色。
3. 用 `GROUP BY` 为每个人创建一行。
4. 用 `HAVING` 只输出担任主角超过 10 次的人。
5. 用 `SELECT` 把人物的 name 和他们的角色数量放入输出。



```
CREATE table leads AS 
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

使用 Ok 来测试你的代码：

```
python3 ok -q leads

Copy

✂️
```

  

### Q4: Long Movies

创建一个 `long_movies` table，包含每个十年中时长超过 3 小时的电影数量。`long_movies` 有两列：

* `decade`（strings）：年代，例如 `1920s`
* `count`（numbers）：该年代中时长超过 3 小时（180 分钟）的电影数量

对于 IMDB 1000 dataset，结果将是：

```
+--------+-------+
| decade | count |
+--------+-------+
| 1930s  | 1     |
| 1950s  | 2     |
| 1960s  | 2     |
| 1970s  | 3     |
| 1980s  | 2     |
| 1990s  | 7     |
| 2000s  | 4     |
| 2010s  | 3     |
| 2020s  | 4     |
+--------+-------+
```

Hint: Creating the Decade (enable JavaScript)

把数字相加并将结果包含进 string 时，要在算术运算两侧加上括号，例如，注意 string 拼接！

```
sqlite> SELECT (192 * 10) || "s";
1920s
```

Hint: Template (enable JavaScript)

```
SELECT ____ AS decade, ____ AS count
FROM ____
WHERE ____
GROUP BY ____;
```

1. 用 `FROM` 和 `WHERE` 只选择 runtime 大于 180 分钟的电影。
2. 用 `GROUP BY` 把同一个年代的所有电影分为一组。
3. 用 `SELECT` 为每个年代创建像 `1920s` 这样的 string，并选出每个年代的电影数量。



```
CREATE table long_movies AS 
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

使用 Ok 来测试你的代码：

```
python3 ok -q long_movies

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

* [Attendance](index.html#attendance "index.html#attendance")
* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [SQL](index.html#sql "index.html#sql")
+ [IMDb](index.html#imdb "index.html#imdb")

- [Q1: Newest Movies](index.html#q1-newest-movies "index.html#q1-newest-movies")
- [Q2: Movies with Dogs](index.html#q2-movies-with-dogs "index.html#q2-movies-with-dogs")
- [Q3: Leads of Leads](index.html#q3-leads-of-leads "index.html#q3-leads-of-leads")
- [Q4: Long Movies](index.html#q4-long-movies "index.html#q4-long-movies")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
