class twodvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        print(f"{self.i}i + {self.j}j")
class threedvector(twodvector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k=k
        print(f"{self.i}i + {self.j}j + {self.k}k")
obj2=threedvector(7,5,9)

class Animals:
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("Bark")
o=Dog()
o.bark()

class Employee:
    salary=1200
    increment=20
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary*(self.increment/100))
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment=100*((salary/self.salary)-1)
    
e=Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement=1300
print(e.increment)