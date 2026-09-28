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

*Due by 11:59pm on Friday, May 1*

Instructions
------------

Download [hw10.zip](hw10.zip "hw10.zip").

**Submission:** When you are done, submit the assignment to Gradescope. You may submit more than once before the deadline; only the
final submission will be scored. Check that you have successfully submitted
your code on Gradescope.
See [Lab 0](../../lab/lab00.html "../../lab/lab00.html") for more instructions on submitting assignments.

**Using Ok:** If you have any questions about using Ok, please
refer to [this guide.](../../articles/using-ok.html "../../articles/using-ok.html")

**Grading:** Homework is graded based on
correctness. Each incorrect problem will decrease the total score by one point.
**This homework is out of 2 points.**
  

To check your progress, you can run `sqlite3` directly by running:

```
python3 sqlite_shell.py --init hw10.sql
```

You should also check your work using `ok`:

```
python3 ok
```

Visualizing SQL
---------------

The CS61A SQL Web Interpreter is a great tool for visualizing and debugging SQL statements!

To get started, visit [code.cs61a.org](https://code.cs61a.org "https://code.cs61a.org") and hit `Start SQL interpreter` on the launch screen.

Most tables used in assignments are already available for use, so let's try to execute a `SELECT` statement:

![](assets/visualize-sql-eg1.png)

In addition to displaying a visual representation of the output table, the "Step-by-step" button lets us step through the SQL execution and visualize every transformation that takes place. For our example, clicking on the next arrow will produce the following visuals, demonstrating exactly how SQL is grouping our rows to form the final output!

Show output (enable JavaScript)

![](assets/visualize-sql-eg2.png)

Required Questions
==================

SQL
---

### Dog Data

In each question below, you will define a new table based on the following
tables about dogs.

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

The `parents` table contains one row for each parent-child relationship; for example,
the first row describes that the dog `"ace"` is the parent of the dog `"bella"`.
The `dogs` table contains the name, fur type, and height for each dog. The `sizes`
table has one row for each classification of dog. A dog matches a particular
classification if its height is greater than `min` and less than or equal to `max`.

Your queries should still perform correctly *even if the values in these tables
change*. For example, if you are asked to list all dogs with a name that starts
with `h`, you should write:

```
SELECT name FROM dogs WHERE name LIKE "h%";
```

The `%` sign matches any number of characters, and patterns in `sqlite` are case in-sensitive, so the pattern `"h%"` matches all strings that begin with `h` or `H`. This query would still be correct if a row was added with the name `harry`. Contrastingly, writing a query like `SELECT "hank";` would not, and only works for the example input.

### Q1: By Parent Height

Create a table `by_parent_height` that has a column of the names of all dogs that have
a `parent`, ordered by the height of the parent dog from tallest parent to shortest
parent.

```
-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

For example, `finn` has a parent `ellie` with height 35, and so
should appear before `ginger` who has a parent `finn` with height 32.
The names of dogs with parents of the same height should appear together in any
order. For example, `bella` and `charlie` should both appear at the end, but
either one can come before the other.

For our example tables, the `by_parent_height` table should look like this:

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

Use Ok to test your code:

```
python3 ok -q by_parent_height

Copy

✂️
```

  


### Q2: Size of Dogs

The Fédération Cynologique Internationale classifies a standard poodle as over
45 cm and up to 60 cm. The `sizes` table describes this and other such
classifications, where a dog must be over the `min` and less than or equal to
the `max` in `height` to qualify as `size`.

Create a `size_of_dogs` table with two columns, one for each dog's `name` and
another for its `size`.

```
-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

The `size_of_dogs` table should look like this:

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

Use Ok to test your code:

```
python3 ok -q size_of_dogs

Copy

✂️
```

  


### Q3: Sentences

Siblings are pairs of dogs that have the same parent. Create a table that
contains a row for each pair of siblings that have the same size classification,
with a single column that contains a sentence describing the siblings by their size.

```
-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

Each sibling pair should appear only once in the output, and siblings should be
listed in alphabetical order (e.g. `"bella and charlie..."` instead of
`"charlie and bella..."`), as follows:

```
sqlite> SELECT * FROM sentences;
The two siblings, bella and charlie, have the same size: standard
The two siblings, ace and ginger, have the same size: toy
```

> **Hint**: First, create a helper table containing the names of each pair of siblings. This
> will make comparing the sizes of siblings when constructing the main table
> easier. Make sure to not pair a child with themselves and do not include duplicate pairs.
>
> **Hint**: If you join a table with itself, use `AS` within the `FROM` clause to
> give each table an alias.
>
> **Hint**: In order to concatenate two strings into one, use the `||` operator, e.g. `SELECT "hello" || "world";` will return `helloworld`.

Use Ok to test your code:

```
python3 ok -q sentences

Copy

✂️
```

  

### Q4: Low Variance

We want to create a table that contains the *height range* (defined as the difference between maximum and minimum `height`) of all dogs that share a `fur` type. However, we'll only
consider `fur` types where each dog with that `fur` type is within 30% of the average `height` of all dogs with that `fur` type; we call this the *low variance* criterion.

For example, if the average `height` for short-haired dogs is 10, then in order to be included in our
output, all dogs with short hair must have a `height` of at most 13 and at least 7 (*inclusive*).

> **Hint**: `MIN`, `MAX`, and `AVG` will be useful here.
>
> **Hint**: You may want to first find the average height and make sure that:
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

Your output should have two columns, in this order: the `fur` type and the `height_range` for the `fur` types that meet this criteria. For the example tables, it should look like this:

```
+------------+--------------+
| fur        | height_range |
+------------+--------------+
| Curly      | 1            |
+------------+--------------+
```

Explanation (enable JavaScript)

The average height of long-haired dogs is 39.7, so the low variance criterion requires the height of each long-haired dog to be between 27.8 and 51.6. However, `ace` is a long-haired dog with height 26, which is outside this range. For short-haired dogs, `bella` falls outside the valid range (check!). Thus, neither short nor long haired dogs are included in the output. There are two curly haired dogs: `finn` with height 32 and `hank` with height 31. This gives a height range of 1.

Use Ok to test your code:

```
python3 ok -q low_variance

Copy

✂️
```

  

Submit Assignment
=================

Submit this assignment by uploading any files you've edited **to the appropriate Gradescope assignment.** [Lab 00](../../lab/lab00.html "../../lab/lab00.html") has detailed instructions.

Make sure to submit `hw10.sql` to the autograder!

Exam Practice
-------------

The following are some SQL exam problems from previous semesters that you may find useful as additional exam practice.

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
