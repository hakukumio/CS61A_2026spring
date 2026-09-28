def sum_naturals(n):
    total,k = 0,1
    while k <= n:
        total,k = total +k,k+1
    return total

def sum_cubes(n):
    total,k = 0,1
    while k<n:
        total,k = total+k**3,k+1
    return total

def sum_square(n):
    total,k = 0,1
    while k<n:
        total,k = total+k**2,k+1
    return total

def pi_sum(n):
    total,k=0,1
    while k<=n:
        total,k = total + 8/((4*k-3)*(4*k-1)),k+1
    return total

def pi_item(n):
    return 8/((4*n-3)*(4*n-1))

def summation(n,term):
    total,k = 0,1
    while k<=n:
        total,k = total + term(k),k+1
    return total


#递归思想 & 函数式编程思想
#如何用于计算当中
def improve(update,close_enough,guess=1):
    if close_enough(guess):
        return guess
    else:
        return improve(update,close_enough,update(guess))

def mysqrt(x):
    def sqrt_close_enough(n):
        return abs(n**2-x) < 0.0001
    def sqrt_update(n):
        return ((n)+(x/n))/2
    def sqrt_improve():
        return improve(sqrt_update,sqrt_close_enough,x)
    return sqrt_improve


#牛顿法
#其用于求解 f(x) = 0的近似解
#属于数值计算的内容
def approx_eq(x,y,tolerent):
    return abs(x - y) < tolerent

def newton_update(f,df):
    def update(x):
        return x - f(x)/ df(x)
    return update

def find_zero(f,df):
    def near_zero(x):
        return approx_eq(f(x),0,0.0001)
    return improve(newton_update(f,df),near_zero)

def newton_sqrt(x):
    def f(n):
        return n**2 -x
    def df(n):
        return 2*n
    return find_zero(f,df)

def newton_power(n,x):
    def f(a):
        return a**n-x
    def df(a):
        return n*(a**(n-1))
    return find_zero(f,df)

# Lambda
# 非常有意思的东西
def composel(f,g):
    return lambda x: f(g(x))

def sum_range(start,end,step):
    if start>end:
        return -1
    else:
        return summation((end-start)//step+1,lambda x:(start + (x-1)*step))
