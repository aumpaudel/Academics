f = open("1poem.txt")
content = f.read()
if "Twinkle" in content:
    print("present in file")
else:
    print("not found")