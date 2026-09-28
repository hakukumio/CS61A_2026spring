Lab 0: Getting Started | CS 61A Spring 2026



[CS 61A](../index.html "../index.html")

* [Lectures](../index.html "../index.html")
* [Syllabus](../articles/about-61a/index.html "../articles/about-61a/index.html")
* [Ed](https://edstem.org/us/courses/93628/discussion "https://edstem.org/us/courses/93628/discussion")
* [Office Hours](../office-hours.html "../office-hours.html")
* [Contact](../articles/contact-61a/index.html "../articles/contact-61a/index.html")
* [Links](lab00.html# "lab00.html#")
  + [Request an Extension](https://go.cs61a.org/extensions "https://go.cs61a.org/extensions")
  + [Request a Regrade](https://go.cs61a.org/regrades "https://go.cs61a.org/regrades")
  + [Office Hours Queue](https://oh.cs61a.org/ "https://oh.cs61a.org/")
  + [Gradescope](https://www.gradescope.com/courses/1229052 "https://www.gradescope.com/courses/1229052")
  + [Add/Change Sections](https://sections.cs61a.org "https://sections.cs61a.org")
  + [Lecture Recordings](https://bcourses.berkeley.edu/courses/1547573/pages "https://bcourses.berkeley.edu/courses/1547573/pages")
  + [Python Tutor](https://pythontutor.com/cp/composingprograms.html "https://pythontutor.com/cp/composingprograms.html")
  + [Code Editors](https://code.cs61a.org/ "https://code.cs61a.org/")
* [Resources](lab00.html# "lab00.html#")
  + [Past Exams & Websites](../resources.html "../resources.html")
  + [Textbook](https://www.composingprograms.com "https://www.composingprograms.com")
  + [Campus Resources](../articles/campus-res/index.html "../articles/campus-res/index.html")
  + [Advice from Students](../articles/advice/index.html "../articles/advice/index.html")
  + [Scheme Specifications](../articles/scheme-spec/index.html "../articles/scheme-spec/index.html")
  + [Scheme Built-In Procedures](../articles/scheme-builtins/index.html "../articles/scheme-builtins/index.html")
* [Guides](lab00.html# "lab00.html#")
  + [Debugging Guide](https://drive.google.com/file/d/1O72u0ml65pibcjz-PXKpqeJDKaVqQ3D8/view "https://drive.google.com/file/d/1O72u0ml65pibcjz-PXKpqeJDKaVqQ3D8/view")
  + [Studying Guide](../articles/studying/index.html "../articles/studying/index.html")
  + [Type Hints](../articles/type-hints.html "../articles/type-hints.html")
  + [Composition Guide](../articles/composition/index.html "../articles/composition/index.html")
  + [MT1 Study Guide](../assets/pdfs/61a-mt1-study-guide.pdf "../assets/pdfs/61a-mt1-study-guide.pdf")
  + [MT2 Study Guide](../assets/pdfs/61a-mt2-study-guide.pdf "../assets/pdfs/61a-mt2-study-guide.pdf")
  + [Final Study Guide](../assets/pdfs/61a-final-study-guide.pdf "../assets/pdfs/61a-final-study-guide.pdf")
* [Staff](lab00.html# "lab00.html#")
  + [Instructors](../instructor.html "../instructor.html")
  + [TAs & Tutors](../staff.html "../staff.html")
  + [Teaching Interns](../teaching-interns.html "../teaching-interns.html")



Lab 0: Getting Started

* [lab00.zip](lab00/lab00.zip "lab00/lab00.zip")
========================================================================

*Due by 11:59pm on Wednesday, January 28.*

Starter Files
-------------

Download [lab00.zip](lab00/lab00.zip "lab00/lab00.zip").

**This lab is required for all students and counts toward your lab score.**

Introduction
------------

This lab explains how to setup your computer to complete assignments and
introduces some of the basics of Python. If you need any help, please post on Ed or ask for help at your assigned lab section.

Here's an outline of the lab:

* **Setup**: Setting up the essential software for the course. This will require several
  components, listed below.

  + **Install a Terminal**: Install a terminal so you can interact with files
    in this course and run OK commands.
  + **Install Python 3**: Install Python version 3.8 or later (ideally Python 3.11 or later) on your
    computer.
  + **Install a Text Editor**: Install software to edit `.py` files for this
    course. Almost all students use VS Code.
* **Review: Your Computer's File System** This is an overview of how your computer's file system
  works, including the meaning of both absolute and relative file paths.
* **Walkthrough: Using the Terminal**: This walks you through how to use the
  terminal and Python interpreter.
* **Walkthrough: Organizing your Files**: This section walks you through how to
  use your terminal to organize and navigate files for this course.
  **Everyone should read this section.**
* **Required: Doing the Assignment**: You must complete this section to get
  credit for the assignment. The main goal of this part is to give you practice using our
  software.
* **Required: Submitting the Assignment**: Turn in your work.
* **Appendix: Useful Python Command Line Options**: These are commands that are
  useful in debugging your work, but not required to complete the lab. We
  include them because they are likely to be helpful to you throughout
  the course.

Setup
-----

> To setup your device, select the guide that corresponds to your operating system.

* **[Guide for Windows](../articles/setup-windows.html "../articles/setup-windows.html")**
* **[Guide for Mac & Linux](../articles/setup-mac.html "../articles/setup-mac.html")**

Your First Assignment
---------------------

> When working on assignments, ensure that your terminal's working directory is correct (which is likely where you unzipped the assignment).

### 1) What Would Python Do? (WWPD)

One component of lab assignments is to predict how the Python interpreter will
behave. We call these questions "What Would Python Do?"

In this class, we use a program called `ok` to assess your knowledge.
`ok` will be included with every assignment. Let's go through
how to do a WWPD question with `ok`.

Open your terminal, and make sure you are in the `lab00` directory that contains
the unzipped lab files for this assignment. In that directory, type `ls` to verify
that there are the following files:

* `lab00.py`: the starter file for this lab
* `ok`: our testing program
* `lab00.ok`: a configuration file for `ok`

If you don't see these files, use `cd` to navigate to the correct directory.

> Attempting to run `ok` in a directory that does not have `ok` will produce an error.

Enter the following in your terminal, which will run `ok` and begin this section:

```
python3 ok -q python-basics -u
```

> The command `python3 ok -q python-basics -u` tells the Python interpreter
> to run the file with the name `ok` in the current working directory.
> `-q python-basics -u` are inputs provided to the `ok` program that identify
> which question to run.
>
> As stated in the setup section, if the `python3` command does not work,
> please try using `python` or `py`.

You will be prompted to enter the output of various statements/expressions.
You must enter them correctly to move on, but there is no penalty for
incorrect answers.

The first time you run Ok, you will be prompted for your bCourses email.
Please follow [these directions](../articles/using-ok.html#signing-in-with-ok "../articles/using-ok.html#signing-in-with-ok").

```
>>> x = 20
>>> x + 2

______



22

>>> x

______



20

>>> y = 5
>>> y = y + 3
>>> y * 2

______



16

>>> y + x

______



28
```

Toggle Solution (enable JavaScript)

### 2) Implementing Functions

Open the entire `lab00` folder in VS Code. You can drag the folder onto the VS
Code application or open VS Code and use `Open Folder...` in the `File` menu.
Once you open the `lab00` folder, you'll see the `lab00.py` file in the file
explorer on the left panel of your VS Code window. Click it to start editing
`lab00.py`, which is the file you will submit to receive credit for the lab.

**Important**: Turn on `Auto Save` in the `File` menu of VS Code. Then, whenever
you change a file, the contents will be saved. If you don't enable `Auto Save`,
be sure to frequently save your work.

**Recommended**: Use the terminal inside VS Code (`Terminal > New Terminal` in
the menu). If you opened the assignment folder in VS Code as instructed above,
then the VS Code terminal's working directory will automatically be set to the
assignment folder, which means you won't have to change directories to check
your work.

Now complete the lab. You should see a function called `twenty_twenty_six` that
has a blank `return` statement. That blank is the only part you should change.
Replace it with an expression that evaluates to 2026. What's the most creative
expression you can come up with?

### 3) Running Tests

We'll also use `ok` to test your code. Switch to the terminal. Make sure you are in the `lab00` directory that contains
`ok` and `lab00.py`.

> **Pro tip:** If you
> opened the `lab00` folder in VS Code and select `New Terminal` in the `Terminal`
> menu of VS Code, then the terminal will automatically be in the `lab00`
> directory.

Now, run `ok` with this command to test your code:

```
python3 ok
```

> Remember, if you are using Windows and the `python3` command does not work, please try using just
> `python` or `py`.

If you wrote your code correctly and you finished unlocking your tests, you should see a successful test:

```
=====================================================================
Assignment: Lab 0
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    2 test cases passed! No cases failed.
```

If you didn't pass the tests, `ok` will instead show you something like this:

```
---------------------------------------------------------------------
Doctests for twenty_twenty_six

>>> from lab00 import *
>>> twenty_twenty_six()
0

# Error: expected
#     2026
# but got
#     0

---------------------------------------------------------------------
Test summary
    0 test cases passed before encountering first failed test case
```

Fix your code in your text editor until the test passes.

> Every time you run `ok`, `ok` will try to back up your work. Don't worry if it
> says that the "Connection timed out" or that you're not enrolled in the
> course. You can still submit this assignment and get credit.

Submitting the Assignment
-------------------------

Now that you have completed your first assignment, it is time to turn it in. You can follow these next steps to submit your work and get points.

> **Important:** You only need to submit to *Gradescope*; you do not need to submit to *Ok*.

### Submit with Gradescope

1. Log in with **School Credentials** using your CalNet ID to [Gradescope](https://www.gradescope.com/ "https://www.gradescope.com/"). You’ll be taken to your **Dashboard** as soon as you log in.

   ![Gradescope login page](lab00/assets/gradescope-loginscreen.png)
   ![select Calnet ID](lab00/assets/gradescope-login.png)
2. On your **Dashboard**, select this course. (You should have already been added to Gradescope. If this is not the case, please make a private Ed post.) This will take you to the list of assignments in the course that you are able to submit. On this list, you will see the status of the assignment, the release date, and the due date.
3. Click on the assignment Lab 0 to open it.
4. When the dialog box appears, click on the gray area that says **Drag & Drop**. This will open your file finder and you should select your code file `lab00.py` that you edited for this assignment.

   ![gradescope submit](lab00/assets/gradescope-submit.png)
5. Once you have chosen your file select the **Upload** button. When your upload is successful, you’ll see a confirmation message on your screen and you will receive an email.

   ![gradescope upload](lab00/assets/gradescope-upload.png)
6. Next, wait a few minutes for the autograder to grade your code file. Your final score will appear at the right and your output should be the same as the one you tested locally. You can check the code that you submitted at the top right where there is a tab labeled **Code**. If there are any errors, you can edit your `lab00.py` code and click **Resubmit** at the bottom of your screen to resubmit your code file. Assignments can be resubmitted as many times as you would like before the deadline.

   ![gradescope results](lab00/assets/gradescope-results.png)

Your responses to WWPD questions are not submitted to Gradescope, and they do not need to be. Lab credit is based on code writing questions.

**Congratulations**, you just submitted your first assignment!

Appendix: Useful Python Command Line Options
--------------------------------------------

Here are the most common ways to run Python on a file.

1. Using no command-line options will run the code in the file you provide and
   return you to the command line. If your file just contains function
   definitions, you'll see no output unless there is a syntax error.

   ```
   python3 lab00.py
   ```
2. **`-i`**: The `-i` option runs the code in the file you provide, then opens
   an interactive session (with a `>>>` prompt). You can then evaluate
   expressions such as calling functions you defined. To exit, type
   `exit()`. You can also use the keyboard shortcut `Ctrl-D` on Linux/Mac
   machines or `Ctrl-Z Enter` on Windows.

   If you edit the Python file while running it interactively, you will need to
   exit and restart the interpreter in order for those changes to take effect.

   Here's how we can run `lab00.py` interactively:

   ```
   python3 -i lab00.py
   ```
3. **`-m doctest`**: Runs the doctests in a file, which are the examples in
   the docstrings of functions.

   Each test in the file consists of `>>>` followed by some Python code and
   the expected output.

   Here's how we can run the doctests in `lab00.py`:

   ```
    python3 -m doctest lab00.py
   ```

   When our code passes all of the doctests, no output is displayed. Otherwise,
   information about the tests that failed will be displayed.

* [Introduction](lab00.html#introduction "lab00.html#introduction")
* [Setup](lab00.html#setup "lab00.html#setup")
* [Your First Assignment](lab00.html#your-first-assignment "lab00.html#your-first-assignment")

+ [1) What Would Python Do? (WWPD)](lab00.html#1-what-would-python-do-wwpd "lab00.html#1-what-would-python-do-wwpd")
+ [2) Implementing Functions](lab00.html#2-implementing-functions "lab00.html#2-implementing-functions")
+ [3) Running Tests](lab00.html#3-running-tests "lab00.html#3-running-tests")

* [Submitting the Assignment](lab00.html#submitting-the-assignment "lab00.html#submitting-the-assignment")

+ [Submit with Gradescope](lab00.html#submit-with-gradescope "lab00.html#submit-with-gradescope")

* [Appendix: Useful Python Command Line Options](lab00.html#appendix-useful-python-command-line-options "lab00.html#appendix-useful-python-command-line-options")
