f = open("lod.txt")
n = 0
while n<4100:
    n += 1
    s = f.readline()
    if "Python" in s:        
        print("present in line:",  n)
        break
    
else:        
    print("not found")

f.close()