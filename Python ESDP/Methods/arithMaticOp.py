def add(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div


a, b = map(int, input().split())
sum, sub, mul, div = add(a, b)
print("Sum :", sum)
print("Sub :", sub)
print("Mul :", mul)
print("Div :", div)
