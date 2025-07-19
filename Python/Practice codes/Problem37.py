import math
n = int(input("Enter Your Number:- "))
l = []
r = 0 
for i in range (1,n+1):
    r = r+1
    l.append(r)
print(math.prod(l))

product = 1 
for i in range (1,n+1):
    product = product * i 
print(product)