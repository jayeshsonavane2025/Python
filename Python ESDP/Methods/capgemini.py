def knowMax():
    ls = []
    n = int(input("Enter number of semesters :"))
    for j in range(0, n):
        nsub = int(input(f"Enter number of subjcts for {j+1} semester"))
        for i in range(0, nsub):
            ls1 = []
            sub = int(input(f"Enter subjcts {i+1} marks:"))
            ls1.append(sub)

        ls.append(ls1)
    k = 1
    for i in ls:
        print("Maximum in ", k, " semester ", max(i))
        k += 1


knowMax()
