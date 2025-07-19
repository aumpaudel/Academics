words = ["donkey", "bc", "bad"]

with open ("donkey.txt", "r") as f :
    s = f.read()

for word in words:
    s = s.replace(word,"#" * len(word))
    with open ("donkey.txt" , "w") as f :
        f.write(s)

