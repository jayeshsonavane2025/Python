def secondmax(list):
    max = list[0]
    smax = list[0]
    for item in list:
        if item > max:
            smax = max
            max = item
            # continue
        if item > smax and item < max:
            smax = item
    print(smax)


secondmax([1, 56, 3, 5, 7, 3, 6, 322])
