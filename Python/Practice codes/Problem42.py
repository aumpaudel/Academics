n = int(input("Enter number:- "))
def suml(n):
    if (n==1):
        return 1 
    else:
        return (n + suml(n-1))

a = suml(n)
print(f"sum is {a}")