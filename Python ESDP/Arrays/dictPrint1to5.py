def dictPrint1toN(n):
    d = {}
    for i in range(1, n + 1):
        d[i] = i * i
        print(i, d[i])
    print(d)


dictPrint1toN(10)
