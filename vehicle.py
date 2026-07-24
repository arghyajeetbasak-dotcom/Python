class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def __init__(self, brand, model,fuel_type):
        super().__init__(brand, model)
        self.fuel_type=fuel_type
    def display(self):
        print(f"Fuel type of {self.brand} {self.model} is {self.fuel_type}")
ob=Car("Toyota","AMD63","Petrol")
ob.display()