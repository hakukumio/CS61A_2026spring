# CS61A_笔记

## 迭代器/生成器

|对象|\_\_iter\_\_|\_\_next\_\_|
|----|----|----|
|迭代器|返回self|返回下一个元素或StopException|
|可迭代对象|返回一个新迭代器||
|生成器|返回self|返回下一个元素或StopException|

### Iterator(迭代器)

迭代器的工作是接收一序列数据,然后反复调用自己的next方法,直到遇上`StopIteration`异常。

在准确的协议约定上，即一个类内部自己实现了`__iter__`与`__next__`.而整个python，如for循环，都是围绕他们而来。基本流程就是

- 调用`__iter__`,获得迭代器.按照约定来说，他们将要返回自己
- 不断调用`__next__`，并检测到`StopIteration`异常，跳出

如下面的for循环与等价代码

```python
for x in count_down(10):
    print(x)

it = iter(count_down(10))
while True:
    try:
        x = next(it)
    except StopIterator:
        break
    print(x)
```

下面这段代码将有助于你更好了解迭代器的背后机制

```python
class count_down:
    def __init__(self,start) -> None:
        self.start = start
        iter(self)
    def __iter__(self):
        self.n = self.start
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        n = self.n
        self.n -= 1
        return n
```

我们实现了一个count_down类。接下来调用它

```shell
>>> c = count_down(10)
>>> d = count_donw(10)
>>> next(c)
10
>>> next(c)
9
>>> next(c)
8
>>> next(d)
10
>>> a = iter(c)
>>> b = iter(c)
>>> next(c)
10
>>> next(a)
9
>>> next(b)
8
>>> a is c
True
>>> a is d
False
```

### 可迭代对象

可迭代对象实质上即实现了`__iter__`的类
在这里我们必须说明即对应的iter与next这两个接口的要求

- `iter(obj)`,实际上就是调用`obj`的`__iter__`方法.同时检验`__iter__`的返回值有没有`__next__`方法。如果没有就报错，如果有就正常返回值
- `next(obj)`,就是直白地调用`obj`的`__next__`方法

由于`__iter__`与`__next__`的具体实现是没有限制的。在刚才的迭代器内我们在一个类内实现`__iter__`与`__next__`.

而对于可迭代对象而言,他们的类只需要实现`__iter__`方法，然后在`__iter__`内返回实现了`__iter__`与`__next__`的迭代器类

### Generator(生成器)

实际上Generator也算是Iterator。这在Python的官方手册内有说明。其中重要的是,是generator的构造与使用

实际上Generator产生的原因就在于，传统的迭代器是先有数据，然后一个一个去遍历。而Generator的核心就在于，其会在遍历到下一个数据的时候才进行计算“生成”这个数据,即 **惰性求值**

下面是一个简单的演示代码

```python
def fib():
    yield 1
    yield 1
    f_a = 1
    f_b = 1
    while True:
        yield f_a + f_b
        c = f_a
        f_a = f_a + f_b
        f_b = c
```

