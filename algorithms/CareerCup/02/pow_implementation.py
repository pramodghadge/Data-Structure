def calculatePower(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n > 1:
        return pow(x,n)
    elif n < 0:
        p = pow(x, abs(n))
        return 1 / float(p)

def pow(x,n):
    out = 1
    for i in range(n):
        out *= x
    return out

if __name__ == '__main__':
    print calculatePower(2,0)