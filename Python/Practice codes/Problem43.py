n = int(input("Enter Your Number:- "))
i = 0
def pattern (n):
   for i in range (0,n+1):
      print("*"*(n-(i)),end=(""))
      print("")
      
pattern(n)