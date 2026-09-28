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

*Due by 11:59pm on Wednesday, March 11.*

Starter Files
-------------

Download [lab06.zip](lab06.zip "lab06.zip").

Attendance
==========

If you are in a regular 61A lab, your TA will come around and check you in. You need to submit the lab problems in addition to attending to get credit for lab. If you are in the mega lab, you only need to submit the lab problems to get credit.

If you miss lab for a good reason (such as sickness or a scheduling conflict) or you don't get checked in for some reason, just fill out [this form](http://go.cs61a.org/lab-attendance "http://go.cs61a.org/lab-attendance") within two weeks to receive attendance credit.

Required Questions
==================

> **Note:**
> If you are facing issues with **types** in your code, add the following line **at the very top** of your `lab06.py` file:
>
> ```
> from __future__ import annotations
> ```
>
> Alternatively, you can **redownload the lab06 folder** from the course website to ensure you have the latest files.

Object-Oriented Programming
---------------------------

Here's a refresher on Object-Oriented Programming. It's okay to skip directly to
the questions and refer back here if you get stuck.

Object-Oriented Programming (enable JavaScript)

**Object-oriented programming** (OOP) uses objects and classes to organize programs. Here's an example of a class:

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

**Class**: The type of an object. The `Car` class (shown above) describes the characteristics of all `Car`
objects.

**Object**: A single instance of a class. In Python, a new object is created by
calling a class.

```
>>> ferrari = Car('red')
```

Here, `ferrari` is a name bound to a `Car` object.

**Class attribute**: A variable that belongs to a class and is accessed via dot notation. The `Car` class has a `max_tires` attribute.

```
>>> Car.max_tires
4
```

**Instance attribute**: A variable that belongs to a particular object. Each `Car` object has a `tires` attribute and a `color` attribute. Like class attributes, instance attributes are accessed via dot notation.

```
>>> ferrari.color
'red'
>>> ferrari.tires
4
>>> ferrari.color = 'green'
>>> ferrari.color
'green'
```

**Method**: A function that belongs to an object and is called via dot notation. By convention, the first parameter of a method is `self`.

When one of an object's methods is called, the object is implicitly provided as the argument for `self`. For example, the `drive` method of the `ferrari` object is called with empty parentheses because `self` is implicitly bound to the `ferrari` object.

```
>>> ferrari = Car('red')
>>> ferrari.drive()
'red car goes vroom!'
```

We can also call the original `Car.drive` function. The original function does not belong to any particular `Car` object, so we must provide an explicit argument for `self`.

```
>>> ferrari = Car('red')
>>> Car.drive(ferrari)
'red car goes vroom!'
```

**\_\_init\_\_**: A special function that is called automatically when a new instance of a class is created.

Notice how the `drive` method takes in `self` as an argument, but it
looks like we didn't pass one in! This is because the dot notation
*implicitly* passes in `ferrari` as `self` for us. So in this example, `self` is bound to the
object called `ferrari` in the global frame.

To evaluate the expression `Car('red')`, Python creates a new `Car` object. Then, Python calls the `__init__` function of the `Car` class with `self` bound to the new object and `color` bound to `'red'`.

### Q1: Bank Account

Extend the `BankAccount` class to include a `transactions` attribute. This attribute should be a list that keeps track of each transaction made on the account. Whenever the `deposit` or `withdraw` method is called, a new `Transaction` instance should be created and added to the list, **even if the action is not successful**.

An instance of the `Transaction` class should have the following attributes:

* `before`: The account balance before the transaction.
* `after`: The account balance after the transaction.
* `id`: The transaction ID, which is the number of previous transactions (deposits or withdrawals) made on that account. The transaction IDs for a specific `BankAccount` instance must be unique, but this `id` does not need to be unique across all accounts. In other words, you only need to ensure that no two `Transaction` objects made by the same `BankAccount` have the same `id`.

In addition, the `Transaction` class should have the following methods:

* `changed()`: Returns `True` if the balance changed (i.e., `before` is different from `after`), otherwise returns `False`.
* `report()`: Returns a string describing the transaction. The string should start with the transaction ID and describe the change in balance. Take a look at the doctests for the expected output.

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

Use Ok to test your code:

```
python3 ok -q BankAccount

Copy

✂️
```

  

### Q2: Email

An email system has three classes: `Email`, `Server`, and `Client`. A `Client` can
`compose` an email, which it will `send` to the `Server`. The `Server` then delivers it to the
`inbox` of another `Client`. To achieve this, a `Server` has a dictionary called
`clients` that maps the name of the `Client` to the `Client` instance.

Assume that a `Client` never changes the `Server` that it uses, and it can only compose an `Email` using that `Server`.

Fill in the definitions below to finish the implementation! The `Email` class
has been completed for you.

> **Important**: Before you start, make sure you read the entire code snippet to understand the relationships between the classes, and pay attention to the parameter type of the methods. Think about what variables you have access to in each method and how can you use them to access the other classes and their methods.

> **Note:**
>
> * The `sender` parameter from the `__init__(self, msg, sender, recipient_name)` method in the `Email` class is a `Client` instance.
> * The `client` parameter from the `register_client(self, client)` method in the `Server` class is a `Client` instance.
> * The `email` parameter from the `send(self, email)` method in the `Server` class is an `Email` instance.

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

> There are two `ok` tests for this problem. Both tests must pass in order to receive full credit.
> You should run them in the order they are presented.
> The `python3 ok -q Server` test will test the `Server` class implementation, and it does not require a correct implementation of the `Client` class.
> The `python3 ok -q Client` test will test both the `Server` and `Client` class implementations.
> So, make sure to test your `Server` class implementation first before testing the `Client` class.

Use Ok to test your code:

```
python3 ok -q Server
python3 ok -q Client

Copy

✂️
```

  

Inheritance
-----------

Two classes may have similar attributes, but one represents a special case of the other. For example, a `Nickel` is a special case of a `Coin`. We say that `Nickel` is a subclass of `Coin`, and `Coin` is the base class (or superclass) for `Nickel`. In Python, the line `class Nickel(Coin):` establishes this relationship.

```
class Coin:
    cents = None  # This will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

class Nickel(Coin):
    cents = 5
```

The methods of `Coin` (such as `__init__`) are also methods for `Nickel`. So, for example, each `Nickel` instance has a `year` attribute. But class attributes or methods defined in the `Nickel` class will be found first.

```
>>> c = Nickel(1990)
>>> c.year
1990
>>> c.cents
5
```

### Q3: Mint

A mint is a place where coins are made. In this question, you'll implement a `Mint` class that can output a `Coin` with the correct year and worth.

* Each `Mint` instance has a `year` stamp. The `update` method sets the
  `year` stamp of the instance to the `present_year` class attribute of the `Mint` *class*.
* The `create` method takes a subclass of `Coin` (*not* an instance!), then
  creates and returns an instance of that subclass stamped with the `Mint`'s year (which may be different from
  `Mint.present_year` if it has not been updated.)
* A `Coin`'s `worth` method returns the `cents` value of the coin plus one
  extra cent for each year of age beyond 50. A coin's age can be determined
  by subtracting the coin's year from the `present_year` class attribute of
  the `Mint` class.

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

Use Ok to test your code:

```
python3 ok -q Mint

Copy

✂️
```

  

Check Your Score Locally
------------------------

You can locally check your score on each question of this assignment by running

```
python3 ok --score
```

**This does NOT submit the assignment!** When you are satisfied with your score, submit the assignment to Gradescope to receive credit for it.

Submit Assignment
=================

Submit this assignment by uploading any files you've edited **to the appropriate Gradescope assignment.** [Lab 00](../lab00.html#submitting-the-assignment "../lab00.html#submitting-the-assignment") has detailed instructions.

Correctly completing all questions is worth one point. If you are in the regular lab, you will need your attendance from your TA to receive that one point. Please ensure your TA has taken your attendance before leaving.

Optional Questions
==================

> These questions are optional. If you don't complete them, you will
> still receive credit for this assignment. They are great practice, so do them
> anyway!

### Q4: Next Virahanka Fibonacci Object

Implement the `next` method of the `VirFib` class. For this class, the `value`
attribute is a Fibonacci number. The `next` method returns a `VirFib` instance
whose `value` is the next Fibonacci number. The `next` method should take only
constant time.

Note that in the doctests, nothing is being printed out. Rather, each call to
`.next()` returns a `VirFib` instance. The way each `VirFib` instance is displayed is
determined by the return value of its `__repr__` method.

> *Hint*: Keep track of the previous number by setting a new instance attribute
> inside `next`. You can create new instance attributes for objects at any point,
> even outside the `__init__` method.

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

Use Ok to test your code:

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
