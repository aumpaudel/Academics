import random 

def game():
    score = random.randint(1,70)
    print(score)
   
    with open ("hiscore.txt", "r") as f :
        l = f.read()
        if (l == ""):
            l =0
        else:
            l = int(l)
            
    if (l<score):
        with open ("hiscore.txt", "w") as f :
            f.write(str(score))

game()