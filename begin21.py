from math import*

x1 = int(input("Son kiriting: "))
x2 = int(input("Son kiriting: "))
y1 = int(input("Son kiriting: "))
y2 = int(input("Son kiriting: "))
x3 = int(input("Son kiriting: "))
y3 = int(input("Son kiriting: "))

a = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
b = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2))
c = sqrt(pow(x3 - x2, 2) + pow(y2 - y1, 2))

p = (a + b + c)/2
S = sqrt(p(p-a)(p-b)(p-c))
print("Natija:",S,p)
