a = int(input("Enter Your Subject Marks:- "))
b = int(input("Enter Your Subject Marks:- "))
c = int(input("Enter Your Subject Marks:- "))
d = a+b+c 

if(a>=40):
    print("Pass in 1st Subject")
else:
    print("Fail in 1st Subject")

if(b>=40):
    print("You are Pass in Subject 2")
else:
    print("You are fail in Subject 2")

if(c>=40):
    print("You are Pass in Subject 3")
else:
    print("You are fail in Subject 3")

if(d>=99):
    print("You Are Pass in the exam")
else:
    print("You are fail in exam")