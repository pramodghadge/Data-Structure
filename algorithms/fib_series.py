from functools import wraps

def fib(n):
    a = b = 1
    while b < n:
        yield b
        a, b, = b , a + b

def memorize(func):
    memo = dict()
    @wraps(func)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = func(*args)
            memo[args] = rv
            return rv
    return wrapper


@memorize
def fibr(n):
    if n < 0:   #base condition
        return 1
    return fibr(n - 2) + fibr(n - 1)

if __name__ == '__main__':
    for i in fib(20):
        print i

    for i in range(10):
        print fibr(i)