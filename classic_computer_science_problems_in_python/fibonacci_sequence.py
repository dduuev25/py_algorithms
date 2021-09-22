# 斐波那契数列
from functools import lru_cache
# 使用递归方法


# 每次调用任意f(n)的时候，都要重新计算
def fib1(n:int)->int:
    if n < 2:
        return n
    else:
        res = fib1(n-1) + fib1(n-2)
        return(res)

# 每次调用任意f(n)的时候，都要重新计算
def fib2(n:int)->int:
    memo = {0:0,1:1}
    if n not in memo:
        memo[n] = fib2(n-1)+fib2(n-2)
    return memo[n]
# 以上两种方法，每次调用任意f(n)的时候，都要重新计算

@lru_cache(maxsize=None)
def fib3(n:int)->int:
    if n < 2:
        return n
    return fib3(n-1)+fib3(n-2)


# 迭代法
def fib4(n:int)->int:
    if n==0:
        return n
    item:int = 0 #初始化 f(0)
    next_item:int = 1 #初始化 f(1)

    for i in range(1,n):
        item,next_item = next_item,item+next_item
    return next_item


if __name__ == "__main__":
    print(fib3(500))
    print(fib4(500))