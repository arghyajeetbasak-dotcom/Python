class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        if(self.l<0 and self.b<0):
            print("Invalid dimensions")
    def area(self):
        print(f"Area = {self.l*self.b}")
    def perimeter(self):
        print(f"Perimeter = {2*(self.l+self.b)}")
obj=Rectangle(78,37)
obj.area()
obj.perimeter()