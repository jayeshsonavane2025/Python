def linearSearch():
    list1 = list(map(int, input().split()))
    key = int(input("Enter key to be searched"))
    for i in range(len(list1)):
        if key == list1[i]:
            print(key, " found at ", i + 1)
            exit()
    print(key, "Not found in array")


linearSearch()
