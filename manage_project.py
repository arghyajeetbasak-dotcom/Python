class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f"Name: {self.name} and age: {self.age}")
class Student(Person):
    def __init__(self, name, age,roll,marks):
        super().__init__(name, age)
        self.roll=roll
        self.marks=marks
    def grade(self):
        if(self.marks>=90):
            grade="A"
        elif(self.marks>=75 and self.marks<90):
            grade="B"
        elif(self.marks>=60 and self.marks<75):
            grade="C"
        else:
            grade="D"
        return grade
class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject=subject
        self.salary=salary
    def details2(self):
        print(f"The teacher's salary is {self.salary} and he/she is expert in {self.subject}")
a=Student("Arghyajeet",19,37,99)
a.details()
print(f"Student's grade is: {a.grade()}")

b=Teacher("Sharanya",35,"Mathematics",1220)
b.details()
b.details2()