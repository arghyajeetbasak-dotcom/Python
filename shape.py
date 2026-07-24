class Shape:
    def __init__(self,colour):
        self.colour=colour
    def display(self):
        print(f"colour is {self.colour}")
class Rectangle(Shape):
    def __init__(self,colour,length,width):
        super().__init__(colour)
        self.length=length
        self.width=width
    def area(self):
        print(f"Area = {self.length*self.width}")
obj1=Rectangle("red",178,32)
obj1.area()