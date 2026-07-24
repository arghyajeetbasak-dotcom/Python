class Info:
    language="Python"
    salary=1200000
    def __init__(self,name,age,language):
        self.name=name
        self.age=age
        self.language=language
        print("Welcome, user!")
    def details(self):
        print(f"The salary of the user {self.name} aged {self.age} is {self.salary} and its language is {self.language} ")
    @staticmethod
    def greet():
        print("End")

arghya=Info("Arghya",19,"C++")
# arghya.name="Arghya"
# arghya.language="C++"
arghya.details()
arghya.greet()