#Hypotenusa of a right triangle
# c= sqrt(a²+b²) 
import math

leg1 = float(input("Type first leg: ")) 
leg2 = float(input("Type second leg: "))
hypotenuse = math.sqrt((leg1**2) + (leg2**2))
print(hypotenuse)