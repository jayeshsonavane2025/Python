def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False


def prime1To100():
    for i in range(1, 101):
        if isPrime(i) == False:
            print(i, " ", end=" ")


prime1To100()
