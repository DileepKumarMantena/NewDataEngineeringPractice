class Vehicle:
    def start(self):
        print("Vehicle starts")


class Car(Vehicle):
    def start(self):
        print("Car starts")


vehicle = Vehicle()
car = Car()


vehicle.start()
car.start()