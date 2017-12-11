import math
#asking user to enter coefficients
a = float(input("Enter a  "))
b = float(input("Enter b  "))
c = float(input("Enter c  "))

#calculate discriminant
d = b**2-4*a*c

print("Discriminant ", d)

#calculate solution according to discriminant
if d>0:
    root1 = (-b+math.sqrt(d))/(2*a)
    root2 = (-b-math.sqrt(d))/(2*a)
    print("x1 ", root1, "x2 ", root2)
elif d==0:
    root = -b / ( 2 * a )
    print("x ", root)
else:  print("no solution")