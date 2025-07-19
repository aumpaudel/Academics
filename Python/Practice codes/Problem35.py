n = int(input("Enter Your Number:- "))
for i in range (1, n+1):
    print(" "* (n-i),end="")
    print("*"* (2*i-1),end="")
    print("")

for i in range (1,n+1):
    print("*"*(i),end=(""))
    print("")

for i in range (1,n+1):
    if(i==n or i==1):
        print("*"*(n),end=(""))
        print("")
    else:
        print("*"*(1),end=(""))
        print(" "*(n-2),end=(""))
        print("*"*(1),end=(""))
        print("")