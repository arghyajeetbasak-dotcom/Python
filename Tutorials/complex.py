class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self, value):
        return Complex(self.r+value.r,self.i+value.i)
    def __mul__(self, value):
        real=self.r * value.r - self.i * value.i
        imag=self.r * value.i + self.i * value.r
        return Complex(real,imag)
    def __str__(self):
        return f"{self.r} + {self.i}i"
c1=Complex(2,5)
c2=Complex(3,6)
print(c1+c2)
print(c1*c2)
