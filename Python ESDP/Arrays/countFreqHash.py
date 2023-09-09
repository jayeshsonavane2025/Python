def countFrequencyHashMap(ls):
    d = {}
    for item in ls:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1

    print(d)


# from collections import defaultdict


countFrequencyHashMap([1, 1, 1, 1, 2, 3, 4, 5, 4, 5, 5])
