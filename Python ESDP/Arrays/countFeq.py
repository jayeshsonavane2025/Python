def countFrequency(list):
    vis = []
    item = 0

    for i in list:
        if i not in vis:
            vis.append(i)
            c = 0

            for item in list:
                if i == item:
                    c += 1
            print(i, " = ", c)


countFrequency([1, 3, 1, 6, 2, 34, 5, 5, 3, 2, 3, 2])
