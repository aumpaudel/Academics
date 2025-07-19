class Cube_Squareroot() :
    @staticmethod
    def welcome():
        print("Hello")
    def __init__(self, number):
        self.number = number
    def cube(self):
        print("Cube: ",self.number**3)
    def square(self):
        print("Square: ",self.number**2)
    def squareroot(self):
        print("Squareroot: ",self.number**(1/2))

# n = int(input("Enter Your Number:- "))
cs = Cube_Squareroot(4)

cs.welcome()
cs.cube()
cs.square()
cs.squareroot()