class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    def __mul__(self,other):
        return self.x*other.x+self.y*other.y+self.z*other.z
    def __str__(self):
        return f"{self.x}i+{self.y}j+{self.z}k"
    def __len__(self):
        return 3
v1=Vector(3,4,5)
v2=Vector(7,8,9)
print(v1+v2)
print(v1*v2)
print(len(v1))