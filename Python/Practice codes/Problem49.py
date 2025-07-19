import os 
os.makedirs("tables", exist_ok=True)

def table(n):
    content = ""
    for i in range (1,11):
        content += f"{n} x {i} = {n*i} \n"
    return content

n = 2 
while n in range (2,21):
    file_path = os.path.join("tables", f"{n}.txt") 
    with open(file_path, "w") as f:
        f.write(table(n))
    n += 1