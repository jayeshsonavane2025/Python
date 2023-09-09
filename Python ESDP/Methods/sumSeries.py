def sumOfSeries(n):
    sum = 0
    for i in range(0, n + 1):
        if i % 2 == 0:
            sum += i
    print(sum)


n = int(input())
sumOfSeries(n)
# print("Sum of series is :", sum)
