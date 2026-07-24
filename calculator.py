class Calculator:
    def __init__(self,n):
        self.n=n
    def operations(self):
        print("Square is",self.n*self.n)
        print("Cube is",self.n*self.n*self.n)
        print("Square root is",self.n**0.5)
    @staticmethod
    def greet():
        print("Hello user")
a=Calculator(4)
a.greet()
a.operations()    