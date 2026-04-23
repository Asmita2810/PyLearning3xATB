#write a program that classifies a triangle based on its side lengths

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Check if it's a valid triangle
if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

else:
    print("Not a valid triangle")