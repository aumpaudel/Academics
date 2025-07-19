def greatest ():
    n1 = int(input("Enter your number:- "))
    n2 = int(input("Enter your number:- "))
    n3 = int(input("Enter your number:- "))
    if (n1>n2 and n1>n3):
        print(f"{n1} is the greatest nuber")
    if (n2>n1 and n2>n3):
        print(f"{n1} is the greatest nuber")
    if (n3>n2 and n3>n1):
        print(f"{n1} is the greatest nuber")

greatest()