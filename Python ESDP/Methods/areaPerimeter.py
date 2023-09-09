def areaPerimeter(l, b):
    area = l * b
    peri = 2 * l * b
    return area, peri


l, b = map(int, input().split())

area, peri = areaPerimeter(l, b)

print("Area :", area)
print("perimeter :", peri)
