#parent class
class Vehicle:
    def __init__(self, brand, cost, Mialage):
        self.brand = brand
        self.cost = cost
        self.Mialage = Mialage

    def show_details(self):
        print("Brand name of the car is:", self.brand)
        print("Cost of the car is:", self.cost)
        print("Mialage of the car is:", self.Mialage)
        
#child class
class Car(Vehicle):
    def car_detail(self):
        print("I am a car")

c1 = Car("Ford", 1200000, 13)  #child class accquire the the attributes of the parent class
c1.show_details()
c1.car_detail()