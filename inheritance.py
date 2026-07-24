import random
class travel:
    name="Arghya"
    def getInfo(self):
        print(f"The name of the passenger is {self.name}")
class travel2(travel):
    fro="Delhi"
    to="Noida"
    def from_and_to(self):
        print(f"The passenger is travelling from {self.fro} to {self.to}")
class travel3(travel2):
    cost=random.randint(252,456)
    def fare(self):
        print(f"The cost of the fare of the passenger is {self.cost}")
a=travel3()
a.getInfo()
a.from_and_to()
a.fare()