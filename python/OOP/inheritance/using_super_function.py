class Vehicle:
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def show_details(self):
        print("Vehicle is of", self.brand, 'brand')
        print("cost of the vehicle is:", self.cost)

class Car(Vehicle):
    def __init__(self, brand, cost, hp, tyres):
        super().__init__(brand, cost)
        self.hp = hp
        self.tyres = tyres

    def show_car_details(self):
        print("I am a car")
        print("HP:", self.hp)
        print("TYRES:", self.tyres)

c1 = Car("Toyota", 1600000, 1200, 4)
c1.show_details()
# c1.show_car_details()