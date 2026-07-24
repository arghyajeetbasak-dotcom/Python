class Employee:
    a=5
    @classmethod
    def show(cls):
        print(f"Class value of a is {cls.a}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
    def __add__(self, other):
        return self.a + other.a
# obj=Employee()
# obj.name="Arghyajeet Basak"
# print(obj.name)
# obj.a=22
# obj.show()
a=Employee()
b=Employee()
print(a+b)