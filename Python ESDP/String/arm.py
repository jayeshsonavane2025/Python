def myPow(x, n):
    res = 1
    for i in range(0, n):
        res *= x
    return res


def arm():
    n = int(input("Enter Number"))
    temp = n
    temp2 = n
    res = 0
    count = 0
    sum = 0
    while n != 0:
        count += 1
        n //= 10
    print(count)
    while count != 0:
        rem = temp % 10
        rem = pow(rem, count)
        sum += rem
        temp //= 10
        count -= 1

    print(sum)
    if sum == temp2:
        print(temp2, " is Armstrong Number")
    else:
        print(temp2, " not Armstrong")


arm()
