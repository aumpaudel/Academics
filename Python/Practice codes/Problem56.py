class Employee :
    def information (self):
        self.name = "Aum"
        self.salary = "100k"
        self.company = "Microsoft"
        self.profesion = "Programmer"

e1 = Employee()
e1.information() 

print("Name:", e1.name)
print("Salary:", e1.salary)
print("Company:", e1.company)
print("Profession:", e1.profesion)