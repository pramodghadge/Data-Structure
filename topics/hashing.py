import math

def myHash(key, size):
    return (hash(key) & 0x7fffffff) % size


if __name__ == '__main__':
    size =10000
    print myHash('Star', size)