class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __add__(self, other):
        return Vector(self.i+other.i,self.j+other.j,self.k+other.k)
    def __mul__(self, other):
        return self.i*other.i+self.j*other.j+self.k*other.k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __len__(self):
        l=[self.i,self.j,self.k]
        return(len(l))
a=Vector(1,2,3)
b=Vector(4,5,6)
print(a+b)
print(a*b)
print(len(a))