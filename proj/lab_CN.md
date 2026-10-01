Optional Contest: Scheme Art | CS 61A Spring 2026



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



Optional Contest: Scheme Art

* [scheme\_contest.zip](scheme_contest.zip "scheme_contest.zip")
==============================================================================================

> 输出即艺术，  
> 但源代码呢？  
> 同样抽象。

Instructions
------------

> 本次竞赛完全自愿参加！

以下是参加竞赛的步骤：

1. 下载 [scheme\_contest.zip](scheme_contest.zip "scheme_contest.zip")。
2. 从[此链接](../../assets/interpreter/abstract_turtle.zip "../../assets/interpreter/abstract_turtle.zip")下载 `abstract_turtle.zip` 文件。然后，把该文件解压到你的 `scheme_contest` 目录中。解压后的文件夹应包含 `canvas.py` 和 `color_names.py` 等文件。或者，如果你更愿意用 `pip` 命令安装，可以改为运行 `pip3 install abstract-turtle`，而不用下载这个 zip 文件。
3. 完成 `contest.scm` 文件（你可以用 `python3 scheme contest.scm --pillow-turtle --turtle-save-path output` 渲染你的画作）。关于绘图 procedures 的说明，请参见 [Scheme Built-in Reference on graphics](../../articles/scheme-builtins/index.html#turtle-graphics "../../articles/scheme-builtins/index.html#turtle-graphics")。

   * 如果这个命令不起作用，可以改试 `python3 scheme contest.scm --turtle-save-path output`。主要区别是：这个命令使用 `tkinter` library，而前一个命令使用 `pillow` library。两者应生成相同的输出。
4. 把上一个命令生成的 `output.png` 上传到 postimages.org。

**这学期允许动画！提交动画 png/gif。**

在 `contest.scm` 中，`draw` procedure 应绘制你的参赛作品，然后在点击时退出。

所有参赛作品（包括其源代码）都会分发给你的同学们投票。请**不要在提交内容中包含个人信息。**

> **重要：**当准备好提交时，请**同时**执行以下两步：
>
> * 把你的 `contest.scm` 文件提交到 Gradescope 上的 **Scheme Contest** 作业。
> * 填写[竞赛表单](https://forms.gle/9nyeYacstuJsG56a7 "https://forms.gle/9nyeYacstuJsG56a7")。请确保这里的信息正确，因为我们会用它来生成你在 Scheme art gallery 中的参赛条目。
>
> **Troubleshooting：**
> 你在尝试渲染作品时遇到 `name 'builtins' is not defined` 错误了吗？
> 如果是，请在 `scheme_builtins.py` 顶部添加以下行：`import builtins`。
> 尝试渲染你的图像时，你可能还会被要求安装一些 dependencies，如果安装了，
> 应该就能正确生成你的可视化。如果你没有看到这个错误（它通常只出现在部分 Windows 用户那里），
> 则不需要添加这个额外的 import。

Contest Description
-------------------

使用 turtle graphics，为你选择的一个迭代或递归过程创建可视化或动画。你的实现必须完全用 Scheme 编写，并使用你构建的 interpreter。所有计算都必须在 Scheme 中完成。

提交作品将分为两个类别：

* *Featherweight*：少于 512 个 Scheme tokens（包括括号）
* *Heavyweight*：少于 4096 个 Scheme tokens（包括括号）



**任何单个 token 都不得超过 1000 个字符。**

你可以通过运行以下命令来检查名为 `contest.scm` 的 Scheme 文件中的 tokens 数量：

```
python3 scheme_tokens.py contest.scm
```

参赛作品（代码和图像）将发布在网上，获奖者由大众投票选出。投票结束后，每个类别的前三名将在 Ed 上公布。

为了提高获胜的机会，欢迎你在参赛作品的注释中包含一个标题和一首描述性的 [haiku](http://en.wikipedia.org/wiki/Haiku "http://en.wikipedia.org/wiki/Haiku")，它们会被纳入投票。

Contest Rules
-------------

提交之前，请确保你的参赛作品遵守以下准则：

* 参赛作品不得包含超过 1000 个字符的 tokens，并且必须提交到正确的类别（featherweight/heavyweight）。
* 参赛作品不得包含任何政治内容。
* 参赛作品不得包含任何冒犯性、色情或道德上有争议的内容。
* 参赛作品不得包含任何个人信息。
* 参赛作品必须与你的代码一致。也就是说，你提交的 Scheme 代码必须能够精确生成你提交的输出图像文件。

我们保留取消任何不遵守这些准则的参赛作品资格的权利。

Past Entries
------------

为了寻找灵感，你可以浏览这些往届参赛作品画廊。请注意，某些提交可能不符合当前准则。

* [Fall 2025](http://inst.eecs.berkeley.edu/~cs61a/fa25/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa25/proj/scheme_gallery/")
* [Spring 2025](http://inst.eecs.berkeley.edu/~cs61a/sp25/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/sp25/proj/scheme_gallery/")
* [Fall 2024](http://inst.eecs.berkeley.edu/~cs61a/fa24/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa24/proj/scheme_gallery/")
* [Summer 2024](http://inst.eecs.berkeley.edu/~cs61a/su24/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/su24/proj/scheme_gallery/")
* [Spring 2024](http://inst.eecs.berkeley.edu/~cs61a/sp24/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/sp24/proj/scheme_gallery/")
* [Fall 2022](http://inst.eecs.berkeley.edu/~cs61a/fa22/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa22/proj/scheme_gallery/")
* [Summer 2022](http://inst.eecs.berkeley.edu/~cs61a/su22/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/su22/proj/scheme_gallery/")
* [Fall 2023](http://inst.eecs.berkeley.edu/~cs61a/fa23/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa23/proj/scheme_gallery/")
* [Summer 2023](http://inst.eecs.berkeley.edu/~cs61a/su23/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/su23/proj/scheme_gallery/")
* [Spring 2023](http://inst.eecs.berkeley.edu/~cs61a/sp23/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/sp23/proj/scheme_gallery/")
* [Fall 2022](http://inst.eecs.berkeley.edu/~cs61a/fa22/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa22/proj/scheme_gallery/")
* [Summer 2022](http://inst.eecs.berkeley.edu/~cs61a/su22/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/su22/proj/scheme_gallery/")
* [Spring 2022](http://inst.eecs.berkeley.edu/~cs61a/sp22/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/sp22/proj/scheme_gallery/")
* [Fall 2021](http://inst.eecs.berkeley.edu/~cs61a/fa21/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa21/proj/scheme_gallery/")
* [Summer 2021](http://inst.eecs.berkeley.edu/~cs61a/su21/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/su21/proj/scheme_gallery/")
* [Spring 2021](http://inst.eecs.berkeley.edu/~cs61a/sp21/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/sp21/proj/scheme_gallery/")
* [Fall 2020](http://inst.eecs.berkeley.edu/~cs61a/fa20/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa20/proj/scheme_gallery/")
* [Summer 2020](http://inst.eecs.berkeley.edu/~cs61a/su20/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/su20/proj/scheme_gallery/")
* [Spring 2020](http://inst.eecs.berkeley.edu/~cs61a/sp20/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/sp20/proj/scheme_gallery/")
* [Fall 2019](http://inst.eecs.berkeley.edu/~cs61a/fa19/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa19/proj/scheme_gallery/")
* [Summer 2019](http://inst.eecs.berkeley.edu/~cs61a/su19/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/su19/proj/scheme_gallery/")
* [Spring 2019](http://inst.eecs.berkeley.edu/~cs61a/sp19/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/sp19/proj/scheme_gallery/")
* [Fall 2018](http://inst.eecs.berkeley.edu/~cs61a/fa18/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa18/proj/scheme_gallery/")
* [Summer 2018](http://inst.eecs.berkeley.edu/~cs61a/su18/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/su18/proj/scheme_gallery/")
* [Spring 2018](http://inst.eecs.berkeley.edu/~cs61a/sp18/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/sp18/proj/scheme_gallery/")
* [Fall 2017](http://inst.eecs.berkeley.edu/~cs61a/fa17/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa17/proj/scheme_gallery/")
* [Summer 2017](http://inst.eecs.berkeley.edu/~cs61a/su17/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/su17/proj/scheme_gallery/")
* [Spring 2017](http://inst.eecs.berkeley.edu/~cs61a/sp17/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/sp17/proj/scheme_gallery/")
* [Fall 2016](http://inst.eecs.berkeley.edu/~cs61a/fa16/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa16/proj/scheme_gallery/")
* [Summer 2016](http://inst.eecs.berkeley.edu/~cs61a/su16/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/su16/proj/scheme_gallery/")
* [Spring 2016](http://inst.eecs.berkeley.edu/~cs61a/sp16/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/sp16/proj/scheme_gallery/")
* [Fall 2015](http://inst.eecs.berkeley.edu/~cs61a/fa15/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa15/proj/scheme_gallery/")
* [Spring 2015](http://inst.eecs.berkeley.edu/~cs61a/sp15/proj/scheme-gallery/ "http://inst.eecs.berkeley.edu/~cs61a/sp15/proj/scheme-gallery/")
* [Fall 2014](http://inst.eecs.berkeley.edu/~cs61a/fa14/proj/scheme_gallery/ "http://inst.eecs.berkeley.edu/~cs61a/fa14/proj/scheme_gallery/")
* [Spring 2014](http://inst.eecs.berkeley.edu/~cs61a/sp14/proj/scheme_contest/scheme_contest.html "http://inst.eecs.berkeley.edu/~cs61a/sp14/proj/scheme_contest/scheme_contest.html")
* [Fall 2013](http://inst.eecs.berkeley.edu/~cs61a/fa13/proj/scheme_contest_gallery/scheme_contest_gallery.html "http://inst.eecs.berkeley.edu/~cs61a/fa13/proj/scheme_contest_gallery/scheme_contest_gallery.html")
* [Spring 2013](http://inst.eecs.berkeley.edu/~cs61a/sp13/projects/scheme_contest_gallery/scheme_contest.html "http://inst.eecs.berkeley.edu/~cs61a/sp13/projects/scheme_contest_gallery/scheme_contest.html")
* [Fall 2012](http://inst.eecs.berkeley.edu/~cs61a/fa12/projects/scheme_contest.html "http://inst.eecs.berkeley.edu/~cs61a/fa12/projects/scheme_contest.html")

* [Instructions](index.html#instructions "index.html#instructions")
* [Contest Description](index.html#contest-description "index.html#contest-description")
* [Contest Rules](index.html#contest-rules "index.html#contest-rules")
* [Past Entries](index.html#past-entries "index.html#past-entries")
