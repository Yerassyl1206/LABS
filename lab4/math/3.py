import math
s=int(input("side:"))
l=int(input("lengh:"))
a = (s * (l**2))/(4*math.tan(math.pi / s))
print(int(a))