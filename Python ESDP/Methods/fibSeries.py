def fibSeries(n):
    a = 0
    b = 1
    c = 0
    for i in range(0, n):
        c = int(a + b)
        a = b
        b = c
        print(c, " ", end="")


a = int(input())
print("The series fibonacci series upto terms", a)
fibSeries(a)
