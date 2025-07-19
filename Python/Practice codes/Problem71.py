numbers = []
for i in range (1,101):
    numbers.append(i)

def funcn(x):
    if (x%5==0):
        return True 
    
filtered = list(filter(funcn,numbers))

print(filtered)