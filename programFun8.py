def areaTriangle(base, height):
    ans = (base*height)*0.5
    return ans

triangleBase = float(input("Enter base of the triangle: "))
triangleHeight = float(input("Enter height of the triangle: "))
area = areaTriangle(triangleBase, triangleHeight)
print("Area of the triangle is ===> ", area)