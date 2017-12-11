import math
class Triangle:
   
    def calculateSquare(self,a,b,c):
        p=(float(a)+float(b)+float(c))/2
        return math.sqrt(p*(p-float(a))*(p-float(b)*(p-float(c))))


class Rectangle:
    def calculateSquare(self, a,b):
        return float(a)*float(b)

class Circle:

    def calculateSquare(self, radius):
        return math.pi*float(radius)


figure = input("Enter figure type: 1 - triangle, 2 - rectangle, 3 - circle ")
if figure == "1":
    triangle=Triangle()
    a = input("Enter a side length ")
    b = input("Enter b side length ")
    c = input("Enter c side length ")
    print(triangle.calculateSquare(a,b,c))
elif figure=="2":
    rectangle=Rectangle()
    a = input("Enter a side length ")
    b = input("Enter b side length ")
    print(rectangle.calculateSquare(a,b))
elif figure=="3":
    circle = Circle()
    radius = input("Enter radius ")
    print(circle.calculateSquare(radius))

