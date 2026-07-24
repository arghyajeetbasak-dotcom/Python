class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display_details(self):
        print(f"Student name: {self.name}")
        print(f"Roll no: {self.roll_no}")
        print(f"Marks: {self.marks}")
    def calculate_grade(self):
        if(self.marks>=90 and self.marks<100):
            grade="A"
            return grade
        elif(self.marks>80 and self.marks<90):
            grade="B"
            return grade
        else:
            grade="C"
            return grade
obj=Student("Arghyajeet",37,97)
obj.display_details()
print(obj.calculate_grade())
