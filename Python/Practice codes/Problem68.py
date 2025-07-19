a:int = int(input("enter the number: "))
b:int = int(input("enter the number: "))

def division():
    try:
         print(a/b)
    except ZeroDivisionError:
        print("infinity")

division()