def fib_gen(n):
    a, b = 0,1
    while b < n:
        yield b
        a, b = b, a+b

from functools import wraps

def memoise(func):
    repo = dict()
    @wraps(func)
    def wrapper(args):
        if args in repo:
            out = repo[args]
        else:
            out = func(args)
            repo[args] = out
        return out
    return wrapper


@memoise
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    # for i in fib_gen(100):
    #     print i

    for i in range(10):
        print fib(i)
