class Complex():
    def number1(self, valuex1, valuey1):
        self.x1 = valuex1
        self.y1 = valuey1
        self.Complex1 = self.x1 + self.y1
    def number2(self, valuex2, valuey2):
        self.x2 = valuex2
        self.y2 = valuey2 
        self.Complex2 = self.x2 + self.y2
    def answer(self):
        self.x = ""
        self.y = ""
    @property
    def ad(self):
        real = self.x1 + self.x2
        imag = self.y1 + self.y2
        return f"{real} + {imag}i"
    @property
    def ml(self):
        real = (self.x1*self.x2) - (self.y1*self.y2)
        imag = (self.x1*self.y2) + (self.x2*self.y1)
        return f"{real} + {imag}i"
    def dimension(self):
        return 2

c = Complex()

c.number1(3,4)
c.number2(2,5)

print(f"Addition of both complex number is {c.ad}")
print(f"Multiplication of both complex number is {c.ml}")
print(f"Dimension of complex numbers: {c.dimension()}")