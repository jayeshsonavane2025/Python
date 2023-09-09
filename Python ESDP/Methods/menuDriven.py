import sys


def add():
    a, b = map(int, input("Enter two numbers").split())
    print("Sum is ", a + b)


def sub():
    a, b = map(int, input("Enter two numbers").split())
    print("Sub is ", a - b)


def mul():
    a, b = map(int, input("Enter two numbers").split())
    print("Mul is ", a * b)


def div():
    a, b = map(int, input("Enter two numbers").split())
    print("Div is ", a / b)


def fact():
    a = int(input("Enter the number:"))
    fact = 1
    for i in range(1, a + 1):
        fact = fact * i
        print(fact)


def pow():
    x, n = map(int, input("Enter x,n").split())
    res = 1
    for i in range(0, n):
        res *= x
    print("Factorial :", res)


def rev():
    s = input("Enter String")
    print(s, " reverse is ", s[::-1])
    # print(s, " reverse is ", "".join(reversed(s)))


def pal():
    s = input("Enter String :")

    start = 0
    end = len(s) - 1
    while start <= end:
        if s[start] != s[end]:
            print(s, " is not Palimndrome")
            break
        start += 1
        end -= 1
    else:
        print(s, " is  palindrome")


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
        # for i in range(0, count):
        #     rem *= rem
        sum += rem
        temp //= 10
        count -= 1

    print(sum)
    if sum == temp2:
        print(temp2, " is Armstrong Number")
    else:
        print(temp2, " not Armstrong")


while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Divisuion")
    print("5.Factorial Number")
    print("6.Find Power")
    print("7.Reverse")
    print("8.Palindrome")
    print("9.Armstrong Number")
    print("10.Exit")

    choice = int(input())
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        fact()
    elif choice == 6:
        pow()
    elif choice == 7:
        rev()
    elif choice == 8:
        pal()
    elif choice == 9:
        arm()
    elif choice == 10:
        sys.exit()
    else:
        print("Enter valid choice")
