def fib_gen(n):
    a , b = 0, 1
    while b < n:
        yield b
        a,b = b, a+b


def fib_rec(n):
    if n < 2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


if __name__ == '__main__':
    # for i in fib_gen(100):
    #     print i
    for i in range(1, 10):
        print fib_rec(i)