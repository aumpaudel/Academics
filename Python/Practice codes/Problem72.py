from functools import reduce
numbers = []
for i in range (1,1199):
    numbers.append(i)

func = lambda x,y: x if x>y else y 

val = reduce(func, numbers)
print(val)