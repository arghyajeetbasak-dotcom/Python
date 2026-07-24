class Employee:
    name="Harry"
    age=18
    lang="Python"
    def __init__(self,name,age,lang):
        self.name=name
        self.age=age
        self.lang=lang
        print("Thank you for reading this program")
    def generate(self):
        print(f"Yo guys I'm {self.name}")
content=Employee("Arghya",18,"Javascript")
# content.name="Arghya"
print(content.name,content.age,content.lang)
content.generate()