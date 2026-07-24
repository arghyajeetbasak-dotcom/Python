class Vector:
    def __init__(self,vec):
        self.vec=vec
    def __len__(self):
        return len(self.vec)
v1=Vector([1,2,3])
print(len(v1))