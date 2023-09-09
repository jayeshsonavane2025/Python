def maxItem(list):
    max1 = list[0]
    for item in list:
        if item > max1:
            max1 = item
    print("Max :", max1)


def minItem(list):
    min1 = list[0]
    for item in list:
        if item < min1:
            min1 = item
    print("Min :", min1)


maxItem([1, 4, 6, 89, 3, 2, 4, 5])
minItem([1, 4, 6, 89, 3, 2, 4, 5])

print(float("inf"))
