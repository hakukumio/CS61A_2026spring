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

class fib_class():
    def __init__(self,start=0,end=-1) -> None:
        if start < 0 or end < start:
            raise ValueError
        self.start = start
        self.end = end