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

*截止时间为 1 月 28 日（周三）晚上 11:59。*

Starter Files
-------------

下载 [lab00.zip](lab00/lab00.zip "lab00/lab00.zip")。

**本次 lab 对所有学生都是必修的，并计入你的 lab 成绩。**

Introduction
------------

本次 lab 讲解如何配置你的电脑以完成作业，并介绍一些 Python 基础知识。如果你需要任何帮助，请在 Ed 上发帖，或在你被分配到的 lab section 求助。

以下是本次 lab 的大纲：

* **配置**：设置本课程所需的必备软件。这需要若干组件，下面会列出。

  + **安装终端**：安装一个终端，这样你就能与本课程中的文件交互并运行 Ok 命令。
  + **安装 Python 3**：在你的电脑上安装 Python 3.8 或更高版本（最好是 Python 3.11 或更高版本）。
  + **安装文本编辑器**：安装用来编辑本课程 `.py` 文件的软件。几乎所有学生都使用 VS Code。
* **复习：你电脑的文件系统** 这里概述你电脑的文件系统是如何工作的，包括 absolute 和 relative file paths 的含义。
* **操作演示：使用终端**：这部分带你了解如何使用终端和 Python interpreter。
* **操作演示：整理你的文件**：这部分带你了解如何使用终端来整理和浏览本课程的文件。**每个人都应该阅读这一部分。**
* **必做：完成作业**：你必须完成这一部分才能获得作业学分。这部分的主要目标是让你练习使用我们的软件。
* **必做：提交作业**：提交你的工作。
* **附录：有用的 Python 命令行选项**：这些命令对调试你的工作很有用，但完成 lab 并不需要它们。我们收录它们，是因为它们很可能在整个课程中对你有所帮助。

Setup
-----

> 要配置你的设备，请选择与你操作系统对应的指南。

* **[Guide for Windows](../articles/setup-windows.html "../articles/setup-windows.html")**
* **[Guide for Mac & Linux](../articles/setup-mac.html "../articles/setup-mac.html")**

Your First Assignment
---------------------

> 做作业时，请确保你的终端的 working directory 是正确的（很可能就是你解压作业的位置）。

### 1) What Would Python Do? (WWPD)

lab 作业的一个组成部分是预测 Python interpreter 的行为。我们把这类题目称为 "What Would Python Do?"。

在本课程中，我们使用一个名为 `ok` 的程序来检验你的知识。每个作业都会附带 `ok`。让我们来看看如何用 `ok` 完成一道 WWPD 题目。

打开你的终端，并确保你位于包含本次作业解压后 lab 文件的 `lab00` 目录中。在该目录下输入 `ls`，确认存在以下文件：

* `lab00.py`：本 lab 的 starter file
* `ok`：我们的测试程序
* `lab00.ok`：`ok` 的配置文件

如果你没有看到这些文件，请用 `cd` 切换到正确的目录。

> 在没有 `ok` 的目录中尝试运行 `ok` 会产生错误。

在你的终端中输入以下内容，它会运行 `ok` 并开始这一部分：

```
python3 ok -q python-basics -u
```

> 命令 `python3 ok -q python-basics -u` 告诉 Python interpreter 运行当前 working directory 中名为 `ok` 的文件。
> `-q python-basics -u` 是提供给 `ok` 程序的输入，用于指明要运行哪道题。
>
> 如 setup 部分所述，如果 `python3` 命令无法运行，请尝试使用 `python` 或 `py`。

系统会提示你输入各种 statements/expressions 的输出。你必须正确输入才能继续，但答错没有惩罚。

第一次运行 Ok 时，系统会提示你输入 bCourses 邮箱。请按照[这些说明](../articles/using-ok.html#signing-in-with-ok "../articles/using-ok.html#signing-in-with-ok")操作。

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

在 VS Code 中打开整个 `lab00` 文件夹。你可以把该文件夹拖到 VS Code 应用上，或者打开 VS Code 并使用 `File` 菜单中的 `Open Folder...`。打开 `lab00` 文件夹后，你会在 VS Code 窗口左侧面板的文件浏览器中看到 `lab00.py` 文件。点击它开始编辑 `lab00.py`，这就是你要提交以获得 lab 学分的文件。

**重要**：在 VS Code 的 `File` 菜单中打开 `Auto Save`。这样每当你修改文件时，内容都会被保存。如果你没有启用 `Auto Save`，请务必经常保存你的工作。

**建议**：使用 VS Code 内置的终端（菜单中的 `Terminal > New Terminal`）。如果你按上面的说明在 VS Code 中打开了作业文件夹，那么 VS Code 终端的 working directory 会自动设为该作业文件夹，这意味着你无需切换目录就能检查你的工作。

现在完成这个 lab。你应该会看到一个名为 `twenty_twenty_six` 的 function，其中有一个空白的 `return` statement。这个空白是你唯一需要修改的部分。把它替换为一个求值为 2026 的 expression。你能想出最有创意的 expression 是什么？

### 3) Running Tests

我们还会用 `ok` 来测试你的代码。切换到终端。确保你位于包含 `ok` 和 `lab00.py` 的 `lab00` 目录中。

> **专业提示：** 如果你在 VS Code 中打开了 `lab00` 文件夹，并在 VS Code 的 `Terminal` 菜单中选择 `New Terminal`，那么终端会自动处于 `lab00` 目录中。

现在，用这个命令运行 `ok` 来测试你的代码：

```
python3 ok
```

> 记住，如果你使用的是 Windows 并且 `python3` 命令无法运行，请尝试只用 `python` 或 `py`。

如果你代码写得正确，并且完成了测试解锁，你应该会看到测试成功：

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

如果你没有通过测试，`ok` 会改为显示类似下面的内容：

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

在文本编辑器中修改你的代码，直到测试通过。

> 每次运行 `ok` 时，`ok` 都会尝试备份你的工作。如果它显示 "Connection timed out"，或者提示你未注册该课程，不必担心。你仍然可以提交这份作业并获得学分。

Submitting the Assignment
-------------------------

既然你已经完成了第一个作业，现在该提交它了。你可以按照以下步骤提交你的工作并获得分数。

> **重要：** 你只需要提交到 *Gradescope*；不需要提交到 *Ok*。

### Submit with Gradescope

1. 使用你的 CalNet ID，通过 **School Credentials** 登录 [Gradescope](https://www.gradescope.com/ "https://www.gradescope.com/")。登录后你会立即进入 **Dashboard**。

   ![Gradescope login page](lab00/assets/gradescope-loginscreen.png)
   ![select Calnet ID](lab00/assets/gradescope-login.png)
2. 在 **Dashboard** 上选择本课程。（你应该已经被添加到 Gradescope 了。如果没有，请在 Ed 上发一个私密帖。）这会带你进入课程中你可以提交的作业列表。在这个列表中，你会看到作业的状态、发布日期和截止日期。
3. 点击作业 Lab 0 将其打开。
4. 当对话框出现时，点击写着 **Drag & Drop** 的灰色区域。这会打开你的文件选择器，你应选择你为本次作业编辑的代码文件 `lab00.py`。

   ![gradescope submit](lab00/assets/gradescope-submit.png)
5. 选择文件后，点击 **Upload** 按钮。上传成功后，你会在屏幕上看到确认消息，并会收到一封邮件。

   ![gradescope upload](lab00/assets/gradescope-upload.png)
6. 接下来，等待几分钟让 autograder 批改你的代码文件。你的最终得分会出现在右侧，输出应与你本地测试的结果一致。你可以在右上角标有 **Code** 的标签页查看你提交的代码。如果有任何错误，你可以修改 `lab00.py` 代码，并点击屏幕底部的 **Resubmit** 重新提交你的代码文件。在截止日期之前，作业可以任意多次重新提交。

   ![gradescope results](lab00/assets/gradescope-results.png)

你对 WWPD 题目的回答不会提交到 Gradescope，也不需要提交。lab 学分基于代码编写题目。

**恭喜**，你刚刚提交了你的第一个作业！

Appendix: Useful Python Command Line Options
--------------------------------------------

以下是在文件上运行 Python 最常见的方式。

1. 不使用任何命令行选项会运行你提供的文件中的代码，然后返回到命令行。如果你的文件只包含 function definitions，那么除非有 syntax error，否则你不会看到任何输出。

   ```
   python3 lab00.py
   ```
2. **`-i`**：`-i` 选项会运行你提供的文件中的代码，然后打开一个交互式会话（带有 `>>>` prompt）。随后你可以求值 expressions，比如调用你定义的 functions。要退出，请输入 `exit()`。你也可以使用键盘快捷键：在 Linux/Mac 机器上按 `Ctrl-D`，在 Windows 上按 `Ctrl-Z Enter`。

   如果你在交互式运行 Python 文件时编辑了该文件，你需要退出并重新启动 interpreter，这些修改才会生效。

   下面是我们如何交互式地运行 `lab00.py`：

   ```
   python3 -i lab00.py
   ```
3. **`-m doctest`**：运行文件中的 doctests，也就是 functions 的 docstrings 中的示例。

   文件中的每个测试都由 `>>>` 加上一些 Python 代码和期望输出组成。

   下面是我们如何运行 `lab00.py` 中的 doctests：

   ```
    python3 -m doctest lab00.py
   ```

   当我们的代码通过所有 doctests 时，不会显示任何输出。否则，会显示关于失败测试的信息。

* [Introduction](lab00.html#introduction "lab00.html#introduction")
* [Setup](lab00.html#setup "lab00.html#setup")
* [Your First Assignment](lab00.html#your-first-assignment "lab00.html#your-first-assignment")

+ [1) What Would Python Do? (WWPD)](lab00.html#1-what-would-python-do-wwpd "lab00.html#1-what-would-python-do-wwpd")
+ [2) Implementing Functions](lab00.html#2-implementing-functions "lab00.html#2-implementing-functions")
+ [3) Running Tests](lab00.html#3-running-tests "lab00.html#3-running-tests")

* [Submitting the Assignment](lab00.html#submitting-the-assignment "lab00.html#submitting-the-assignment")

+ [Submit with Gradescope](lab00.html#submit-with-gradescope "lab00.html#submit-with-gradescope")

* [Appendix: Useful Python Command Line Options](lab00.html#appendix-useful-python-command-line-options "lab00.html#appendix-useful-python-command-line-options")
