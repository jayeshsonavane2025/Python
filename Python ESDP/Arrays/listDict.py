from collections import defaultdict


def listDisplay(ls):
    d = defaultdict(list)
    for i in ls:
        d[i // 10].append(i)
    for k, v in d.items():
        print(k, v)


listDisplay([1, 23, 4, 4, 44, 66, 45, 33, 22, 9, 56, 4, 24, 67, 89, 44])
