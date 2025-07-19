class C_2dvector():
    def axis(self, x, y):
        self.x = x
        self.y = y

class C_3dvector(C_2dvector):
    def axis(self, x, y, z):
        super().axis(x, y)
        self.z = z

c2 = C_2dvector()
c3 = C_3dvector()

c2.axis(2,3)
print(c2.x, c2.y)
c3.axis(2,3,4)
print(c3.x, c3.y, c3.z)