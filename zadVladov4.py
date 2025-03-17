class Vehicle:
    def __init__(self, brand, godina):
        self.brand = brand
        self.godina = godina
    def start(self):
        print(f"{self.brand} ({self.godina}) is starting.")
    def stop(self):
        print(f"{self.brand} is stopping.")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} is driving.")

class Bicycle(Vehicle):
    def pedal(self):
        print(f"{self.brand} is pedaling.")

class Motorcycle(Vehicle):
    def ride(self):
        print(f"{self.brand} is riding.")

if __name__ == "__main__":
    toiota = Car("Toyota", 20200)
    bicycle = Bicycle("Generic", 20190)
    
    toiota.start()
    toiota.drive()
    bicycle.pedal()
    toiota.stop()
