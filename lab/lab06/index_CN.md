Lab 6: OOP | CS 61A Spring 2026



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



Lab 6: OOP

* [lab06.zip](lab06.zip "lab06.zip")
================================================

*截止时间为 3 月 11 日（周三）晚上 11:59。*

Starter Files
-------------

下载 [lab06.zip](lab06.zip "lab06.zip")。

Attendance
==========

如果你参加的是常规 61A lab，你的 TA 会过来为你 check in。你除了到场之外，还需要提交 lab problems，才能获得本次 lab 的学分。如果你参加的是 mega lab，那么只需提交 lab problems 即可获得学分。

如果你因为正当理由（例如生病或时间冲突）缺席 lab，或者因为某些原因没有被 check in，只需在两周内填写[此表单](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance")即可获得 attendance 学分。

Required Questions
==================

> **注意：**
> 如果你的代码中遇到 **types** 相关的问题，请在你的 `lab06.py` 文件**最顶部**添加以下这一行：
>
> ```
> from __future__ import annotations
> ```
>
> 或者，你可以从课程网站**重新下载 lab06 文件夹**，以确保你拥有最新的文件。

Object-Oriented Programming
---------------------------

如果你需要复习 Object-Oriented Programming，请查阅下拉框。你也可以直接跳到题目部分，遇到困难时再回到这里查阅。

Object-Oriented Programming (enable JavaScript)

**Object-oriented programming**（OOP）使用 objects 和 classes 来组织程序。下面是 class 的一个例子：

```
class Car:
    max_tires = 4

    def __init__(self, color):
        self.tires = Car.max_tires
        self.color = color

    def drive(self):
        if self.tires < Car.max_tires:
            return self.color + ' car cannot drive!'
        return self.color + ' car goes vroom!'

    def pop_tire(self):
        if self.tires > 0:
            self.tires -= 1
```

**Class**：一个 object 的类型。`Car` class（如上所示）描述了所有 `Car` objects 的特征。

**Object**：一个 class 的单个实例。在 Python 中，通过调用一个 class 来创建新的 object。

```
>>> ferrari = Car('red')
```

这里，`ferrari` 是一个绑定到 `Car` object 的名字。

**Class attribute**：属于某个 class 的变量，通过点号记法访问。`Car` class 有一个 `max_tires` attribute。

```
>>> Car.max_tires
4
```

**Instance attribute**：属于某个特定 object 的变量。每个 `Car` object 都有一个 `tires` attribute 和一个 `color` attribute。与 class attributes 一样，instance attributes 也是通过点号记法访问的。

```
>>> ferrari.color
'red'
>>> ferrari.tires
4
>>> ferrari.color = 'green'
>>> ferrari.color
'green'
```

**Method**：属于某个 object 的 function，通过点号记法调用。按照惯例，method 的第一个参数是 `self`。

当一个 object 的某个 method 被调用时，该 object 会被隐式地作为 `self` 的参数传入。例如，`ferrari` object 的 `drive` method 调用时括号内为空，因为 `self` 被隐式绑定到了 `ferrari` object。

```
>>> ferrari = Car('red')
>>> ferrari.drive()
'red car goes vroom!'
```

我们也可以调用原始的 `Car.drive` function。原始 function 并不属于任何特定的 `Car` object，所以我们必须为 `self` 显式提供一个参数。

```
>>> ferrari = Car('red')
>>> Car.drive(ferrari)
'red car goes vroom!'
```

**\_\_init\_\_**：一个特殊的 function，在创建 class 的新实例时会被自动调用。

注意 `drive` method 接收 `self` 作为参数，但看起来我们并没有传入它！这是因为点号记法为我们*隐式地*把 `ferrari` 作为 `self` 传入。所以在这个例子中，`self` 在 global frame 中被绑定到名为 `ferrari` 的 object。

要求值表达式 `Car('red')`，Python 会创建一个新的 `Car` object。然后，Python 调用 `Car` class 的 `__init__` function，其中 `self` 绑定到新 object，`color` 绑定到 `'red'`。

### Q1: Bank Account

扩展 `BankAccount` class，添加一个 `transactions` attribute。这个 attribute 应该是一个 list，用于记录账户上发生的每一笔交易。每当 `deposit` 或 `withdraw` method 被调用时，都应创建一个新的 `Transaction` 实例并将其加入该 list，**即使操作没有成功**。

一个 `Transaction` class 的实例应具有以下 attributes：

* `before`：交易前的账户余额。
* `after`：交易后的账户余额。
* `id`：交易 ID，即该账户之前发生的交易（存款或取款）数量。特定 `BankAccount` 实例的交易 ID 必须唯一，但这个 `id` 不需要在所有账户之间唯一。换句话说，你只需确保同一个 `BankAccount` 创建的两个 `Transaction` object 没有相同的 `id`。

此外，`Transaction` class 还应具有以下 methods：

* `changed()`：如果余额发生了变化（即 `before` 与 `after` 不同）则返回 `True`，否则返回 `False`。
* `report()`：返回一个描述该交易的 string。该 string 应以交易 ID 开头，并描述余额的变化。预期输出请查看 doctests。

```
class Transaction:
    def __init__(self, id: int, before: int, after: int):
        self.id = id
        self.before = before
        self.after = after

    def changed(self) -> bool:
        """Return whether the transaction resulted in a changed balance."""
        "*** YOUR CODE HERE ***"

    def report(self) -> str:
        """Return a string describing the transaction.

        >>> Transaction(3, 20, 10).report()
        '3: decreased 20->10'
        >>> Transaction(4, 20, 50).report()
        '4: increased 20->50'
        >>> Transaction(5, 50, 50).report()
        '5: no change'
        """
        msg: str = 'no change'
        if self.changed():
            "*** YOUR CODE HERE ***"
        return str(self.id) + ': ' + msg

class BankAccount:
    """A bank account that tracks its transaction history.

    >>> a = BankAccount('Eric')
    >>> a.deposit(100)    # Transaction 0 for a
    100
    >>> b = BankAccount('Erica')
    >>> a.withdraw(30)    # Transaction 1 for a
    70
    >>> a.deposit(10)     # Transaction 2 for a
    80
    >>> b.deposit(50)     # Transaction 0 for b
    50
    >>> b.withdraw(10)    # Transaction 1 for b
    40
    >>> a.withdraw(100)   # Transaction 3 for a
    'Insufficient funds'
    >>> len(a.transactions)
    4
    >>> len([t for t in a.transactions if t.changed()])
    3
    >>> for t in a.transactions:
    ...     print(t.report())
    0: increased 0->100
    1: decreased 100->70
    2: increased 70->80
    3: no change
    >>> b.withdraw(100)   # Transaction 2 for b
    'Insufficient funds'
    >>> b.withdraw(30)    # Transaction 3 for b
    10
    >>> for t in b.transactions:
    ...     print(t.report())
    0: increased 0->50
    1: decreased 50->40
    2: no change
    3: decreased 40->10
    """

    # *** YOU NEED TO MAKE CHANGES IN SEVERAL PLACES IN THIS CLASS ***

    def __init__(self, account_holder: str):
        self.balance: int = 0
        self.holder = account_holder

    def deposit(self, amount: int) -> int:
        """Increase the account balance by amount, add the deposit
        to the transaction history, and return the new balance.
        """
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount: int) -> int | str:
        """Decrease the account balance by amount, add the withdraw
        to the transaction history, and return the new balance.
        """
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
```

使用 Ok 来测试你的代码：

```
python3 ok -q BankAccount

Copy

✂️
```

  

### Q2: Email

一个 email 系统有三个 classes：`Email`、`Server` 和 `Client`。一个 `Client` 可以 `compose` 一封 email，然后把它 `send` 给 `Server`。`Server` 再把它投递到另一个 `Client` 的 `inbox`。为了实现这一点，`Server` 有一个名为 `clients` 的 dictionary，把 `Client` 的名字映射到 `Client` 实例。

假设一个 `Client` 从不更换它使用的 `Server`，并且它只能使用那个 `Server` 来 compose 一封 `Email`。

填写下面的定义来完成实现！`Email` class 已经为你完成了。

> **重要**：在开始之前，请务必阅读整个代码片段，理解这些 classes 之间的关系，并注意各 methods 的参数类型。想想每个 method 中你可以访问哪些变量，以及如何用它们来访问其他 classes 及其 methods。

> **注意：**
>
> * `Email` class 中 `__init__(self, msg, sender, recipient_name)` method 的 `sender` 参数是一个 `Client` 实例。
> * `Server` class 中 `register_client(self, client)` method 的 `client` 参数是一个 `Client` 实例。
> * `Server` class 中 `send(self, email)` method 的 `email` 参数是一个 `Email` 实例。

```
class Email:
    """An email has the following instance attributes:

        msg (str): the contents of the message
        sender (Client): the client that sent the email
        recipient_name (str): the name of the recipient (another client)
    """
    def __init__(self, msg: str, sender, recipient_name: str):
        self.msg = msg
        self.sender = sender
        self.recipient_name = recipient_name

class Server:
    """Each Server has one instance attribute called clients that is a
    dictionary from client names to client objects.

    >>> s = Server()
    >>> # Dummy client class implementation for testing only
    >>> class Client:
    ...     def __init__(self, server, name):
    ...         self.inbox = []
    ...         self.server = server
    ...         self.name = name
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> s.register_client(a) 
    >>> s.register_client(b)
    >>> len(s.clients)  # we have registered 2 clients
    2
    >>> all([type(c) == str for c in s.clients.keys()])  # The keys in self.clients should be strings
    True
    >>> all([type(c) == Client for c in s.clients.values()])  # The values in self.clients should be Client instances
    True
    >>> new_a = Client(s, 'Alice')  # a new client with the same name as an existing client
    >>> s.register_client(new_a)
    >>> len(s.clients)  # the key of a dictionary must be unique
    2
    >>> s.clients['Alice'] is new_a  # the value for key 'Alice' should now be updated to the new client new_a
    True
    >>> e = Email("I love 61A", b, 'Alice')
    >>> s.send(e)
    >>> len(new_a.inbox)  # one email has been sent to new Alice
    1
    >>> type(new_a.inbox[0]) == Email  # a Client's inbox is a list of Email instances
    True
    """
    def __init__(self):
        self.clients = {}

    def send(self, email: Email):
        """Append the email to the inbox of the client it is addressed to.
            email is an instance of the Email class.
        """
        ____.inbox.append(email)

    def register_client(self, client):
        """Add a client to the clients mapping (which is a 
        dictionary from client names to client instances).
            client is an instance of the Client class.
        """
        ____[____] = ____

class Client:
    """A client has a server, a name (str), and an inbox (list).

    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    >>> b.inbox[1].sender.name
    'Alice'
    """
    def __init__(self, server: Server, name: str):
        self.inbox: list = []
        self.server = server
        self.name = name
        server.register_client(____)

    def compose(self, message: str, recipient_name: str):
        """Send an email with the given message to the recipient."""
        email = Email(message, ____, ____)
        self.server.send(email)
```

> 这道题有两个 `ok` 测试。必须两个测试都通过才能获得满分。
> 你应按它们出现的顺序运行它们。
> `python3 ok -q Server` 测试会测试 `Server` class 的实现，它不要求 `Client` class 有正确的实现。
> `python3 ok -q Client` 测试会同时测试 `Server` 和 `Client` class 的实现。
> 因此，在测试 `Client` class 之前，请务必先测试你的 `Server` class 实现。

使用 Ok 来测试你的代码：

```
python3 ok -q Server
python3 ok -q Client

Copy

✂️
```

  

Inheritance
-----------

两个 classes 可能有相似的 attributes，但其中一个表示另一个的特殊情况。例如，`Nickel` 是 `Coin` 的一个特殊情况。我们说 `Nickel` 是 `Coin` 的 subclass，而 `Coin` 是 `Nickel` 的 base class（或 superclass）。在 Python 中，`class Nickel(Coin):` 这一行建立了这种关系。

```
class Coin:
    cents = None  # This will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

class Nickel(Coin):
    cents = 5
```

`Coin` 的 methods（例如 `__init__`）也是 `Nickel` 的 methods。所以，例如每个 `Nickel` 实例都有一个 `year` attribute。但在 `Nickel` class 中定义的 class attributes 或 methods 会被优先找到。

```
>>> c = Nickel(1990)
>>> c.year
1990
>>> c.cents
5
```

### Q3: Mint

mint 是制造硬币的地方。在这道题中，你将实现一个 `Mint` class，它可以输出带有正确 year 和 worth 的 `Coin`。

* 每个 `Mint` 实例都有一个 `year` stamp。`update` method 会把该实例的 `year` stamp 设置为 `Mint` *class* 的 `present_year` class attribute。
* `create` method 接收 `Coin` 的一个 subclass（*不是*实例！），然后创建并返回该 subclass 的一个实例，并印上该 `Mint` 的 year（如果该 mint 尚未 update，这可能与 `Mint.present_year` 不同）。
* `Coin` 的 `worth` method 返回该硬币的 `cents` 值，再加上年龄超过 50 岁后每多一岁一分的额外 cent。硬币的年龄可以通过用 `Mint` class 的 `present_year` class attribute 减去硬币的 year 来确定。

```
class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2025
    >>> dime = mint.create(Dime)
    >>> dime.year
    2025
    >>> Mint.present_year = 2105  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2025
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2105
    >>> Mint.present_year = 2180     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2025

    def __init__(self):
        self.update()

    def create(self, coin):
        "*** YOUR CODE HERE ***"

    def update(self) -> None:
        "*** YOUR CODE HERE ***"

class Coin:
    cents = None # will be provided by subclasses, but not by Coin itself

    def __init__(self, year: int):
        self.year = year

    def worth(self) -> int:
        "*** YOUR CODE HERE ***"

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10
```

使用 Ok 来测试你的代码：

```
python3 ok -q Mint

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

Optional Questions
==================

> 这些题目是可选的。如果你没有完成它们，你仍然会获得这份作业的学分。它们是很好的练习，所以还是做一做吧！

### Q4: Next Virahanka Fibonacci Object

实现 `VirFib` class 的 `next` method。对于这个 class，`value` attribute 是一个 Fibonacci number。`next` method 返回一个 `VirFib` 实例，其 `value` 是下一个 Fibonacci number。`next` method 只能花费常数时间。

注意，在 doctests 中并没有打印任何内容。相反，每次调用 `.next()` 都会返回一个 `VirFib` 实例。每个 `VirFib` 实例的显示方式由它的 `__repr__` method 的返回值决定。

> *提示*：通过在 `next` 内部设置一个新的 instance attribute 来记录前一个数字。你可以在任何时候为 objects 创建新的 instance attributes，即使是在 `__init__` method 之外。

```
class VirFib():
    """A Virahanka Fibonacci number.

    >>> start = VirFib()
    >>> start
    VirFib object, value 0
    >>> start.next()
    VirFib object, value 1
    >>> start.next().next()
    VirFib object, value 1
    >>> start.next().next().next()
    VirFib object, value 2
    >>> start.next().next().next().next()
    VirFib object, value 3
    >>> start.next().next().next().next().next()
    VirFib object, value 5
    >>> start.next().next().next().next().next().next()
    VirFib object, value 8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    VirFib object, value 8
    """

    def __init__(self, value: int = 0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"

    def __repr__(self) -> str:
        return "VirFib object, value " + str(self.value)
```

使用 Ok 来测试你的代码：

```
python3 ok -q VirFib

Copy

✂️
```

* [Attendance](index.html#attendance "index.html#attendance")
* [Required Questions](index.html#required-questions "index.html#required-questions")

+ [Object-Oriented Programming](index.html#object-oriented-programming "index.html#object-oriented-programming")

- [Q1: Bank Account](index.html#q1-bank-account "index.html#q1-bank-account")
- [Q2: Email](index.html#q2-email "index.html#q2-email")

+ [Inheritance](index.html#inheritance "index.html#inheritance")

- [Q3: Mint](index.html#q3-mint "index.html#q3-mint")

+ [Check Your Score Locally](index.html#check-your-score-locally "index.html#check-your-score-locally")

* [Submit Assignment](index.html#submit-assignment "index.html#submit-assignment")
* [Optional Questions](index.html#optional-questions "index.html#optional-questions")

+ [Q4: Next Virahanka Fibonacci Object](index.html#q4-next-virahanka-fibonacci-object "index.html#q4-next-virahanka-fibonacci-object")
