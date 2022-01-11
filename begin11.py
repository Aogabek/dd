from math import *

a = int(input("Nolga teng bolmagan birinchi sonni kiritng: "))
b = int(input("Nolga teng bolmagan ikkinchi sonni kiritng: "))

if a>0 and b>0:
    s= a+b
    i= a*b
    h= fabs(a)
    j= fabs(b)
    print("Natija: ", s,i,h,j)
else :
    print("Sonlar nolga teng")