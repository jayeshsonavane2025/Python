def binarySearch(ls, key, start, end):
    s = 0
    e = len(ls) - 1
    mid = 0
    last = 0
    while s <= e:
        if start == end:
            print("last occurence at", last)

            break
        mid = (s + e) // 2
        if ls[mid] == key:
            last = key
            print(key, " found at ", mid)
            binarySearch(ls, key, mid + 1, end)
            break
        elif ls[mid] > key:
            e = mid - 1
        else:
            s = mid + 1
    else:
        print(key, " not found")


ls = list(map(int, input().split()))
key = int(input("Enter key to be searched"))
binarySearch(ls, key, 0, len(ls))
