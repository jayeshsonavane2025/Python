def nFibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return nFibonacci(n - 1) + nFibonacci(n - 2)


n = int(input("Enter number"))
print(n, " fibonacci is ", nFibonacci(n))
