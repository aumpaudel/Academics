l = ["Rohan", "Aum", "Binwant", "Daman", "Khushman", "Aditya", "Ramesh", "Krish"]
print(f"list={l}")

def remove_list():
    name = input("Enter Name You want to Remove from list:- ")
    l.remove(name)
    return l
a = remove_list()
print(a)