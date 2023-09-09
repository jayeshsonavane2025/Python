# def zigZag(ls):
#     for i in range(len(ls)):
#         for j in range(len(ls[i])):


# zigZag([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])


mat = []
for i in range(4):
    row = list(map(int, input().split()))
    mat.append(row)
print()

for i in range(4):
    if i % 2 == 0:
        for j in range(4):
            print(mat[j][i], end=" ")
    else:
        for j in range(3, -1, -1):
            print(mat[i][j], end=" ")
    print()
