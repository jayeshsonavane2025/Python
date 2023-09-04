#method for addition
def add(a, b):
    #typecasting to int
    return int(a) + int(b)

a = input("Enter a: ")
b = input("Enter b: ")

#calling method
result = add(a, b)

print("The addition of " + a + " and " + b + " is " + str(result))
