class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no
    def display(self):
        print(f"Student name: {self.name}\nAge: {self.age}\nRoll No: {self.roll_no}")
a=Student("Arghya",19,37)
a.display()
        