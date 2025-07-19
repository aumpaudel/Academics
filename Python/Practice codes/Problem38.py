# prime number or not
n = int(input("Enter your number:- "))
for i in range (2,n):
    if n%i == 0:
        print("Number Is Not Prime")
        break
else:
    print("Number Is Prime")