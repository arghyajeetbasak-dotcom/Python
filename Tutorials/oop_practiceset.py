class Programmer:
    company="Microsoft"
    def __init__(self,name,salary):
        self.name=name  
        self.salary=salary     
p1=Programmer("Arghya",1500000)
print(p1.name,p1.company,p1.salary)

p2=Programmer("Shubham",1300000)
print(p2.name,p2.salary,p2.company)


class Calculator:
    def __init__(self,num):
        self.num=num
    def operations(self):
        print(f"Square is {self.num*self.num}")
        print(f"Cube is {self.num*self.num*self.num}")
        print(f"Square root is {self.num**(1/2)}")
    @staticmethod
    def greet():
        print("Hello")
num1=Calculator(4)
num1.greet()
num1.operations()

class Attribute:
    a=23
obj=Attribute()
obj.a=0
print(obj.a)
print(Attribute.a)

import random
class Train:
    def __init__(self,trainNo,fro,to):
        self.trainNo=trainNo
        self.fro=fro
        self.to=to
    def bookTicket(self):
        print(f"Train no {self.trainNo} is booked from {self.fro} to {self.to}")
    def status(self):
        print(f"Train no {self.trainNo} is running on time")
    def getFare(self):
        print(f"Fare of train {self.trainNo} running from {self.fro} to {self.to} is {random.randint(400,2000)}")
obj=Train(12338799,"Kolkata","Siliguri")
obj.bookTicket()
obj.status()
obj.getFare()
