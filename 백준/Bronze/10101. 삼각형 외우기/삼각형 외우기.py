import sys

triangle = []

for i in range(3):
    angle=int(sys.stdin.readline())
    triangle.append(angle)

if sum(triangle)!=180:
    print("Error")
else:
    if triangle[0]==triangle[1]==triangle[2]==60:
        print("Equilateral")
    elif triangle[0]==triangle[1] or triangle[0]==triangle[2] or triangle[1]==triangle[2]:
        print("Isosceles")
    else:
        print("Scalene")