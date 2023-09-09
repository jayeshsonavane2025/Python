def myPow(x, n):
    res = 1
    for i in range(0, n):
        res *= x
    return res


x, n = map(int, input().split())

print("Power is :", myPow(x, n))
