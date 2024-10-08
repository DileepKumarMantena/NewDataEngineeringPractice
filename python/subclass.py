# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"Vehicle Brand: {self.brand}, Model: {self.model}"


# Subclass Car
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Inherit brand and model from Vehicle
        self.doors = doors

    def get_info(self):
        return f"Car Brand: {self.brand}, Model: {self.model}, Number of Doors: {self.doors}"


# Subclass Bike
class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)  # Inherit brand and model from Vehicle
        self.bike_type = bike_type

    def get_info(self):
        return f"Bike Brand: {self.brand}, Model: {self.model}, Type: {self.bike_type}"


# Demonstration
# Creating objects of each class
vehicle = Vehicle("Generic", "V1")
car = Car("Toyota", "Camry", 4)
bike = Bike("Yamaha", "MT-15", "Sport")

# Displaying the details using get_info()
print(vehicle.get_info())  # Output from base class
print(car.get_info())      # Output from Car subclass
print(bike.get_info())     # Output from Bike subclass