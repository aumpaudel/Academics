with open ("lod.txt") as f :
    s = f.read()

with open ("1poem.txt") as f :
    t = f.read()

if s==t:
    print("IDENTICAL")
else:
    print("NON IDENTICAL")