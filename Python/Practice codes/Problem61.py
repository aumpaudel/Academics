class Employee():
    def __init__(self):
        self._Salary = "75k"
        self._Company = "Google" 
        self._Post = "Cook"
    @property
    def salary(self):
        return self._Salary 
    @salary.setter
    def salary(self, value):
        self._Salary = value 

e = Employee()
print(e.salary)

e.salary = "85k"
print(e.salary)