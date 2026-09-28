def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last,last = n // 10, n %10
        return sum_digits(all_but_last) + last

def fact_iter(N):
    total,k = 1,1
    while k<=N:
        total *= k
        k += 1
    return total

def fact_recu(N):
    if N == 1 or N == 2:
        return N
    if N <= 0:
        return -1
    k = N
    return k*fact_recu(k-1)

#multiple recursive
#but remenber is that Python isn't scheme
#so if N is too big,it will encounter "recursive depth Error"
def is_odd(N):
    if N == 0:
        return False
    return is_even(N-1)

def is_even(N):
    if N == 0:
        return True
    return is_odd(N-1)

#print recursive
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

def alice_play(n):
    if n == 0:
        print('Bob wins')
    else:
        print("Alice removed one,n = ",n-1)
        return bob_play(n-1)

def bob_play(n):
    if n == 0:
        print("alice wins")
    elif is_even(n):
        print('Bob removed two,n = ',n-2)
        alice_play(n-2)
    else:
        print('Bob removed one,n = ',n-1)
        alice_play(n-1)

    # tree recursion

def fibs(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibs(n-1)+fibs(n-2)

def count_partition(n,m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 1:
        return 1
    else:
        return count_partition(n-m,m)+count_partition(n,m-1)

def get_money(n,len,list):
    if n == 0:
        return 1
    elif n<0:
        return 0
    elif len == 1:
        return 1
    else:
        return get_money(n-list[len-1],len,list)+get_money(n,len-1,list)

def get_money_print(amount,coins):
    dp = [0]*(amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin,amount+1,1):
            dp[i] += dp[i-coin]
    return dp[amount]