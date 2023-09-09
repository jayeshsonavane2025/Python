def separateDigits(list):
    res = []
    for item in list:
        if item < 0:
            res.append(item)
    for item in list:
        if item == 0:
            res.append(item)

    for item in list:
        if item > 0:
            res.append(item)
    print(res)


separateDigits([1, -1, 0, 0, 4, -2, -5, 9, 3, -8, 2, -7, 92, -6, -33, 8, 56, 34])
#remaining not perfect 