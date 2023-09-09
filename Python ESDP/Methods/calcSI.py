def calculateSI(p, n, r):
    return p * n * r / 100


p, n, r = map(int, input().split())
print("Simple Interest on P=", p, " N=", n, " R=", r, " is ", calculateSI(p, n, r))
